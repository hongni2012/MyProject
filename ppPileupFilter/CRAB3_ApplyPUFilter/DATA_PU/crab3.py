from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'ppPUStudy'
config.General.workArea = 'crab_projects_ppPUStudy'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ppPileupFilter_cfg.py'
config.Data.inputDataset = '/MinimumBias3/Run2015E-PromptReco-v1/AOD'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/5TeV/Cert_262081-262273_5TeV_PromptReco_Collisions15_25ns_JSON.txt'
config.Data.runRange = '262081-262273'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 15
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

   for num in range(1,2):
       RequestName = 'Run2015ppPUStudyMB'+str(num)
       DataSetName = '/MinimumBias'+ str(num) +'/Run2015E-PromptReco-v1/AOD'
       config.General.requestName = RequestName
       config.Data.inputDataset = DataSetName
       config.Data.outputDatasetTag = 'CRAB3_ppPUStudy_DATA_PU'
       submit(config)

# python crab3_ppTrackingAnalyzer.py to execute 
# ./multicrab -c status -w crab_projects/ to check status 
