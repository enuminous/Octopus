import json
import pandas as pd
from octopus import OCTOPUSExperiment

data = pd.read_csv("example_data.csv")
edges = pd.read_csv("example_edges.csv")

exp = OCTOPUSExperiment(
    time_column="time",
    target_column="failure",
    feature_columns=["node_a","node_b","node_c","node_d"],
    horizons=(1,3,7,23),
    random_state=23,
)

result = exp.run(data, edges)
print(json.dumps(result, indent=2))
