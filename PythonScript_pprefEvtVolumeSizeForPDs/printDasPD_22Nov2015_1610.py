#!/usr/bin/env python
#
# Script to print information about the pp Reference Run PDs in DAS
#
 
from datetime import datetime
import os
 
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
 
now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print "\n RAW statistics for Run2015E-v1 datasets in DAS at", mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss, "(Chicago time)"
print ""
 
totalRawSize = 0
totalRawEvents = 0
for pdName in pdNames:
    dasRawPathName = '/' + pdName + '/Run2015E-v1/RAW'
    findEventsRawCommand = './das.py --limit=1000 --format=plain --query="dataset dataset=' + dasRawPathName + ' | grep dataset.nevents" > tmp.txt ; tail -1 tmp.txt > events.txt'
    #print "\n findEventsRawCommand ", findEventsRawCommand
    os.system(findEventsRawCommand)
    fileInput = open('events.txt', 'r')
    thisEvents = 0
    rawEventSize = 0
    for line in fileInput:
        nEvents = line.rstrip('\n')
        if(nEvents != '[]'):
            thisEvents = int(nEvents)
            totalRawEvents += thisEvents
    fileInput.close()
 
    findSizeRawCommand = './das.py --limit=1000 --format=plain --query="dataset dataset=' + dasRawPathName + ' | grep dataset.size" > tmp.txt ; tail -1 tmp.txt > size.txt'
    #print "\n findSizeRawCommand ", findSizeRawCommand
    os.system(findSizeRawCommand)
    fileInput = open('size.txt', 'r')
    for line in fileInput:
        rawFileSize = line.rstrip('\n')
        if(rawFileSize == '[]'):
              rawFileSizeGB = 0
        else:
              rawFileSizeGB = int(rawFileSize)/1.0e9
              if(thisEvents > 0):
                   rawEventSize = rawFileSizeGB*1.0e3/thisEvents
        totalRawSize += rawFileSizeGB
    fileInput.close()
 
    print " PD", pdName, "has", nEvents, "events with a volume size",
    print "%0.1f %s" % (rawFileSizeGB, "GB"),
    print "%s %0.3f %s" % ("giving a RAW event size", rawEventSize, "MB/event")
 
print "\n The total size of the RAW files is",
print "%0.1f %s" % (totalRawSize, "GB"),
print "with", totalRawEvents, "events",
averageEventSize = totalRawSize*1.0e3/totalRawEvents
print "%s %0.3f %s" % ("giving an average RAW event size", averageEventSize, "MB/event")
exit()
