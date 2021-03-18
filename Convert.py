def makeSingleString(bigList):
    retData = ""
    separator = "$$$$$$$$$$$$$$$$$$$$$$$$$"
    for listEle in bigList:
        msg = str(listEle)
        msg = msg + separator
        msg = msg[0:42]
        retData = retData + msg
    return retData

def makeListFromString(longString):
    retData = []
    data = longString.split('$')
    for item in data:
        if len(item) > 0:
            retData.append(int(item))
    return retData

def DictToString(signature,data):
    string = "P:"+str(signature[0])+":Q:"+str(signature[1])+":Data:"+data
    return string

def StringToDict(str):
    retData = []
    data = str.split(':')
    for item in data:
        if len(item) > 0:
            retData.append(item)

    dict = {
        retData[0]: retData[1],
        retData[2]: retData[3],
        retData[4]: retData[5]
    }
    return dict