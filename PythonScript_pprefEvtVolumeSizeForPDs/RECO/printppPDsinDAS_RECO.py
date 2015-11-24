#!/usr/bin/env python
#
# modified Script to print information about the pp Reference Run PDs in DAS in table format
#
 
from datetime import datetime
import os
from prettytable import PrettyTable

Dir = "/afs/cern.ch/user/h/honi/CMSSW_7_5_5_patch3/src/PythonScript_pprefEvtVolumeSizeForPDs/RECO"
 
pdNames = ["HIMinimumBias1"]
pdNames.append("L1MinimumBias")
pdNames.append("EmptyBX")
pdNames.append("HighPtLowerJets")
pdNames.append("HighPtJet80")
pdNames.append("HighPtLowerPhotons")
pdNames.append("HighPtPhoton30AndZ")
pdNames.append("HIOniaTnP")
pdNames.append("HIEWQExo")
pdNames.append("HIOnia")
pdNames.append("FullTrack")
pdNames.append("HighMultiplicity")
pdNames.append("ppForward")
pdNames.append("HeavyFlavor")
pdNames.append("HIHardProbes")

pdNum = len(pdNames)
x = PrettyTable(["PD Names","Number of Events(K)","File Size(GB)","average Event Size(MB)"])
x.align["PD Name"] = "l"
x.padding_width = 1
x.float_format = .3;

now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print "\n RECO statistics for Run2015E-PromptReco-v1 datasets in DAS at", mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss, "(Geneva time)"
print ""
 
totalRECOSize = 0
totalRECOEvents = 0
for pdName in pdNames:
    dasRECOPathName = '/' + pdName + '/Run2015E-PromptReco-v1/RECO'
    findEventsRECOCommand = Dir + '/das.py --limit=1000 --format=plain --query="dataset dataset=' + dasRECOPathName + ' | grep dataset.nevents" > tmp.txt ; tail -1 tmp.txt > events.txt'
    os.system(findEventsRECOCommand)
    fileInput = open('events.txt', 'r')
    thisEvents = 0
    RECOEventSize = 0
    for line in fileInput:
        nEvents = line.rstrip('\n')
        if(nEvents != '[]'):
            nEventsM = int(nEvents)/1.0e3 
            thisEvents = int(nEvents)
        else:
            nEvents = 0
            nEventsM = 0
        totalRECOEvents += thisEvents
    fileInput.close()
 
    findSizeRECOCommand = Dir + '/das.py --limit=1000 --format=plain --query="dataset dataset=' + dasRECOPathName + ' | grep dataset.size" > tmp.txt ; tail -1 tmp.txt > size.txt'
    os.system(findSizeRECOCommand)
    fileInput = open('size.txt', 'r')
    for line in fileInput:
        RECOFileSize = line.rstrip('\n')
        if(RECOFileSize == '[]'):
              RECOFileSizeGB = 0
        else:
              RECOFileSizeGB = int(RECOFileSize)/1.0e9
              if(thisEvents > 0):
                   RECOEventSize = RECOFileSizeGB*1.0e3/thisEvents
        totalRECOSize += RECOFileSizeGB
    fileInput.close()

    x.add_row([pdName,nEventsM,RECOFileSizeGB,RECOEventSize])
print x

averageEventSize = totalRECOSize*1.0e3/totalRECOEvents
print "\n RECO File Summary:"
print " Total Size = ", 
print "%0.1f %s" % (totalRECOSize, "GB")
print " Event Number = ", totalRECOEvents, "events"
print " Average Event Size = ", 
print "%0.3f %s" % (averageEventSize, "MB/event")
exit()
