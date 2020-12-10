from src.utils.query_utils import get_query, build_after_param
from src.utils.time_utils import get_time_days_before
from .helpers import make_github_call


def get_repo_owner(repo):
    query = get_query("repo_search", repo, "")
    init_res = make_github_call(query)
    if "errors" in init_res:
        return False
    init_res = init_res["data"]["search"]
    results = init_res["edges"]
    has_next = init_res["pageInfo"]["hasNextPage"]
    next_cursor = init_res["pageInfo"]["endCursor"]
    while has_next:
        next_res = make_github_call(repo, build_after_param(next_cursor))
        next_res = next_res["data"]["search"]
        results += next_res["edges"]
        has_next = next_res["pageInfo"]["hasNextPage"]
        next_cursor = next_res["pageInfo"]["endCursor"]
    repo_username_count = {}
    for result in results:
        if result['node']['name'] in repo_username_count:
            return False
        if result['node']['name'] == repo:
            repo_username_count[repo] = result['node']['owner']['login']

    return repo_username_count[repo] if len(repo_username_count) == 1 else False


def get_repo_commits(repo):
    owner = get_repo_owner(repo)
    if not owner:
        return False
    last_week = get_time_days_before(7)
    query = get_query("repo_activity", owner, repo, last_week)
    commits = make_github_call(query)
    return commits["data"]["repository"]["object"]["history"]["nodes"]


def get_total_changes_on_commits(repo):
    total = 0
    commits = get_repo_commits(repo)
    if not commits and type(commits) != list:
        return False
    for commit in commits:
        total += commit["additions"]
        total -= commit["deletions"]
    return total
