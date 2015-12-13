import FWCore.ParameterSet.Config as cms

import RpPbAnalysis.ppPileupFilter.pileUpFilter_cfi

pileupVertexFilterCutG = RpPbAnalysis.ppPileupFilter.pileUpFilter_cfi.pileupVertexFilter.clone()

pileupFilter_baseCut_loose = pileupVertexFilterCutG.clone(
                                                           dzCutByNtrk = cms.vdouble(
                                                                                    999.,999.,999.,4.8,1.9,
                                                                                     1.2, 0.8, 0.8,0.8,0.6,
                                                                                     0.5, 0.4, 0.4,0.3,0.2,
                                                                                     0.2, 0.2, 0.2,0.2,0.2,
                                                                                     0.1, 0.1, 0.1,0.1,0.1,
                                                                                     0.1, 0.1, 0.1,0.1,0.1,
                                                                                     0.1, 0.0
                                                                                    ),  
                                                           dxyVeto = cms.double(0.05)
                                                       )

pileupFilter_baseCut_tight = pileupVertexFilterCutG.clone(
                                                           dzCutByNtrk = cms.vdouble(
                                                                                    999.,999.,4.0,1.5,1.0,
                                                                                     0.6, 0.5,0.4,0.3,0.3,
                                                                                     0.3, 0.2,0.2,0.2,0.1,
                                                                                     0.1, 0.1,0.1,0.1,0.1,
                                                                                     0.1, 0.1,0.1,0.0
                                                                                    ),
                                                           dxyVeto = cms.double(0.05) 
                                                       )

pileupFilter_baseCut_loose_dz1p0 = pileupVertexFilterCutG.clone(
                                                           dzCutByNtrk = cms.vdouble(
                                                                                    999.,999.,999.,4.8,1.9,
                                                                                     1.2, 0.8, 0.8,0.8,0.6,
                                                                                     0.5, 0.4, 0.4,0.3,0.2,
                                                                                     0.2, 0.2, 0.2,0.2,0.2,
                                                                                     0.1, 0.1, 0.1,0.1,0.1,
                                                                                     0.1, 0.1, 0.1,0.1,0.1,
                                                                                     0.1, 0.0
                                                                                    ),
                                                           dxyVeto = cms.double(0.05),
                                                           dzTolerance = cms.double(1.0)
                                                       )

pileupFilter_baseCut_tight_dz1p0 = pileupVertexFilterCutG.clone(
                                                           dzCutByNtrk = cms.vdouble(
                                                                                    999.,999.,4.0,1.5,1.0,
                                                                                     0.6, 0.5,0.4,0.3,0.3,
                                                                                     0.3, 0.2,0.2,0.2,0.1,
                                                                                     0.1, 0.1,0.1,0.1,0.1,
                                                                                     0.1, 0.1,0.1,0.0
                                                                                    ),
                                                           dxyVeto = cms.double(0.05),
                                                           dzTolerance = cms.double(1.0)
                                                       )

pileupFilter_vtx1 = pileupVertexFilterCutG.clone(
                                                           dzCutByNtrk = cms.vdouble(
                                                                                     999.,0.0,0.0,0.0,0.0
                                                                                    ),
                                                           dzTolerance = cms.double(9999.0)

                                                )                                                           
 


