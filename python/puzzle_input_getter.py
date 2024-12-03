"""
Either set ADVENT_OF_CODE_SESSION_COOKIE environment variable,
or create a file $HOME/.config/advent-of-code/session-cookie with your session cookie

You can get your session cookie by logging in and extracting the value from the stored cookie

NEVER SHARE THAT COOKIE, IT IS PERSONALIZED
"""

import functools
import os
import pathlib
from collections.abc import Callable

import requests

__session_cookie = None

__ENV_VAR = "ADVENT_OF_CODE_SESSION_COOKIE"

__COOKIEPATH = pathlib.Path.home() / ".config" / "advent-of-code/session-cookie"

__LOCALCOOKIE = pathlib.Path(__file__).parent / ".session-cookie"


if __ENV_VAR in os.environ:
    __session_cookie = os.environ[__ENV_VAR].strip()
elif __LOCALCOOKIE.exists():
    __session_cookie = __LOCALCOOKIE.read_text().strip()
elif __COOKIEPATH.exists():
    __session_cookie = __COOKIEPATH.read_text().strip()


def __cache_input(func) -> Callable[[int, int], str]:
    """Decorator that caches to the directory of the current script into .cache folder"""

    @functools.wraps(func)
    def wrapper(year: int, day: int) -> str:
        path = (
            pathlib.Path(__file__).parent
            / ".cache"
            / "advent-of-code"
            / f"{year}"
            / f"day{day:02}.input"
        )

        if path.exists():
            result = path.read_text()
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            result = func(year, day)
            path.write_text(result)
        return result

    return wrapper


@__cache_input
def __get_puzzle_input(year: int, day: int) -> str:
    if __session_cookie is None:
        raise ValueError(
            "Please set session cookie to download your input.\nEither set ADVENT_OF_CODE_SESSION_COOKIE environment variable,\nor create a file $HOME/.config/advent-of-code/session-cookie with your session cookie"
        )
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"Cookie": f"session={__session_cookie}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Error getting puzzle input: {response.status_code}")


def get_puzzle_input(year: int, day: int) -> str:
    """Gets the puzzle input for year and day using your session cookie.

    Args:
        year (int): year
        day (int): day
    Returns:
        str: puzzle input
    """
    return __get_puzzle_input(year, day)
