from copy import deepcopy
import json
from shutil import ReadError
import sys
import getopt
import os
import glob

def getToken():
    with open("./secret.json", "r", encoding="utf-8") as jsonFile:
        file = json.load(jsonFile)
        return file["dc-token"]

def getWorklogPath():
    with open("./secret.json", "r", encoding="utf-8") as jsonFile:
        file = json.load(jsonFile)
        return file["worklog-path"]

def getWorklog():
    txtfiles = []
    for file in glob.glob(getWorklogPath() + "\\*.json"):
        txtfiles.append(file)
    return txtfiles
    