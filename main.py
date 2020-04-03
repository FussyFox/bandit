"""Lambda function that executes bandit, a static file linter."""
from lintipy import CheckRun


handle = CheckRun.as_handler(
    'bandit',
    'bandit.cli.main', '-r', '.'
)
