"""
auto_tts.py: cron job that allows pdfs to stay updated routinely. It uses the tts.py class
            TimetableScraper to allow such routine values. New values are inserted in a .txt
"""
from tts2 import TimetableScraper
import sys

"""
TimetableAutomator is a scraper that automates the process, rather than making the user
                download the pdf and do it themselves. This is done by using cron jobs
                and beautifulSoup/requests to grab the pdf from uwindsor's sites
"""
class TimetableAutomator(TimetableScraper):
    def __init__(self, filename=None):
        super().__init__(filename)

    """
        auto_routine: cron job runs this. This is the underlying routine that makes everything automated. 
                      It performs requests and uses beautifulsoup to get pdf data, parses the new pdfs and 
                      updates all related json. Saves log files. 
    """
    def auto_routine(self):
        # first of all, update pdf's to latest version using checkdate.py
        from helper import checkdate

        # then scrape data. The sequence is laid out in def scrape()
        self.scrape()
    
    def scrape(self):
        pass


if __name__ == "__main__":
    import os
    tts = TimetableAutomator(sys.argv[1:])
    tts.auto_routine()
    print(tts)