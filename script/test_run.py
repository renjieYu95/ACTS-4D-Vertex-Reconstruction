#! /usr/bin/env python3

import argparse, tempfile
import shutil
from pathlib import Path
from mycommon.sequencer import get_sequencer
from mycommon.addMyEventGen1 import addMyEventGen1
from mycommon.rng import get_rng
from mycommon.labels import split_event_sim_label

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("event_label")
    parser.add_argument("outdir")
    parser.add_argument("--skip", type=int, required=True, help="Skip number of events")
    parser.add_argument("--events", type=int, required=True, help="Number of events")
    parser.add_argument("--threads", type=int, default=1, help="Number of threads")
    parser.add_argument("--use-event-seed", action="store_true", help="Use event seed")
    args = parser.parse_args()

    event_label, simulation_label = split_event_sim_label(args.event_label)

    outdir = Path(args.outdir)
    skip = args.skip
    events = args.events

    with tempfile.TemporaryDirectory() as temp:
        run(
            threads=args.threads,
            use_event_seed=args.use_event_seed,
            tp=Path(temp),
            event_label=event_label,
            outdir=outdir,
            skip=skip,
            events=events,

                )
    return 0

def run(
    threads: int,
    use_event_seed: bool,
    tp: Path,
    event_label: str,
    outdir: Path,
    skip: int,
    events: int,
    ):

    output_files = []
    rng = get_rng(not use_event_seed, event_label)

    sequencer = get_sequencer(
        output_files=output_files,
        skip=skip,
        events=events,
        threads=threads,
        tp=tp,
            )
    addMyEventGen1(
        output_files=output_files,
        sequencer=sequencer,
        event_label=event_label,
        rnd=rng,
        outputDirRoot=tp,
            )
    sequencer.run()
    del sequencer

    outdir.mkdir(parents=True, exist_ok=True)
    for file in output_files:
        source = tp / file["file"]
        destination = outdir / file["move"] if "move" in file else outdir / file["file"]
        assert source.exists(), f"File not found: {source}"
        shutil.copy(source, destination)

if __name__ == "__main__":
    main()

