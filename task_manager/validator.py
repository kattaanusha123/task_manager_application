# validator.py

import re


def validate_name(name):
    return bool(re.match(r"^[A-Za-z0-9 ]+$", name))


def validate_priority(priority):
    return priority.lower() in ["high", "medium", "low"]
