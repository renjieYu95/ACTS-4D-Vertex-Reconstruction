import re
import itertools


def list_event_labels(config):
    return (
        [f"10mu_pu{pu}" for pu in config["pileups"]]
        + [f"ttbar_pu{pu}" for pu in config["pileups"]]
        + [f"4mu_split_{d}um" for d in config["vertex_distances"]]
        + [f"10mu_split_{d}um" for d in config["vertex_distances"]]
    )


def list_event_sim_labels(config):
    return [
        create_event_sim_label(event, simulation)
        for event, simulation in itertools.product(
            list_event_labels(config), config["simulations"]
        )
    ]


def create_event_sim_label(event_label, simulation_label):
    return f"{event_label}_{simulation_label}"


def split_event_sim_label(event_sim_label):
    m = re.match(r"(.+)_(.+)", event_sim_label)
    if m:
        return m.group(1), m.group(2)
    raise ValueError(f"unknown event label {event_sim_label}")


def get_number_of_events(config, event_sim_label):
    return config["number_of_events"]


def get_events_per_slice(config, event_sim_label):
    return config["events_per_slice"]


def get_skip_events(config, event_sim_label):
    total = get_number_of_events(config, event_sim_label)
    step = get_events_per_slice(config, event_sim_label)
    return range(0, total, step), step


def get_event_details(event_label):
    m = re.match(r"(\d+)mu_pu(\d+)", event_label)
    if m:
        n = int(m.group(1))
        pu = int(m.group(2))
        return "nmu", {"n": n, "pu": pu}
    m = re.match(r"ttbar_pu(\d+)", event_label)
    if m:
        pu = int(m.group(1))
        return "ttbar", {"pu": pu}
    m = re.match(r"(\d+)mu_split_(\d+)um", event_label)
    if m:
        n = int(m.group(1))
        d = int(m.group(2))
        return "nmu_split", {"n": n, "d": d}
    m = re.match(r"(\d+)pi_pu0", event_label)
    if m:
        n = int(m.group(1))
        return "npi_single", {"n": n}
    m = re.match(r"(\d+)mu_pu0", event_label)
    if m:
        n = int(m.group(1))
        return "nmu_single", {"n": n}
    raise ValueError(f"unknown event: {event_label}")


def list_reco_labels(config):
    return [create_reco_label(seeding) for seeding in config["seedings"]]


def create_reco_label(seeding):
    return f"{seeding}"


def split_reco_label(reco_label):
    return reco_label
