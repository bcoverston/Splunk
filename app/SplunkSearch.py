__author__ = 'eMaM'

from time import sleep

import sys

#from app import Config
#from app.Utils import formateDate, startDate, endDate

import Config
from Utils import formateDate, startDate, endDate

import splunklib.client as client


class SplunkSearch():
    def __init__(self):
        self.service = client.connect(
            host=Config.DEVELOPMENT_CONF['splunk']['host'],
            port=Config.DEVELOPMENT_CONF['splunk']['port'],
            username=Config.DEVELOPMENT_CONF['splunk']['username'],
            password=Config.DEVELOPMENT_CONF['splunk']['password'])

    def search(self):
        savedsearches = self.service.saved_searches[Config.DEVELOPMENT_CONF['splunk']['Data_For_Download_Analytics']]
        kwargs = {
            "earliest_time": formateDate(startDate(), Config.DEVELOPMENT_CONF['misc']['splunk_search_date_format']),
            "latest_time": formateDate(endDate(), Config.DEVELOPMENT_CONF['misc']['splunk_search_date_format'])
        }

        savedsearches.update(**kwargs).refresh()

        # Run the saved search
        job = savedsearches.dispatch()

        sleep(500)

        while True:
            job.refresh()
            stats = {"isDone": job["isDone"],
                     "doneProgress": float(job["doneProgress"])*100,
                     "scanCount": int(job["scanCount"]),
                     "eventCount": int(job["eventCount"]),
                     "resultCount": int(job["resultCount"])}
            status = ("\r%(doneProgress)03.1f%%   %(scanCount)d scanned   "
                      "%(eventCount)d matched   %(resultCount)d results") % stats

            sys.stdout.write(status)
            sys.stdout.flush()
            if stats["isDone"] == "1":
                break
            sleep(2)

        jobresults = job.results()

        #TODO make result to csv


