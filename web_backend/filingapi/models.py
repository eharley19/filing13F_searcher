"""Create table models for database"""
import hashlib

from dataclasses import dataclass
from filingapi import db

@dataclass
class Infotable(db.Model):
    row_id: str
    accession_no: str
    cik_no: str
    nameOfIssuer: str
    titleOfClass: str

    """Define Infotable Table"""
    __tablename__ = 'infotable'
    row_id = db.Column(db.String, primary_key=True)
    accession_no = db.Column(db.String, db.ForeignKey('primary_doc.accession_no'))
    cik_no = db.Column(db.String)
    name_of_issuer = db.Column(db.String)
    title_of_class = db.Column(db.String)
    cusip = db.Column(db.String)
    value = db.Column(db.Numeric)
    ssh_prnamt = db.Column(db.Integer)
    ssh_prnamt_type = db.Column(db.String)
    put_call = db.Column(db.String)
    investment_discretion = db.Column(db.String)
    other_manager = db.Column(db.String)
    voting_authority_sole = db.Column(db.Integer)
    voting_authority_shared = db.Column(db.Integer)
    voting_authority_none = db.Column(db.Integer)

    def __repr__(self):
        return "<Infotable(accession_no='%s', cik_no='%s', nameOfIssuer='%s', " \
               "titleOfClass='%s', cusip='%s', value='%s', " \
               "sshPrnamt='%s', sshPrnamtType='%s', putCall='%s', " \
               "investmentDiscretion='%s', otherManager='%s', votingAuthority_Sole='%s', " \
               "votingAuthority_Shared='%s', votingAuthority_None='%s')>" % (
                   self.accession_no, self.cik_no, self.nameOfIssuer,
                   self.titleOfClass, self.cusip, self.value,
                   self.sshPrnamt, self.sshPrnamtType, self.putCall,
                   self.investmentDiscretion, self.otherManager, self.votingAuthority_Sole,
                   self.votingAuthority_Shared, self.votingAuthority_None)

    def create_primary_key(self):
        """Uses hash to generate Primary Key based on original row data for infotable table"""
        infotable_row_list = [self.accession_no,
                              self.cik_no,
                              self.nameOfIssuer,
                              self.titleOfClass,
                              self.titleOfClass,
                              self.cusip,
                              self.value,
                              self.sshPrnamt,
                              self.sshPrnamtType,
                              self.putCall,
                              self.investmentDiscretion,
                              self.otherManager,
                              self.votingAuthority_Sole,
                              self.votingAuthority_Shared,
                              self.votingAuthority_None
                              ]
        full_str = ''.join(str(cell) for cell in infotable_row_list)
        result = hashlib.md5(full_str.encode())
        return result.hexdigest()


@dataclass
class PrimaryDoc(db.Model):
    accession_no: str
    cik_no: str
    company_name: str
    filing_date: db.Date
    infotable_rows: Infotable

    """Define PrimaryDoc Table"""
    __tablename__ = 'primary_doc'
    accession_no = db.Column(db.String, primary_key=True)
    cik_no = db.Column(db.String)
    company_name = db.Column(db.String)
    filing_date = db.Column(db.Date)
    infotable_rows = db.relationship("Infotable")

    def __repr__(self):
        return "<PrimaryDoc(accession_no='%s', cik_no='%s', filing_date='%s', company_name='%s')>" % (
            self.accession_no, self.cik_no, self.filing_date, self.company_name)