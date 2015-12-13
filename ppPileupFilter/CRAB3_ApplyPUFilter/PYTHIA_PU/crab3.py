from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'ppPUStudy'
config.General.workArea = 'crab_projects_ppPUStudy'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ppPileupFilter_cfg.py'
config.Data.inputDataset = ''
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = ''

config.Site.storageSite = 'T2_US_Vanderbilt'

if __name__ == '__main__':
   from CRABAPI.RawCommand import crabCommand
   from CRABClient.ClientExceptions import ClientException
   from httplib import HTTPException

   config.General.workArea = 'crab_projects_ppPUStudy'

   def submit(config):
      try:
           crabCommand('submit', config = config)
      except HTTPException as hte:
           print "Failed submitting task: %s" % (hte.headers)
      except ClientException as cle:
          print "Failed submitting task: %s" % (cle)
 
   DataType = ["PYTHIA_PU"]

   DataSamples = ["/Neutrinos5Mfor5TeVpp/gsfs-pp5TeVPileupAOD__2015_11_18-0fbbb68e7aea6e58696cc3c7d18d21c8/USER"] 

   RequestName = DataType[0]
   DataSetName = DataSamples[0]
   config.General.requestName = RequestName
   config.Data.inputDataset = DataSetName
   config.Data.outputDatasetTag = 'CRAB3_ppPUStudy_PYTHIA_PU'
   submit(config)

# python crab3_ppTrackingAnalyzer.py to execute 
# ./multicrab -c status -w crab_projects/ to check status 
