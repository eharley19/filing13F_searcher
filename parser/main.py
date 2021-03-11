from crawler_edgar_current_events import grab_text
from crawler_edgar_current_events import get_13f_filing_detail_urls
from crawler_edgar_current_events import get_primary_doc_and_infotable_urls
from crawler_edgar_current_events import get_primary_doc_xml_url
from crawler_edgar_current_events import get_infotable_xml_url
from parser_13f_primary_doc_xml import grab_primary_doc_root
from parser_13f_primary_doc_xml import grab_primary_doc_cik
from parser_13f_primary_doc_xml import grab_primary_doc_company_name
from parser_13f_infotable_xml import grab_infotable


def main():
    url_edgar_current_events = 'https://www.sec.gov/cgi-bin/current?q1=0&q2=6&q3=13F'
    text_edgar_current_events = grab_text(url_edgar_current_events)
    filing_detail_urls = get_13f_filing_detail_urls(text_edgar_current_events)
    for filing_detail_url in filing_detail_urls:
        filing_detail_text = grab_text(filing_detail_url)
        xml_links = get_primary_doc_and_infotable_urls(filing_detail_text)
        primary_doc_xml_url = get_primary_doc_xml_url(xml_links)
        infotable_xml_url = get_infotable_xml_url(xml_links)

        root = grab_primary_doc_root(primary_doc_xml_url)
        cik = grab_primary_doc_cik(root)
        company_name = grab_primary_doc_company_name(root)
        print(cik, company_name)

        df = grab_infotable(infotable_xml_url)
        df.insert(loc=0, column='id', value=cik)
        print(df.head())
        #TODO: send to sql alchemy


if __name__ == "__main__":
    main()

# print("check")
