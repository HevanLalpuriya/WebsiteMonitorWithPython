"""
controller code reads the xml configuration file, monitors the websites and logs the resutls
"""

from ReadXMLFile import read_websitelist
from MonitorWebsite import access_url
import threading
from myLogger import mylog
from credentialManager import simplecheckcredential

# name of the configuration file to be read
fileName = "websiteList.xml"

def work():

    """ Reading configuration file """
    websitelist = read_websitelist(fileName)

    # timer according to sample rate
    threading.Timer(int(websitelist[0].sampleRate), work).start()

    # reading the data
    for i in range(len(websitelist)):

        finalResult = access_url(websitelist[i].url, websitelist[i].content)
        logmsg = "{:<80} ".format(str(websitelist[i].url)) \
                 + "{:<10} ".format(finalResult.responseCode) \
                 + "{:<50} ".format(finalResult.result) \
                 + "{0:10.2f}     ".format(finalResult.timeTaken) \
                 + "{:<40} ".format(str(websitelist[i].content))

        print str(logmsg)
        mylog("info", logmsg)
    print "- - - - - - - - - - - - - - - - "


def Start():
    # validating credentials
    if simplecheckcredential():
        work()


