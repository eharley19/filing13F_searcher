# pylint: disable=too-few-public-methods
"""This file contains tests for the class Parser"""
import re
from xml.etree import ElementTree

from edgar_filing_searcher.models import Company, EdgarFiling
from edgar_filing_searcher.parsers.crawler_current_events import get_text
from edgar_filing_searcher.parsers.data_13f import data_13f_row
from edgar_filing_searcher.parsers.errors import CantFindUrlException
import pytest


def test__parse_sec_accession_no():
    assert False


def test__parse_primary_doc_xml_and_infotable_xml_urls():
    assert False


def test__parse_primary_doc_xml_url():
    assert False


def test__parse_infotable_xml_url():
    assert False


def test__parse_primary_doc_root():
    assert False


def test__parse_primary_doc_cik():
    assert False


def test__parse_primary_doc_company_name():
    assert False


def test__parse_primary_doc_accepted_filing_date():
    assert False


def test__parse():
    assert False
