from app import Config

__author__ = 'eMaM'


class Salesforce():
    def __init__(self):
        self.sf = Salesforce(
            username=Config.DEVELOPMENT_CONF['salesforce']['username'],
            password=Config.DEVELOPMENT_CONF['salesforce']['password'],
            security_token=Config.DEVELOPMENT_CONF['salesforce']['token']
            # sandbox=True
        )





