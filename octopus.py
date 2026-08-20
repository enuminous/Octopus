from dataclasses import dataclass
import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LogisticRegression

from graph_features import build_graph_features
from latent_state import latent_proxy, neighborhood_reconstruction
from baselines import ProbModel, BaseRateModel
from metrics import binary_metrics, stratified_by_missingness

@dataclass
class OCTOPUSExperiment:
    time_column: str
    target_column: str
    feature_columns: list
    horizons: tuple = (1,3,7,23)
    train_fraction: float = 0.65
    random_state: int = 23

    def run(self, df, edges):
        df = df.sort_values(self.time_column).reset_index(drop=True).copy()
        cut = max(10, int(len(df)*self.train_fraction))
        y = df[self.target_column].astype(int).to_numpy()

        gf = build_graph_features(df, edges, self.feature_columns, self.horizons)
        gf["latent_proxy"] = latent_proxy(gf, self.horizons)

        # Local-only observed features + missingness
        local = pd.DataFrame(index=df.index)
        for c in self.feature_columns:
            local[c] = df[c].astype(float)
            local[f"{c}__missing"] = df[c].isna().astype(float)
        local = local.ffill().fillna(0.0)

        # Conventional neighborhood reconstruction baseline
        neigh = neighborhood_reconstruction(df, edges, self.feature_columns)
        neigh = pd.concat([local, neigh], axis=1).fillna(0.0)

        # OCTOPUS combines local and graph-relational state
        octo = pd.concat([local, gf], axis=1).fillna(0.0)

        models = {
            "octopus": (ProbModel(self.random_state), octo),
            "local_only": (ProbModel(self.random_state), local),
            "neighbor_graph": (ProbModel(self.random_state), neigh),
            "base_rate": (BaseRateModel(), local),
        }

        results = {}
        for name, (model, X) in models.items():
            model.fit(X.iloc[:cut], y[:cut])
            p = model.predict_proba(X.iloc[cut:])
            results[name] = {
                "overall": binary_metrics(y[cut:], p),
                "by_missingness": stratified_by_missingness(
                    y[cut:], p, gf["missing_fraction"].to_numpy()[cut:]
                )
            }

        return {
            "n_total": len(df),
            "train_n": cut,
            "test_n": len(df)-cut,
            "results": results,
            "primary_delta_brier_local_minus_octopus": (
                results["local_only"]["overall"]["brier"]
                - results["octopus"]["overall"]["brier"]
            ),
            "interpretation": (
                "Positive delta favors OCTOPUS over the matched local-only model. "
                "Performance should also be examined separately under higher missingness."
            )
        }
