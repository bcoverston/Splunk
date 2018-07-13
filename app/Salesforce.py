from app import Config
from simple_salesforce import Salesforce

__author__ = 'eMaM'


class SalesforceIntergration():
    def __init__(self):
        self.sf = Salesforce(
            username=Config.DEVELOPMENT_CONF['salesforce']['username'],
            password=Config.DEVELOPMENT_CONF['salesforce']['password'],
            security_token=Config.DEVELOPMENT_CONF['salesforce']['token']
            # sandbox=True
        )

    def query_all_leads(self):
        tables = ['Lead', 'Contact', 'Account']
        # tables = ['lead']
        for each in tables:
            self.sf.query_all("select * from {}".format(each))



SalesforceIntergration().query_all_leads()