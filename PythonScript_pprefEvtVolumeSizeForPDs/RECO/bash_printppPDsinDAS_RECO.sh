#!/bin/bash
cd /afs/cern.ch/user/h/honi/CMSSW_7_5_5_patch3/src
eval `scramv1 runtime -sh` 

python /afs/cern.ch/user/h/honi/CMSSW_7_5_5_patch3/src/PythonScript_pprefEvtVolumeSizeForPDs/RECO/printppPDsinDAS_RECO.py &> /afs/cern.ch/user/h/honi/CMSSW_7_5_5_patch3/src/PythonScript_pprefEvtVolumeSizeForPDs/RECO/output_printppPDsinDAS_RECO.txt
