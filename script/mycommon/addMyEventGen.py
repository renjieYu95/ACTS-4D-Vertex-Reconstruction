import acts
from acts.examples.simulation import (
    addPythia8,
    
)
import acts.examples
from mycommon.labels import get_event_details

u = acts.UnitConstants

def addMyEventGen(
  sequencer: acts.example.Sequencer,
  event_label: str,
  rnd: acts.examples.RandomNumbers,
  outputDirRoot: Optional[Union[Path, str]] = None,
):
  
  # unknown
  hllhcVtxGen = acts.examples.GaussianVertexGenerator(
        mean=acts.Vector4(0, 0, 0, 0),
        stddev=acts.Vector4(0.0125 * u.mm, 0.0125 * u.mm, 50.0 * u.mm, 180.0 * u.ps),
    )
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

        return
  
raise ValueError(f"unknown event type: {event_type}")

if "__main__" == __name__:
  sequencer = acts.examples.Sequencer(
    events=10,         
    numThreads=-1,     
    logLevel=acts.logging.INFO 
)
  rnd = acts.examples.RandomNumbers(seed=42)
    MyEventGen(sequencer,ttbar_pu200).run()










