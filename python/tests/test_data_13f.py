# pylint: disable=redefined-outer-name
"""This file contains tests for data_13f"""
from edgar_filing_searcher.parsers.data_13f import data_13f_row, parse_infotable_doc_root, \
    parse_xml_text
import pytest


@pytest.fixture
def infotable_xml():
    """"""
    return ['/Archives/edgar/data/1506796/000090901221000060/primary_doc.xml',
     '/Archives/edgar/data/1506796/000090901221000060/aci_13f.xml']


@pytest.fixture
def current_events_text():
    """"""
    with open("tests/fixtures/edgar_current_events.html", "rt") as file:
        return file.read()


def test_parse_infotable_doc_root():
    assert parse_infotable_doc_root(infotable_xml) == '0000909012-21-000060'


def test_parse_xml_text():
    assert parse_xml_text(filing_detail_text) == '0000909012-21-000060'


def test_data_13f_row():
    assert data_13f_row(filing_detail_text) == '0000909012-21-000060'
