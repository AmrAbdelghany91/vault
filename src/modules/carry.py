"""
    See https://stackoverflow.com/questions/3338283/python-sharing-global-variables-between-modules-and-classes-therein/3338357#3338357
    Use  a mutable list to share instances of the same class across multiple modules
"""

global_scope = [
    None  # Placeholder for Encryption instance
]
