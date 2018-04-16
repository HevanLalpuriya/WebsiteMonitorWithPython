# WebsiteMonitorWithPython
WebsiteMonitorWithPython
To execute the website monitoring program follow the below steps:
 
Pre-requisite: Install python 2.7
https://www.python.org/download/releases/2.7/ 

1. Extract the "WebsiteMonitor.zip" file
2. Configure websites list and SampleRate in "websiteList.xml" file.
3. In the command prompt reach to the directory where the Run.py exists.
4. Type "Python Run.py" and press Enter key
5. you will be asked for credentials : (username: abc, Password: abc) and press enter

you can see the results in Result folder.

This program has,

-> Used python version 2.7.12
-> Capability to Read the web pages and content from a configuration file
-> Configurable IntervalTime/samplingRate to which the requests would be sent to web server
-> Capability to validate the content returned from website
-> To give response time in seconds
-> Capability of writing  results in a saperate folder according to dates and new file is created each hour
   The result file contains the checked URL, status check, results, Response time and verified content
