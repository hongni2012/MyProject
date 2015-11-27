#!/usr/bin/env python
#
# modified Script to print information about the pp Reference Run PDs in DAS in table format
#
 
from datetime import datetime
import os
from prettytable import PrettyTable
from prettytable import ALL

Dir = "/afs/cern.ch/user/h/honi/CMSSW_7_5_5_patch3/src/PythonScript_pprefEvtVolumeSizeForPDs/AOD"
 
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
x = PrettyTable(["PDs","File Size(GB)","#Events(K)","#Lumis","avg. Event Size(MB)","avg. Lumi Size (MB)"])
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
print "\n AOD statistics for Run2015E-PromptReco-v1 datasets in DAS at", mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss, "(Geneva time)"
print ""
 
totalAODSize = 0
totalAODEvents = 0
totalLumis = 0
for pdName in pdNames:
    dasAODPathName = '/' + pdName + '/Run2015E-PromptReco-v1/AOD'
    findEventsAODCommand = Dir + '/das.py --limit=1000 --format=plain --query="dataset dataset=' + dasAODPathName + ' | grep dataset.nevents" > tmp.txt ; tail -1 tmp.txt > events.txt'
    os.system(findEventsAODCommand)
    fileInput = open('events.txt', 'r')
    thisEvents = 0
    AODEventSize = 0
    for line in fileInput:
        nEvents = line.rstrip('\n')
        if(nEvents != '[]'):
            nEventsM = int(nEvents)/1.0e3 
            thisEvents = int(nEvents)
        else:
            nEvents = 0
            nEventsM = 0
        totalAODEvents += thisEvents
    fileInput.close()
 
    findSizeAODCommand = Dir + '/das.py --limit=1000 --format=plain --query="dataset dataset=' + dasAODPathName + ' | grep dataset.size" > tmp.txt ; tail -1 tmp.txt > size.txt'
    os.system(findSizeAODCommand)
    fileInput = open('size.txt', 'r')
    for line in fileInput:
        AODFileSize = line.rstrip('\n')
        if(AODFileSize == '[]'):
            AODFileSizeGB = 0
        else:
            AODFileSizeGB = int(AODFileSize)/1.0e9
            if(thisEvents > 0):
               AODEventSize = AODFileSizeGB*1.0e3/thisEvents
        totalAODSize += AODFileSizeGB
    fileInput.close()

    countLumiAODCommand = Dir + '/das.py --limit=1000 --format=plain --query="run,lumi dataset=' + dasAODPathName + ' | count(lumi)" > tmp.txt ; tail -1 tmp.txt > lumicounts.txt'
    os.system(countLumiAODCommand)
    fileInput = open('lumicounts.txt','r')
    thisLumis = 0
    for line in fileInput:
        nLumis = line.strip('count(lumi)=')
        if(nLumis != '[]'):
            thisLumis = int(nLumis)
        totalLumis += thisLumis

    if(thisLumis == 0):
        FileSizePerLumi = 0
    else:
        FileSizePerLumi = AODFileSizeGB*1.0e3/thisLumis
    fileInput.close()
   
    x.add_row([pdName,AODFileSizeGB,nEventsM,thisLumis,AODEventSize,FileSizePerLumi])
print x

averageEventSize = totalAODSize*1.0e3/totalAODEvents
if(totalLumis != 0):
    averageFileSizePerLumi = totalAODSize*1.0e3/totalLumis
else:
    averageFileSizePerLumi = 0

print "\n AOD File Summary:"
print " Total Size = ", 
print "%0.1f %s" % (totalAODSize, "GB")
print " Event Number = ", totalAODEvents, "events"
print " avg. Event Size = ", 
print "%0.3f %s" % (averageEventSize, "MB/event")
print " avg. Lumi Size = ",
print "%0.3f %s" % (averageFileSizePerLumi, "MB/Lumi")

exit()
