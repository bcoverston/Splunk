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
        'password': 'datastax2',
        'token': 'UXgOITuTQiwePYBwnnWo5QEpp',
        'backup': {
            'path': '~/sf-bk/'
        },
        'download_path':'~/sf-download/'
    },
    'misc':{
        'splunk_search_date_format' : "%Y-%m-%dT%H:%M:%S.%f",
        'splunk_export_format' : "%Y%m%d",

    }
}
