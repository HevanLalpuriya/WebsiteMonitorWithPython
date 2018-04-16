""" Logger file """
import logging
import datetime
import os

def mylog(loglevel, msg):
    currentPath = str(os.getcwd())
    myPath = "Results\\Results_{:%Y%m%d%H}".format(datetime.datetime.now())
    if os.path.isdir(myPath) == False:
        os.makedirs(myPath)
    os.chdir(myPath)

    MyLogFile = "{:%Y%m%d%H}".format(datetime.datetime.now()) + "logMonitor.log"
    logging.basicConfig(filename=MyLogFile, level=logging.INFO)
    msg = " {:%Y-%m-%d %H:%M:%S}  ".format(datetime.datetime.now()) + str(msg)
    if loglevel == "error":
        logging.error(msg)
    else:
        logging.info(msg)
    os.chdir(currentPath)