from src.utils.query_utils import get_query
from src.utils.time_utils import get_now_isoformat, get_time_days_before
from .helpers import make_github_call


def make_user_contribution_call(owner):
    time_yesterday = get_time_days_before(1)
    now = get_now_isoformat(True)
    query = get_query("user_contribution", owner, time_yesterday, now)
    response = make_github_call(query)
    return response.json()["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
