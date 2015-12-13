import FWCore.ParameterSet.Config as cms

ppPileup = cms.EDAnalyzer('ppPileupFilter',
    trackSrc = cms.InputTag("generalTracks"),
    vertexSrc = cms.InputTag("offlinePrimaryVertices"),
    vertexZMax = cms.double(15.0),
    ptBins = cms.vdouble(
        0,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.4,1.6,1.8,2.0,2.2,2.4,3.2,4.0,4.8,5.6,6.4,7.2,9.6,
        12.0,14.4,19.2,24.0,28.8,35.2,41.6,48.0,60.8,73.6,86.4,103.6,120.8
    ),    
    qualityString = cms.string("highPurity"),
    dxySigMax = cms.double(3.0),
    dzSigMax = cms.double(3.0),
    ptErrOverptMax = cms.double(0.1) 
)
