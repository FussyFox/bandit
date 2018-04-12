"""Lambda function that executes bandit, a static file linter."""
import logging
import sys

from lintipy import Handler

root_logger = logging.getLogger('')
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(logging.StreamHandler(sys.stdout))


def handle(*args, **kwargs):
    """Handle that is invoked by AWS lambda."""
    Handler('bandit', 'bandit', '-r', '.')(*args, **kwargs)
