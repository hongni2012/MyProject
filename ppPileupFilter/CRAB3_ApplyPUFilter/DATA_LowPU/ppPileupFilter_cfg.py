import FWCore.ParameterSet.Config as cms

process = cms.Process("TRACKANA")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('RpPbAnalysis.ppPileupFilter.ppPileupFilter_cff')

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(5000)
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('pileupfilterstudy.root')
)

process.GlobalTag.globaltag = '75X_dataRun2_Prompt_ppAt5TeV_v0'

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        '/store/data/Run2015E/MinimumBias12/AOD/PromptReco-v1/000/262/163/00000/0EFA48B3-FA91-E511-B192-02163E01379F.root',
    )
)

process.load("RpPbAnalysis.ppPileupFilter.pileUpFilter_cff")

process.NoPUFilter = process.ppPileup.clone()
process.p0 = cms.Path(process.NoPUFilter)

process.applybaseCut_loose = process.ppPileup.clone()
process.p1 = cms.Path(process.pileupFilter_baseCut_loose*process.applybaseCut_loose)

process.applybaseCut_loose_dz1p0 = process.ppPileup.clone()
process.p2 = cms.Path(process.pileupFilter_baseCut_loose_dz1p0*process.applybaseCut_loose_dz1p0)

process.applybaseCut_tight = process.ppPileup.clone()
process.p3 = cms.Path(process.pileupFilter_baseCut_tight*process.applybaseCut_tight)

process.applybaseCut_tight_dz1p0 = process.ppPileup.clone()
process.p4 = cms.Path(process.pileupFilter_baseCut_tight_dz1p0*process.applybaseCut_tight_dz1p0)

process.selectevtsonlyonevtx = process.ppPileup.clone()
process.p5 = cms.Path(process.pileupFilter_vtx1*process.selectevtsonlyonevtx)


