"""
Either set ADVENT_OF_CODE_SESSION_COOKIE environment variable,
or create a file $HOME/.config/advent-of-code/session-cookie with your session cookie

You can get your session cookie by logging in and extracting the value from the stored cookie

NEVER SHARE THAT COOKIE, IT IS PERSONALIZED
"""

import functools
import itertools
import os
import pathlib
import tempfile
from collections.abc import Callable, Iterator

import requests

__session_cookie = None

__ENV_VAR = "ADVENT_OF_CODE_SESSION_COOKIE"

__COOKIEPATH = pathlib.Path.home() / ".config" / "advent-of-code/session-cookie"


if __ENV_VAR in os.environ:
    __session_cookie = os.environ[__ENV_VAR].strip()
elif __COOKIEPATH.exists():
    __session_cookie = __COOKIEPATH.read_text().strip()


def __cache_input_temp(func) -> Callable[[int, int], str]:
    @functools.wraps(func)
    def wrapper(year: int, day: int) -> str:
        tempdir = tempfile.gettempdir()
        path = pathlib.Path(tempdir) / "advent-of-code" / f"{year}_{day}"

        if path.exists():
            result = path.read_text()
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            result = func(year, day)
            path.write_text(result)
        return result

    return wrapper


@__cache_input_temp
def __get_puzzle_input(year=int, day=int) -> str:
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


def get_puzzle_input(year: int, day: int) -> list[str]:
    return __get_puzzle_input(year=year, day=day).splitlines()


def get_puzzle_input_tee(year: int, day: int) -> tuple[Iterator[str], ...]:
    return itertools.tee(get_puzzle_input(year=year, day=day), 2)
