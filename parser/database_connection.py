from sqlalchemy import create_engine, Column, Integer, String, Numeric
import os
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(os.environ.get('DB_CONNECTION_STRING'), echo=True)
Base = declarative_base()


class Infotable(Base):
    __tablename__ = 'infotable'
    id = Column(Integer, primary_key=True)
    accession_no = Column(String(50))
    cik = Column(String(50))
    nameOfIssuer = Column(String(50))
    titleOfClass = Column(String(50))
    cusip = Column(String(50))
    value = Column(Numeric)
    sshPrnamt = Column(Integer)
    sshPrnamtType = Column(String(50))
    putCall = Column(String(50))
    investmentDiscretion = Column(String(50))
    otherManager = Column(String(50))
    votingAuthority_Sole = Column(Integer)
    votingAuthority_Shared = Column(Integer)
    votingAuthority_None = Column(Integer)

    def __repr__(self):
        return "<User(accession_no='%i', cik='%s', nameOfIssuer='%s', " \
               "titleOfClass='%s', cusip='%s', value='%s', " \
               "sshPrnamt='%i', sshPrnamtType='%i', putCall='%i', " \
               "investmentDiscretion='%i', otherManager='%i', votingAuthority_Sole='%i', " \
               "votingAuthority_Shared='%i', votingAuthority_None='%i')>" % (
                   self.accession_no, self.cik, self.nameOfIssuer,
                   self.titleOfClass, self.cusip, self.value,
                   self.sshPrnamt, self.sshPrnamtType, self.putCall,
                   self.investmentDiscretion, self.otherManager, self.votingAuthority_Sole,
                   self.votingAuthority_Shared, self.votingAuthority_None)


class Primary_doc(Base):
    __tablename__ = 'primary_doc'
    id = Column(Integer, primary_key=True)
    cik = Column(String(50))
    filing_date = Column(String(50))
    company_name = Column(String(50))

    def __repr__(self):
        return "<User(cik='%s', filing_date='%s', company_name='%s')>" % (
            self.cik, self.filing_date, self.company_name)


Base.metadata.create_all(engine)


def insert_in_infotable_table(engine, df):
    df.to_sql('infotable_test3', engine)


def insert_in_primary_table(engine, df):
    engine.execute("INSERT INTO primary_doc_test1 (cik, cik)"
                   "VALUES (3, 'susan'), "
                   "ON CONFLICT (cik) DO NOTHING;"
                   )


def update_database(engine):
    engine.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")