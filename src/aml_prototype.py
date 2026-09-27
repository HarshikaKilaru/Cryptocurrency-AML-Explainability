import pandas as pd
import networkx as nx

# Sample cryptocurrency transaction data
transactions = pd.DataFrame({
    "sender": ["W1", "W1", "W2", "W3", "W4", "W4", "W5", "W6"],
    "receiver": ["W2", "W3", "W3", "W4", "W5", "W6", "W7", "W7"],
    "amount": [100, 50, 75, 120, 40, 300, 25, 60]
})

# Create a directed transaction graph
G = nx.DiGraph()

for _, transaction in transactions.iterrows():
    G.add_edge(
        transaction["sender"],
        transaction["receiver"],
        weight=transaction["amount"]
    )

# Calculate degree for each wallet
degree = dict(G.degree())

degree_df = pd.DataFrame(
    degree.items(),
    columns=["wallet", "degree"]
)

# Calculate Z-score
mean_degree = degree_df["degree"].mean()
std_degree = degree_df["degree"].std()

if std_degree != 0:
    degree_df["z_score"] = (
        degree_df["degree"] - mean_degree
    ) / std_degree
else:
    degree_df["z_score"] = 0

# Flag potential anomalies
degree_df["potential_anomaly"] = (
    degree_df["z_score"].abs() > 2
)

print("Wallet Analysis")
print(degree_df)

print("\nPotentially anomalous wallets:")
print(
    degree_df[
        degree_df["potential_anomaly"]
    ]
)
