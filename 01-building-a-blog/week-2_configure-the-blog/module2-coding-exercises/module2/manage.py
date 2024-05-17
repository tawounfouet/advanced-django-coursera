#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'module2.settings')
    os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")
    # this is to make our config reading tests pass
    if "test" in sys.argv:  # hack to detect if running tests
        os.environ["DJANGO_ALLOWED_HOSTS"] = "host1.example.com,host2.example.org"
    try:
        from configurations.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
