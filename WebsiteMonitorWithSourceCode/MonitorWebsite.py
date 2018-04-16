""" code to monitor websites """
import urllib2
import time


class MonitorResults:
    def __init__(self):
        timeStamp = None
        result = None
        timeTaken = None
        responseCode = None

# method to access the url and return the results
def access_url(urlname, content):
    mr = MonitorResults()
    initialTime = time.clock()
    try:
        response = urllib2.urlopen(str(urlname))
        TotalTime = time.clock() - initialTime
        if response.getcode() == 200:
            if validate_content(response, content):
                mr.result = "pass"
                mr.timeTaken = TotalTime
                mr.responseCode = "200"
            else:
                mr.result = "fail: content doesn't match : "
                mr.timeTaken = TotalTime
                mr.responseCode = "200"
        else:
            mr.result = "fail with " + response.getcode()
            mr.responseCode = response.getcode()
            mr.timeTaken = TotalTime
        return mr

    except urllib2.HTTPError, e:
        mr.timeTaken = time.clock() - initialTime
        mr.result = "Error: URL not accessible "
        mr.responseCode = str(e.getcode())
        pass

    except Exception as e:
        mr.timeTaken = time.clock() - initialTime
        mr.result = "something went wrong : {0}".format(str(e.message))
        mr.responseCode = " "
        pass

    return mr


# method to validate content
def validate_content(response, content):
    try:
        response_data = str(response.read())

        if response_data.index(str(content)) > 0:
            return True
        else:
            return False

    except:
        pass
    return False
