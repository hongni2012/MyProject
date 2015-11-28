#!/usr/bin/env python
#
# modified Script to print information about the pp Reference Run PDs in DAS in table format
#
 
from datetime import datetime
import os
from prettytable import PrettyTable
from prettytable import ALL

Dir = "/afs/cern.ch/user/h/honi/CMSSW_7_5_5_patch3/src/PythonScript_pprefEvtVolumeSizeForPDs/RAW"

pdNames = ["MinimumBias1"]
pdNames.append("MinimumBias16")
pdNames.append("ppForward")
pdNames.append("HighMultiplicity")
pdNames.append("FullTrack")
pdNames.append("BTagCSV")
pdNames.append("HeavyFlavor")
pdNames.append("JetHT")
pdNames.append("HighPtJet80")
pdNames.append("HighPtLowerJets")
pdNames.append("DoubleMu")
pdNames.append("MuPlusX")
pdNames.append("SingleMuHighPt")
pdNames.append("SingleMuLowPt")

pdNum = len(pdNames)
x = PrettyTable(["PDs","File Size(GB)","Max File(GB)","#Evts(K)","#Lumis","avg. Evt Size(MB)","avg. Lumi Size (GB)"])
x.align["PD Name"] = "l"
x.padding_width = 1
x.float_format = .3;
x.hrules = ALL

now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print "\n RAW statistics for Run2015E-v1 datasets in DAS at", mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss, "(Geneva time)"
 
totalRAWSize = 0
totalRAWEvents = 0
totalLumis = 0
MaxFileSize = 0

for pdName in pdNames:
    dasRAWPathName = '/' + pdName + '/Run2015E-v1/RAW'
    findEventsRAWCommand = Dir + '/das.py --limit=1000 --format=plain --query="dataset dataset=' + dasRAWPathName + ' | grep dataset.nevents" > tmp.txt ; tail -1 tmp.txt > events.txt'
    os.system(findEventsRAWCommand)
    fileInput = open('events.txt', 'r')
    thisEvents = 0
    RAWEventSize = 0
    for line in fileInput:
        nEvents = line.rstrip('\n')
        if(nEvents != '[]'):
            nEventsK = int(nEvents)/1.0e3 
            thisEvents = int(nEvents)
        else:
            nEvents = 0
            nEventsK = 0
        totalRAWEvents += thisEvents
    fileInput.close()
 
    findSizeRAWCommand = Dir + '/das.py --limit=1000 --format=plain --query="dataset dataset=' + dasRAWPathName + ' | grep dataset.size" > tmp.txt ; tail -1 tmp.txt > size.txt'
    os.system(findSizeRAWCommand)
    fileInput = open('size.txt', 'r')
    for line in fileInput:
        RAWFileSize = line.rstrip('\n')
        if(RAWFileSize == '[]'):
            RAWFileSizeGB = 0
        else:
            RAWFileSizeGB = int(RAWFileSize)/1.0e9
            if(thisEvents > 0):
               RAWEventSize = RAWFileSizeGB*1.0e3/thisEvents
        totalRAWSize += RAWFileSizeGB
    fileInput.close()

    countLumiRAWCommand = Dir + '/das.py --limit=1000 --format=plain --query="run,lumi dataset=' + dasRAWPathName + ' | count(lumi)" > tmp.txt ; tail -1 tmp.txt > lumicounts.txt'
    os.system(countLumiRAWCommand)
    fileInput = open('lumicounts.txt','r')
    thisLumis = 0
    for line in fileInput:
        nLumis = line.strip('count(lumi)=N/A')
        if(nLumis != '[]'):
            thisLumis = int(nLumis)
        else:
            nLumis = 0
        totalLumis += thisLumis

    if(thisLumis == 0):
        FileSizePerLumi = 0
    else:
        FileSizePerLumi = RAWFileSizeGB/thisLumis
    fileInput.close()

    findMaxFileRAWCommand = Dir + '/das.py --limit=1000 --format=plain --query="file dataset=' + dasRAWPathName + ' | max(file.size)" > tmp.txt ; tail -1 tmp.txt > maxfilesize.txt'
    os.system(findMaxFileRAWCommand)
    fileInput = open('maxfilesize.txt','r')
    thisMaxSize = 0
    for line in fileInput:
        maxsize = line.strip('max(file.size)=')
        if(maxsize != '[]'):    
            thisMaxSize = int(maxsize)/1.0e9
    fileInput.close()
   
    x.add_row([pdName,int(RAWFileSizeGB),thisMaxSize,int(nEventsK),thisLumis,RAWEventSize,FileSizePerLumi])
   
    if(MaxFileSize < thisMaxSize):
        MaxFileSize = thisMaxSize

averageEventSize = totalRAWSize*1.0e3/totalRAWEvents
if(totalLumis != 0):
    averageFileSizePerLumi = totalRAWSize/totalLumis
else:
    averageFileSizePerLumi = 0

x.add_row(['RAW',int(totalRAWSize),MaxFileSize,int(totalRAWEvents/1.0e3),totalLumis,averageEventSize,averageFileSizePerLumi]) 
print x

print "\n RAW File Summary:"
print " Total Size = ", 
print "%0.1f %s" % (totalRAWSize, "GB")
print " Event Number = ", totalRAWEvents, "events"
print " avg. Event Size = ", 
print "%0.3f %s" % (averageEventSize, "MB/event")
print " Lumi Number = ", totalLumis, "Lumis"
print " avg. Lumi Size = ",
print "%0.3f %s" % (averageFileSizePerLumi, "GB/Lumi")
print "\n"

exit()
