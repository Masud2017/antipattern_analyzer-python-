from git import Repo
from datetime import datetime

def get_repo_metrics(repo_path: str) -> dict:
    repo = Repo(repo_path)
    commits = list(repo.iter_commits())

    total_added = 0
    total_deleted = 0

    for commit in commits:
        stats = commit.stats.total
        total_added += stats['insertions']
        total_deleted += stats['deletions']

    last_commit_date = commits[0].committed_datetime if commits else None

    metrics = {
        "total_commits": len(commits),
        "total_added": total_added,
        "total_deleted": total_deleted,
        "code_churn": total_added + total_deleted,
        "last_commit": last_commit_date.isoformat() if last_commit_date else None
    }

    return metrics


if __name__ == "__main__":
    path = "./example"  # change this to your repo path
    print(get_repo_metrics(path))
