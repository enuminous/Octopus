import numpy as np
import pandas as pd

EPS = 1e-8

def robust_fill(series):
    med = series.expanding(min_periods=1).median()
    return series.fillna(med).fillna(0.0)

def robust_z(series, window=23):
    s = robust_fill(series.astype(float))
    med = s.rolling(window, min_periods=3).median()
    mad = (s-med).abs().rolling(window, min_periods=3).median()
    return ((s-med)/(1.4826*mad+EPS)).replace([np.inf,-np.inf], np.nan).fillna(0.0)

def build_graph_features(df, edges, feature_columns, horizons=(1,3,7,23)):
    out = pd.DataFrame(index=df.index)

    # Node state + missingness
    filled = {}
    for c in feature_columns:
        s = df[c].astype(float)
        out[f"{c}__missing"] = s.isna().astype(float)
        fs = robust_fill(s)
        filled[c] = fs
        out[f"{c}__z"] = robust_z(fs, max(horizons))
        out[f"{c}__dx"] = fs.diff().fillna(0.0)

    # Edge relational state
    edge_cols = []
    for _, row in edges.iterrows():
        a, b = row["source"], row["target"]
        if a not in filled or b not in filled:
            continue
        lag = int(row.get("lag", 0))
        sb = filled[b].shift(lag) if lag > 0 else filled[b]
        diff = filled[a] - sb
        prod = filled[a] * sb
        corr = filled[a].rolling(max(horizons), min_periods=3).corr(sb)

        dname = f"edge__{a}__{b}__lag{lag}__diff"
        pname = f"edge__{a}__{b}__lag{lag}__prod"
        cname = f"edge__{a}__{b}__lag{lag}__corr"

        out[dname] = robust_z(diff, max(horizons)).abs()
        out[pname] = robust_z(prod, max(horizons)).abs()
        out[cname] = corr.fillna(0.0)
        edge_cols.extend([dname, pname, cname])

    if edge_cols:
        out["distributed_contradiction"] = out[edge_cols].abs().mean(axis=1)
        out["distributed_dispersion"] = out[edge_cols].std(axis=1).fillna(0.0)
    else:
        out["distributed_contradiction"] = 0.0
        out["distributed_dispersion"] = 0.0

    # Missingness itself is distributed state.
    miss_cols = [f"{c}__missing" for c in feature_columns]
    out["missing_fraction"] = out[miss_cols].mean(axis=1)

    # Multiscale persistence.
    for h in horizons:
        out[f"dc_mean_{h}"] = out["distributed_contradiction"].rolling(h, min_periods=1).mean()
        out[f"dd_mean_{h}"] = out["distributed_dispersion"].rolling(h, min_periods=1).mean()
        out[f"missing_mean_{h}"] = out["missing_fraction"].rolling(h, min_periods=1).mean()

    return out.replace([np.inf,-np.inf], np.nan).fillna(0.0)
