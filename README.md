# Explainable Cryptocurrency AML

An academic research project exploring an explainable approach to identifying potentially anomalous cryptocurrency transaction patterns using transaction graphs and statistical anomaly detection.

 Overview :

Cryptocurrency transactions can involve complex movement patterns that may make suspicious activity difficult to identify using simple transaction-level rules.

This research explores a graph-based and explainable approach where cryptocurrency wallets are represented as nodes and transactions are represented as weighted, time-stamped edges.

The goal is to identify unusual transaction behaviour while keeping the detection process interpretable.

🎯 Objectives

* Model cryptocurrency transactions as a graph
* Identify potentially anomalous transaction patterns
* Analyze wallet connectivity and transaction behaviour
* Use statistical methods for anomaly detection
* Apply graph-based measures such as degree and betweenness centrality
* Provide interpretable reasons for why a transaction or wallet may be considered anomalous

🔬 Proposed Methodology

The research focuses on three major areas:

1. Transaction Graph Analysis

* Wallets → Nodes
* Transactions → Edges
* Transaction amount → Edge weight
* Transaction time → Temporal information

2. Behavioural Indicators

The proposed analysis considers patterns such as:

* Rapid multi-hop movement
* Repetitive micro-splitting
* Abnormal transaction frequency
* Unusual wallet connectivity

3. Explainable Anomaly Detection

Statistical techniques such as:

* Z-score
* Interquartile Range (IQR)

can be combined with graph metrics such as:

* Degree centrality
* Betweenness centrality

to identify unusual behaviour and provide interpretable indicators.

🏗️ Conceptual Architecture

Cryptocurrency Transactions
          ↓
Data Representation
          ↓
Transaction Graph
          ↓
Feature & Behaviour Analysis
          ↓
Graph Metrics + Statistical Detection
          ↓
Anomaly Identification
          ↓
Explainable Results

💡 Research Focus

The key focus of this work is explainability.

Rather than only producing an anomaly label, the approach aims to provide understandable indicators explaining why a wallet or transaction pattern appears unusual.

⚠️ Limitations

This research does not claim to:

* Identify the real-world identity of wallet owners
* Establish criminal activity
* Replace regulatory investigation
* Provide real-time enforcement
* Guarantee that every detected anomaly represents illicit activity

An anomaly should be treated as an indicator requiring further investigation.

🚀 Future Work

Future development could include:

* Implementation using real or appropriately anonymized datasets
* Temporal graph analysis
* Machine learning-based anomaly detection
* Graph Neural Networks (GNNs)
* Interactive visualization
* Real-time monitoring
* Comparison with existing AML approaches

📚 Status

Research / Conceptual Prototype

This repository documents the research methodology and conceptual framework. Implementation components may be added as the research progresses.

⸻

Author: Harshika Kilaru
Field: Computer Science & Business Systems


## 💻 Prototype

A small Python prototype demonstrates the core concept using synthetic cryptocurrency transaction data.

The prototype currently demonstrates:

* Transaction graph construction
* Wallet degree analysis
* Z-score calculation
* Potential anomaly identification

🛠️ Tech Stack

* Python
* Pandas
* NetworkX

▶️ How to Run

Clone the repository:

git clone https://github.com/HarshikaKilaru/Cryptocurrency-AML-Explainability.git

Navigate to the project:

cd Cryptocurrency-AML-Explainability

Install dependencies:

pip install -r requirements.txt

Run the prototype:

python src/aml_prototype.py

📊 Example Output

The prototype produces wallet-level graph statistics and identifies observations that may require further investigation based on the selected statistical threshold.

Example:

Wallet Analysis
  wallet  degree  z_score  potential_anomaly
0     W1       2    ...
1     W2       3    ...
2     W3       3    ...
3     W4       3    ...
4     W5       2    ...
5     W6       2    ...
6     W7       2    ...
Potentially anomalous wallets:
...

The output is intended to demonstrate how graph metrics and statistical analysis can be combined to produce interpretable anomaly indicators.

Note: The prototype uses synthetic transaction data. The example output should not be interpreted as evidence of illicit activity or as a real-world AML finding.

📊 Prototype Status

This is an early research prototype using synthetic transaction data. It is intended to demonstrate the proposed methodology and is not a production AML detection system.
