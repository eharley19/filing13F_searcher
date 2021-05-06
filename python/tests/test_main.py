# pylint: disable=import-error
"""This file contains the main method"""
from edgar_filing_searcher.database import db
from edgar_filing_searcher.parsers.crawler_current_events import get_text, \
    parse_13f_filing_detail_urls
from edgar_filing_searcher.parsers.parser_class import Parser
from edgar_filing_searcher.parsers.setup_db_connection import setup_db_connection


def test_create_url_list():
    assert False


def test_send_data_to_db():
    assert False


def test_main():
    assert False
