#/usr/bin/env pythion3
import acts
from pathlib import Path
from typing import Any, Optional, Union
from acts.examples.simulation import (
    addPythia8,
    
)
import acts.examples
from mycommon.labels import get_event_details

u = acts.UnitConstants

def addMyEventGen1(
    output_files: list[dict[str, str]],
    sequencer: acts.examples.Sequencer,
    event_label: str,
    rnd: acts.examples.RandomNumbers,
    outputDirRoot: Optional[Union[Path, str]] = None,
):
  
    # unknow
    hllhcVtxGen = acts.examples.GaussianVertexGenerator(
        mean=acts.Vector4(0, 0, 0, 0),
        stddev=acts.Vector4(0.0125 * u.mm, 0.0125 * u.mm, 50.0 * u.mm, 180.0 * u.ps),
    )
    rnd = acts.examples.RandomNumbers(seed=42)
    event_type, event_details = get_event_details(event_label)

    if event_type == "ttbar":
        pu = event_details["pu"]

        addPythia8(
            sequencer,
            rnd=rnd,
            nhard=1,
            npileup=pu,
            beam=acts.PdgParticle.eProton,
            cmsEnergy=14 * u.TeV,
            hardProcess=["Top:qqbar2ttbar = on"],
            pileupProcess=["SoftQCD:all = on"],
            vtxGen=hllhcVtxGen,
            outputDirRoot=outputDirRoot,
        )


  
    raise ValueError(f"unknown event type: {event_type}")

    output_files.append({"file": "particles.root", "move": "particles_generator.root"})
    output_files.append({"file": "vertices.root", "move": "vertices_generator.root"})
    return

#if "__main__" == __name__:
#    addMyEventGen(Path("/afs/cern.ch/user/r/reyu/private/mywork/gunoutput")).run()










