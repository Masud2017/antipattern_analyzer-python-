import ast
import os
import json
from collections import defaultdict
from concurrent.futures import Executor

# -------------------------
# Map detectors
# -------------------------
anti_pattern_detectors = {
    "CatchAndDoNothing": detect_catch_and_do_nothing,
    "CatchAndReturnNone": detect_catch_and_return_none,
    "CatchGeneric": detect_catch_generic,
    "DestructiveWrapping": detect_destructive_wrapping,
    "DummyHandler": detect_dummy_handler,
    "IncompleteImplementation": detect_incomplete_implementation,
    "LogAndReturnNone": detect_log_and_return_none,
    "LogAndThrow": detect_log_and_throw,
    "MultipleLineLog": detect_multiple_line_log,
    "NestedTryExceptionExample": detect_nested_try,
    "OverCatch": detect_over_catch,
    "OverCatchAndAbort": detect_over_catch_and_abort,
    "ThrowInsideFinally": detect_throw_inside_finally,
    "IgnoringInterruptedException": detect_ignoring_interrupted_exception
}

# -------------------------
# Analyzer functions
# -------------------------
def analyze_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        try:
            tree = ast.parse(f.read(), filename=filepath)
        except Exception:
            return {}
    results = defaultdict(lambda: {"count": 0, "lines": []})
    for node in ast.walk(tree):
        for name, detector in anti_pattern_detectors.items():
            if detector(node):
                results[name]["count"] += 1
                results[name]["lines"].append(getattr(node, 'lineno', 'unknown'))
    return results

def analyze_project(root_dir):
    project_report = {}
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                patterns = analyze_file(path)
                if patterns:
                    project_report[path] = patterns
    return project_report

# -------------------------
# Run analyzer and save JSON
# -------------------------
if __name__ == "__main__":
    project_path = "./example"  # replace with your project path
    report = analyze_project(project_path)
    
    # Print to console
    for file, patterns in report.items():
        print(f"\nFile: {file}")
        for pattern, info in patterns.items():
            print(f"  {pattern}: {info['count']} occurrences at lines {info['lines']}")
    
    # Save JSON report
    with open("anti_patterns_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
    
    print("\n✅ Analysis complete. Report saved as 'anti_patterns_report.json'")
