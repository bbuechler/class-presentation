import os


def who():
    """
    Attempt to deduce user
    """

    return os.getenv('USER') or 'unknown'


def hello():
    """
    Greet User
    """

    user = who()
    print(f"Welcome to new {user}!")


if __name__ == '__main__':
    """
    Totally meaningful software
    """

    hello()
