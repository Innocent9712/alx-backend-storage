#!/usr/bin/env python3
"""5. Implementing an expiring web cache and tracker"""
import requests
from typing import Callable
import redis


def counter(func: Callable) -> Callable:
    """Counts and stores the number of times a url is visited
    caches the count for 10secs"""
    def wrapper(url: str) -> Callable:
        newConn = redis.Redis()
        newConn.incrby(f"count:{url}", amount=1)
        newConn.expire(f"count:{url}", 10)
        return func(url)
    return wrapper


@counter
def get_page(url: str) -> str:
    """In this tasks, we will implement a get_page function
    The core of the function is very simple.
    It uses the requests module to obtain the HTML content of
    a particular URL and returns it."""
    return requests.get(url).content


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
