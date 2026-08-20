import numpy as np
import pandas as pd

def latent_proxy(graph_features, horizons=(1,3,7,23)):
    parts = [
        graph_features["distributed_contradiction"],
        graph_features["distributed_dispersion"],
        graph_features["missing_fraction"],
    ]
    for h in horizons:
        parts.extend([
            graph_features[f"dc_mean_{h}"],
            graph_features[f"dd_mean_{h}"],
            graph_features[f"missing_mean_{h}"],
        ])
    stack = pd.concat(parts, axis=1)
    ranked = stack.rank(pct=True)
    return ranked.mean(axis=1).fillna(0.0)

def neighborhood_reconstruction(df, edges, feature_columns):
    out = pd.DataFrame(index=df.index)
    for target in feature_columns:
        incoming = edges.loc[edges["target"] == target, "source"].tolist()
        incoming = [c for c in incoming if c in feature_columns]
        if incoming:
            out[f"{target}__neighbor_mean"] = df[incoming].astype(float).mean(axis=1)
        else:
            out[f"{target}__neighbor_mean"] = 0.0
    return out.fillna(0.0)
