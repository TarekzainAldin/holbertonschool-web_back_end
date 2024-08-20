#!/usr/bin/python3
"""contatnte the function index"""


def index_range(page, page_size):
    """"return tuble for the tow args """

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
