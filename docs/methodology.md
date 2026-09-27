## Research Methodology

1. Transaction Graph Representation

The proposed framework represents cryptocurrency transactions as a directed graph.

* Nodes: Cryptocurrency wallets
* Edges: Transactions between wallets
* Edge weight: Transaction amount
* Timestamp: Time associated with the transaction

This representation allows transaction relationships and movement patterns to be analyzed from a graph perspective.

2. Behavioural Indicators

The research considers behavioural patterns that may indicate unusual activity:

Rapid Multi-Hop Movement

Funds moving through several wallets within a short period.

Repetitive Micro-Splitting

A larger amount being divided into multiple smaller transactions.

Abnormal Transaction Frequency

A wallet performing significantly more transactions than expected within a given period.

Unusual Connectivity

Wallets exhibiting unusually high or strategically positioned connectivity within the transaction network.

3. Graph-Based Analysis

Two graph measures are considered:

Degree Centrality

Degree centrality measures the connectivity of a wallet within the transaction network.

A wallet with unusually high connectivity may require further investigation.

Betweenness Centrality

Betweenness centrality measures how frequently a wallet lies on paths connecting other wallets.

A wallet with high betweenness may act as an important intermediary within the transaction network.

4. Statistical Anomaly Detection

The proposed framework considers statistical techniques for identifying unusual observations.

Z-Score

The Z-score measures how far an observation is from the mean:

Z = (x − μ) / σ

where:

* x = observed value
* μ = mean
* σ = standard deviation

A high absolute Z-score can indicate an observation that differs substantially from the population.

Interquartile Range

The IQR method uses:

IQR = Q3 − Q1

Values outside the commonly used boundaries:

Lower Bound = Q1 − 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR

may be treated as statistical outliers.

5. Explainability

The main objective is not simply to classify a wallet as anomalous.

The framework aims to provide interpretable indicators such as:

* unusually high degree
* high betweenness
* abnormal transaction frequency
* rapid movement patterns
* unusual transaction amounts

This allows an analyst to understand the factors contributing to an anomaly.

6. Conceptual Pipeline

Transaction Data
       ↓
Data Preparation
       ↓
Transaction Graph
       ↓
Behavioural Features
       ↓
Graph Metrics
       ↓
Statistical Analysis
       ↓
Anomaly Identification
       ↓
Explainable Results

7. Research Scope

This methodology is intended as an analytical research framework.

An identified anomaly does not establish that a wallet or transaction is involved in illegal activity. Further investigation and contextual information would be required.
