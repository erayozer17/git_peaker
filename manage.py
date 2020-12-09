from flask.cli import FlaskGroup
from src import app
import unittest
import coverage


COV = coverage.coverage(
    branch=True,
    include='src/*',
    omit=[
        'src/tests/*',
        'src/config.py',
    ]
)
COV.start()

cli = FlaskGroup(app)


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('src/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


if __name__ == '__main__':
    cli()
