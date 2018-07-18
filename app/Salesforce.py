import csv
import os

from simple_salesforce import SalesforceMalformedRequest
from simple_salesforce.exceptions import SalesforceError, SalesforceAuthenticationFailed

from app import Config
from simple_salesforce import Salesforce

from app.Utils import formateDate, startDate

__author__ = 'eMaM'


class SalesforceIntergration():
    def __init__(self):

        self.filename_pattern = Config.DEVELOPMENT_CONF['misc']['splunk_export_format']
        self.retry = 3
        self.sf = self.connect()

    def connect(self):
        try:
            sf = Salesforce(
                username=Config.DEVELOPMENT_CONF['salesforce']['username'],
                password=Config.DEVELOPMENT_CONF['salesforce']['password'],
                security_token=Config.DEVELOPMENT_CONF['salesforce']['token']
            )
        except Exception as e:
            if self.retry != 0:
                self.retry -= 1
                self.connect()
            else:
                raise SalesforceAuthenticationFailed("500",'Can`t connect to saleforce')

        return sf

    def query_all_leads(self):
        tables = ['Lead', 'Contact', 'Account']
        # tables = ['lead']
        for each in tables:
            salesforce_object = self.sf.__getattr__(each)
            fieldNames = [field['name'] for field in salesforce_object.describe()['fields']]
            try:
                results = self.sf.query_all(
                    "SELECT {} FROM {} WHERE CreatedDate={}".format(','.join(fieldNames), each, 'LAST_MONTH'))['records']
            except SalesforceMalformedRequest as e:
                continue

            outputfile = os.path.join(Config.DEVELOPMENT_CONF['salesforce']['backup']['path'],
                                      each + formateDate(startDate(), self.filename_pattern) + '.csv')
            with open(outputfile, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldNames, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
                writer.writeheader()
                for row in results:
                    try:
                        # each row has a strange attributes key we don't want
                        row.pop('attributes', None)
                        writer.writerow(row)
                    except:
                        continue


SalesforceIntergration().query_all_leads()
