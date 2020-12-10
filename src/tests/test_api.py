import json
import unittest
from src.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_sanity(self):
        """Ensure the /sanity route behaves correctly."""
        response = self.client.get('/sanity')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('check!', data['message'])
        self.assertIn('success', data['status'])

    def test_active(self):
        """Ensure the /active/<user> route behaves correctly."""
        response = self.client.get('/active/erayozer17')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('is_active_since_yesterday', data)
        assert isinstance(data['is_active_since_yesterday'], bool)

    def test_downwards(self):
        """Ensure the /downwards/<repo> route behaves correctly."""
        response = self.client.get('/downwards/git_peaker')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('is_repo_downwarded_since_last_week', data)
        assert isinstance(data['is_repo_downwarded_since_last_week'], bool)

    def test_active_not_found(self):
        """Ensure the /active/<user> route behaves correctly when not found."""
        user = "hubduhvhdbfuvdfbvudfbvufvyb"
        response = self.client.get(f'/active/{user}')
        data = json.loads(response.data.decode())
        self.assertIn('message', data)
        self.assertEqual(response.status_code, 400)
        assert f"{user} not found." == data['message']

    def test_downwards_not_found(self):
        """Ensure the /downwards/<repo> route behaves correctly when not found."""
        repo = "hubduhvhdbfuvdfbvudfbvufvyb"
        response = self.client.get(f'/downwards/{repo}')
        data = json.loads(response.data.decode())
        self.assertIn('message', data)
        self.assertEqual(response.status_code, 400)
        assert f"{repo} is not unique or not found." == data['message']


if __name__ == '__main__':
    unittest.main()
