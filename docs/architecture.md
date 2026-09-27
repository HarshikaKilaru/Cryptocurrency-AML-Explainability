## System Architecture

# Conceptual Architecture

The proposed framework follows a pipeline from cryptocurrency transaction data to explainable anomaly identification.

┌──────────────────────────────┐
│   Cryptocurrency Transactions │
│      Wallet & Transaction Data │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       Data Preparation       │
│  Cleaning • Formatting       │
│  Feature Preparation        │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│      Transaction Graph       │
│  Wallets → Nodes             │
│  Transactions → Edges        │
│  Amount → Edge Weight        │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   Behavioural Analysis      │
│  • Transaction Frequency     │
│  • Rapid Multi-Hop Movement  │
│  • Micro-Splitting           │
│  • Connectivity Patterns     │
└──────────────┬───────────────┘
               ↓
       ┌───────┴────────┐
       ↓                ↓
┌──────────────┐ ┌───────────────┐
│ Graph Metrics│ │  Statistical  │
│              │ │   Detection   │
│ • Degree     │ │ • Z-Score     │
│ • Betweenness│ │ • IQR         │
└──────┬───────┘ └───────┬───────┘
       └────────┬────────┘
                ↓
┌──────────────────────────────┐
│     Anomaly Identification   │
│  Identify unusual patterns   │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│     Explainable Results      │
│  Indicators behind anomaly   │
│  detection are presented     │
└──────────────────────────────┘

Module Description

1. Data Preparation

Transaction records are prepared for analysis by organizing wallet addresses, transaction amounts, timestamps, and related attributes.

2. Transaction Graph

The transaction network is represented as a directed graph where wallets are nodes and transfers are edges.

3. Behavioural Analysis

Transaction behaviour is examined using indicators such as frequency, movement patterns, and unusual connectivity.

4. Graph Analysis

Graph metrics such as degree centrality and betweenness centrality are used to characterize wallet positions within the network.

5. Statistical Detection

Z-score and IQR-based methods can be used to identify statistically unusual observations.

6. Explainable Results

Instead of providing only an anomaly label, the framework aims to provide interpretable indicators associated with the detected behaviour.

Framework Objective

The overall objective is to combine graph analysis + statistical anomaly detection + explainability into a transparent cryptocurrency AML research framework.
