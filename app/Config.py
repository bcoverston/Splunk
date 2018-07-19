__author__ = 'eMaM'

DEVELOPMENT_CONF = {
    # 'splunk': {
    #     'username': 'admin',
    #     'password': 'qazxsw@1',
    #     'host':'127.0.0.1',
    #     'port': 8089,
    #     'scheme': 'https',
    #     'fields': ['_time', 'd_time', 'clientip', 'file', 'status', 'uri', 'user'],
    #     'backup': {
    #         'path': '~/splunk-bk/'
    #     },
    #     'report':'Data_For_Download_Analytics'
    # },

    'splunk': {
        'username': 'jega',
        'password': 'C@ssandra94010',
        'host':'datastax.splunkcloud.com',
        'port': 8089,
        'scheme': 'https',
        'fields': ['_time', 'd_time', 'clientip', 'file', 'status', 'uri', 'user'],
        'backup': {
            'path': '~/splunk-bk/'
        },
        'report':'Data_For_Download_Analytics',
        'download':{
            'daily_path':'',
            'full_path':''
        },
    },

    'salesforce': {
        'username': 'integration@datastax.com.neworg',
        'password': 'DatastaxAugust2016',
        'token': 'IWmfL7jMw6XzWOLbuR8efn2m',
        'backup': {
            'path': '/Users/mac/'
        },
        'download_path':'~/sf-download/',
        'fields':{
            'Account':'BillingLongitude|Revenue_Range__c|ParentId|Sales_Region__c|Website|Type|BillingCountryCode|DataStax_Pursuit_List__c|LastModifiedDate|type|BillingLatitude|Account_Subtype__c|BillingStateCode|Name|NumberOfEmployees|BillingCity|BillingPostalCode|Id|Global_2000__c|Industry',
            'Lead':'Email|LastModifiedDate|ConvertedAccountId|Existing_Account__c|Id|Type__c',
            'Contact':'Name|Email|AccountId|Id|type'
        }
    },
    'misc':{
        'splunk_search_date_format' : "%Y-%m-%dT%H:%M:%S.%f",
        'splunk_export_format' : "%Y%m%d",

    }
}
