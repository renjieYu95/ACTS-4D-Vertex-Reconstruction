#!/usr/bin/env python3
import acts
from pathlib import Path
from typing import Any, Optional, Union
from acts.examples.simulation import (
    addPythia8,
    
)
import acts.examples
from mycommon.labels import get_event_details

u = acts.UnitConstants

def addMyEventGen(
    outputDir,
    sequencer: acts.examples.Sequencer=None,
    outputRoot: bool = True,
#    rnd: acts.examples.RandomNumbers,
#  outputDirRoot: Optional[Union[Path, str]] = None,
):
    outputDir=Path(outputDir)
  
  # unknown
    hllhcVtxGen = acts.examples.GaussianVertexGenerator(
        mean=acts.Vector4(0, 0, 0, 0),
        stddev=acts.Vector4(0.0125 * u.mm, 0.0125 * u.mm, 50.0 * u.mm, 180.0 * u.ps),
    )
    rnd = acts.examples.RandomNumbers(seed=42)
#    event_type, event_details = get_event_details(event_label)
#    if event_type == "ttbar":
#        pu = event_details["pu"]
    sequencer = acts.examples.Sequencer(
    events=10,
    numThreads=-1,
    logLevel=acts.logging.INFO
)
    addPythia8(
            sequencer,
            rnd=rnd,
            nhard=1,
            npileup=200,
            beam=acts.PdgParticle.eProton,
            cmsEnergy=14 * u.TeV,
            hardProcess=["Top:qqbar2ttbar = on"],
            pileupProcess=["SoftQCD:all = on"],
            vtxGen=hllhcVtxGen,
            outputDirRoot=outputDir,
        )

    return sequencer
  
    raise ValueError(f"unknown event type: {event_type}")

if "__main__" == __name__:
    addMyEventGen(Path("/afs/cern.ch/user/r/reyu/private/mywork/gunoutput")).run()










