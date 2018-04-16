""" Reading xml file """
from xml.dom import minidom
from os import path
from myLogger import mylog


class xmlcontent:
    def __init__(self):
        url = None
        id = None
        content = None
        sampleRate = None


def read_websitelist(fileName):
    if path.exists(fileName):
        doc = minidom.parse(fileName)
        IDs = doc.getElementsByTagName("ID")
        xmlcontent.sampleRate = doc.getElementsByTagName("sampleRate")[0].firstChild.data

        list_content = []

        try:
            for ID in IDs:
                c1 = xmlcontent()

                c1.id = ID.getAttribute("id")
                c1.url = ID.getElementsByTagName("URL")[0].firstChild.data
                c1.content = ID.getElementsByTagName("Content")[0].firstChild.data
                list_content.append(c1)
            return list_content
        except Exception as e:
            mylog("error", "Please check the xml config file. something went wrong.")
            raise IOError("something went wrong whie reading xml : {0}".format(str(e.message)))
            pass
    else:
        mylog("error", "File: " + fileName + " doesn't exist.")
        raise IOError("file doesn't exist")
