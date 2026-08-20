import pandas as pd
from graph_features import build_graph_features
from octopus import OCTOPUSExperiment

def test_graph_features():
    df = pd.read_csv("example_data.csv")
    edges = pd.read_csv("example_edges.csv")
    gf = build_graph_features(
        df, edges,
        ["node_a","node_b","node_c","node_d"],
        horizons=(1,3,7,23),
    )
    assert len(gf) == len(df)
    assert "distributed_contradiction" in gf.columns
    assert "missing_fraction" in gf.columns

def test_experiment_runs():
    df = pd.read_csv("example_data.csv")
    edges = pd.read_csv("example_edges.csv")
    exp = OCTOPUSExperiment(
        time_column="time",
        target_column="failure",
        feature_columns=["node_a","node_b","node_c","node_d"],
    )
    out = exp.run(df, edges)
    assert "results" in out
    assert "octopus" in out["results"]
    assert "local_only" in out["results"]
