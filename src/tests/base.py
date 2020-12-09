from flask_testing import TestCase
from src import app


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('src.config.TestingConfig')
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass
