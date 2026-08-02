import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

DATA_DIR = ROOT_DIR / "data"

pressure_df = pd.read_csv(DATA_DIR / "pressure_results.csv")
rr_df = pd.read_csv(DATA_DIR / "rr_results.csv")
feed_df = pd.read_csv(DATA_DIR / "ratio_results.csv")

plt.figure(figsize=(8,6))

plt.scatter(
    pressure_df["Purity"],
    pressure_df["Annual Utility Cost"],
    label="Pressure Study"
)

plt.scatter(
    rr_df["Purity"],
    rr_df["Annual Utility Cost"],
    label="Reflux Ratio Study"
)

plt.scatter(
    feed_df["Purity"],
    feed_df["Annual Utility Cost"],
    label="Feed Ratio Study"
)

plt.xlabel("Ethyl Acetate Purity")
plt.ylabel("Annual Utility Cost ($/year)")
plt.title("Purity vs Annual Utility Cost")
plt.legend()
plt.grid(True)

plt.show()