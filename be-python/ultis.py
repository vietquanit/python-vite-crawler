import os
import os.path
import json

fileName = 'data.json'

def createFileJsonData():
    dictionary = {}
    json_object = json.dumps(dictionary, indent=4)
    if (os.path.isfile('')): #if file exists clear content
        open(fileName, 'w').close()
    else:
        open(fileName, 'w+').close()

def checkFolderAndCreateNew(dictionary):
    if (os.path.isdir(dictionary)): #if folder exists clear content
        print('exists')
    else:
        os.mkdir(dictionary)
# def writeDataToFile(data):
#     json_object = json.dumps(data, indent=4)
#     with open(fileName, 'w') as outfile:
#         outfile.write(json_object)