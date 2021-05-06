# pylint: disable=import-error
"""This file contains the main method"""
from edgar_filing_searcher.parsers.main import create_url_list, send_data_to_db, main
import pytest


@pytest.fixture
def current_events_text():
    """This function creates an fixture with test edgar_current_events html data"""
    with open("fixtures/edgar_current_events.html", "rt") as file:
        return file.read()


def test_create_url_list(current_events_text):
    assert False


def test_send_data_to_db():
    assert False


def test_main():
    assert False
