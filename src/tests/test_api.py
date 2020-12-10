import json
import unittest
from src.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_users(self):
        """Ensure the /sanity route behaves correctly."""
        response = self.client.get('/sanity')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('check!', data['message'])
        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
