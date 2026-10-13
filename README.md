# OCTOPUS

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Octopus) · This repository is linked through its source; GitHub Pages is not enabled.

<details>
<summary>Recent repositories (9)</summary>

- [Oroboros](https://github.com/enuminous/Oroboros) · [README](https://github.com/enuminous/Oroboros/blob/main/README.md) · [Page](https://enuminous.github.io/Oroboros/)
- [P-NP](https://github.com/enuminous/P-NP) · [README](https://github.com/enuminous/P-NP/blob/main/README.md) · [Page](https://enuminous.github.io/P-NP/)
- [Research-Program](https://github.com/enuminous/Research-Program) · [README](https://github.com/enuminous/Research-Program/blob/main/README.md) · [Page](https://enuminous.github.io/Research-Program/)
- [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) · [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) · [Page](https://enuminous.github.io/I-Have-Guts/)
- [Wrights-Law](https://github.com/enuminous/Wrights-Law) · [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) · [Page](https://enuminous.github.io/Wrights-Law/)
- [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) · [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) · [Page](https://enuminous.github.io/Aristotle-eNuminous/)
- [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) · [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) · [Page](https://enuminous.github.io/Multiverse-Simulator/)
- [accelerando-8192](https://github.com/enuminous/accelerando-8192) · [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) · [Page source](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html)
- [Codex-888](https://github.com/enuminous/Codex-888) · [README](https://github.com/enuminous/Codex-888/blob/main/README.md) · [Page](https://enuminous.github.io/Codex-888/)

</details>
<!-- ENUMINOUS-NETWORK:END -->

**Observational Coupling and Temporal Orchestration of Partially Unobserved Systems**

OCTOPUS is an EFMW-derived framework for distributed systems where no single sensor, node, agent, or subsystem contains the full state.

Its central question is:

> Can relational structure among partially observed components recover useful information about the system's hidden or future state?

## Intended uses

- sensor networks
- distributed AI agents
- robotics fleets
- industrial systems
- logistics and supply chains
- power and communications networks
- multi-service software systems
- ecological networks
- organizational systems

## Core idea

OCTOPUS treats missingness, disagreement, coupling change, lagged influence, and graph-wide contradiction as signal.

```text
observed nodes
→ node normalization
→ missingness map
→ pairwise / lagged coupling
→ graph construction
→ distributed contradiction
→ neighborhood propagation
→ latent-state proxy
→ target prediction
```

## Flat-stack repository

Everything lives at repository root.

```text
README.md
LICENSE
CITATION.cff
pyproject.toml
requirements.txt
octopus.py
graph_features.py
latent_state.py
baselines.py
metrics.py
freeze.py
forecast_schema.json
example_config.yaml
example_data.csv
example_edges.csv
example_run.py
test_octopus.py
MANIFEST.sha256
```

## Scientific hypothesis

The default hypothesis is narrow:

> In partially observed systems, changes in relationships among observed components may contain predictive information not available from the observed components individually.

OCTOPUS does not assume this is true.

## Baselines

Included comparisons:

- local-only logistic model
- imputed local-only model
- simple graph-neighborhood average
- persistence / base-rate predictor

## Primary evaluation

For binary target states:

- Brier score
- log loss
- ROC-AUC
- average precision
- accuracy
- missingness-stratified performance

The most important comparison is:

> Does graph-relational state improve out-of-sample prediction over matched local-only models?

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run example

```bash
python example_run.py
```

## Tests

```bash
pytest -q
```

## Minimal usage

```python
import pandas as pd
from octopus import OCTOPUSExperiment

data = pd.read_csv("example_data.csv")
edges = pd.read_csv("example_edges.csv")

exp = OCTOPUSExperiment(
    time_column="time",
    target_column="failure",
    feature_columns=["node_a", "node_b", "node_c", "node_d"],
    horizons=(1, 3, 7, 23),
    random_state=23,
)

result = exp.run(data, edges)
print(result)
```

## Freeze rule

Before prospective evaluation freeze:

- node list
- edge list
- directionality
- lag set
- missingness rules
- imputation rules
- feature definitions
- horizons
- model capacity
- target
- cutoff
- baselines
- metrics
- exclusions

Then run:

```bash
python freeze.py
```

## Negative results

If local-only or conventional graph baselines match OCTOPUS, no OCTOPUS-specific contribution has been demonstrated.

## Status

Research software. Experimental. Not validated for safety-critical deployment.
