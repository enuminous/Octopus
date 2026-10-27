# OCTOPUS

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Octopus) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Intended uses](#intended-uses)
- [Core idea](#core-idea)
- [Flat-stack repository](#flat-stack-repository)
- [Scientific hypothesis](#scientific-hypothesis)
- [Baselines](#baselines)
- [Primary evaluation](#primary-evaluation)
- [Installation](#installation)
- [Run example](#run-example)
- [Tests](#tests)
- [Minimal usage](#minimal-usage)
- [Freeze rule](#freeze-rule)
- [Negative results](#negative-results)
- [Status](#status)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Gecko](https://github.com/enuminous/Gecko) · [Owl](https://github.com/enuminous/Owl) · [Hive](https://github.com/enuminous/Hive)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


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
