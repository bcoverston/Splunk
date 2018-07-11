from app import Config

__author__ = 'eMaM'

from time import sleep

import sys

from app.Utils import formateDate, startDate, endDate

import splunklib.client as client


class SplunkSearch():
    def __init__(self):

        self.service = client.connect(
                    host=Config.DEVELOPMENT_CONF['splunk']['host'],
                    port=Config.DEVELOPMENT_CONF['splunk']['port'],
                    username=Config.DEVELOPMENT_CONF['splunk']['username'],
                    password=Config.DEVELOPMENT_CONF['splunk']['password'],
                    scheme=Config.DEVELOPMENT_CONF['splunk']['scheme'])


    def search(self):


        savedsearches = self.service.saved_searches[Config.DEVELOPMENT_CONF['splunk']['report']]
        kwargs = {
            "auto_summarize.dispatch.earliest_time": formateDate(startDate(), Config.DEVELOPMENT_CONF['misc']['splunk_search_date_format']),
            "auto_summarize.dispatch.latest_time": formateDate(endDate(), Config.DEVELOPMENT_CONF['misc']['splunk_search_date_format'])
        }


        savedsearches.update(**kwargs).refresh()

        # Run the saved search
        job = savedsearches.dispatch()

        sleep(10)

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


        search_results = job.results(**{"output_mode": "csv"})

        f = open("~/NewFile.csv", 'w')
        f.write(search_results.read())



SplunkSearch().search()


# curl -k https://prd-p-5p7k7lg9772d.cloud.splunk.com:8089/services/auth/login --data-urlencode username=emam151987 --data-urlencode password=Qazxsw#1
