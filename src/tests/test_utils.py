from freezegun import freeze_time
import unittest
from src.tests.base import BaseTestCase
from src.utils.time_utils import get_now_isoformat, get_time_days_before, sanitize_isoformat_time
from src.utils.query_utils import get_query, build_after_param


class TestTimeUtils(BaseTestCase):
    """Tests for the time utils."""

    @freeze_time("2012-01-14 12:00:01")
    def test_return_now_correctly_not_sanitized(self):
        """Ensure it returns now in isofromat correctly."""
        now = get_now_isoformat()
        expected = "2012-01-14T12:00:01"
        assert now == expected

    @freeze_time("2012-01-14 12:00:01")
    def test_return_now_correctly_sanitized(self):
        """Ensure it returns now sanitized in isofromat correctly."""
        now = get_now_isoformat(True)
        expected = "2012-01-14T12:00:01Z"
        assert now == expected

    @freeze_time("2012-01-14 12:00:01")
    def test_return_correct_time_get_time_days_before(self):
        """Ensure it returns date before n days from now in isofromat correctly."""
        result = get_time_days_before(3)
        assert result == "2012-01-11T12:00:01Z"

    def test_return_correct_time_sanitized(self):
        """Ensure it sanitizes time in isofromat correctly."""
        result = sanitize_isoformat_time("2012-01-11T12:00:01.08457")
        assert result == "2012-01-11T12:00:01Z"


class TestQueryUtils(BaseTestCase):
    """Tests for the query utils."""

    def test_repo_activity_query_built_correctly(self):
        """Ensure it builds repo_activity query correctly."""
        owner = "erayozer17"
        name = "example_repo"
        since = "2012-01-11T12:00:01Z"
        query = """query {
    repository(owner: "%s", name: "%s") {
      object(expression: "master") {
        ... on Commit {
          history(since: "%s") {
            nodes {
              committedDate
              additions
              deletions
            }
          }
        }
      }
    }
  }
""" % (owner, name, since)
        built_query = get_query("repo_activity", owner, name, since)
        assert query == built_query

    def test_build_after_param(self):
        """Ensure it builds after parameter correctly for repo_search query."""
        next_cursor = "123asdzxc"
        expected = ', after: "123asdzxc"'
        assert build_after_param(next_cursor) == expected

    def test_repo_search_query_built_correctly(self):
        """Ensure it builds repo_search query correctly."""
        repo_name = "example_repo"
        query = """{
search(query: "is:public %s", type: REPOSITORY, first: 100%s) {
    edges {
      node {
        ... on Repository {
          name
          owner{
            login
          }
        }
      }
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}
""" % (repo_name, "")
        built_query = get_query("repo_search", repo_name, "")
        assert query == built_query

    def test_repo_user_contribution_built_correctly(self):
        """Ensure it builds user_contribution query correctly."""
        owner = "example_owner"
        from_date = "2012-01-11T12:00:01Z"
        to_date = "2012-01-12T12:00:01Z"
        query = """query {
    user(login: "%s") {
        contributionsCollection(from: "%s", to: "%s") {
            contributionCalendar {
                totalContributions
            }
        }
    }
}
""" % (owner, from_date, to_date)
        built_query = get_query("user_contribution", owner, from_date, to_date)
        assert query == built_query


if __name__ == '__main__':
    unittest.main()
