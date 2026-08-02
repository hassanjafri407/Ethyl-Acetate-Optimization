import win32com.client as win32
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path

from economic_analysis import annual_utility_cost
from economic_analysis import total_energy

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR.parent / "aspen-model" / "ethyl-acetate-optimization - heat integration.bkp"

aspen = win32.Dispatch("Apwn.Document")
aspen.InitFromArchive2(str(MODEL_PATH))

aspen.Tree.FindNode(
    r"\Data\Blocks\RADFRAC1\Input\BASIS_RR"
).Value = 2.0

aspen.Tree.FindNode(
    r"\Data\Streams\ETH-ACE\Input\FLOW\MIXED\ETHANOL"
).Value = 50

aspen.Tree.FindNode(
    r"\Data\Streams\ETH-ACE\Input\FLOW\MIXED\ACETI-01"
).Value = 50

aspen.Engine.Run2()

pressure_values = np.arange(1.0, 5.5, 0.5)

results = []

for pressure in pressure_values:

    print(f"Running {pressure:.1f} bar")


    aspen.Tree.FindNode(
        r"\Data\Blocks\RADFRAC1\Input\PRES1"
    ).Value = pressure

    aspen.Engine.Run2()


    purity = aspen.Tree.FindNode(
        r"\Data\Streams\LIQ-DIST\Output\MOLEFRAC\MIXED\ETHYL-01"
    ).Value

    condenser = aspen.Tree.FindNode(
        r"\Data\Blocks\RADFRAC1\Output\COND_DUTY"
    ).Value

    reboiler = aspen.Tree.FindNode(
        r"\Data\Blocks\RADFRAC1\Output\REB_DUTY"
    ).Value
    
    cost = annual_utility_cost(        
    condenser,
    reboiler)

    energy = total_energy(
    condenser,
    reboiler)

    results.append([
    pressure,
    purity,
    condenser,
    reboiler,
    energy,
    cost])

    df = pd.DataFrame(
    results,columns=[
        "Pressure (bar)",
        "Purity",
        "Condenser Duty",
        "Reboiler Duty",
        "Total Energy",
        "Annual Utility Cost"
    ]
)

ROOT_DIR = BASE_DIR.parent

DATA_DIR = ROOT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

df.to_csv(DATA_DIR / "pressure_results.csv", index=False)

plt.figure(figsize=(8,5))

plt.plot(
    df["Pressure (bar)"],
    df["Purity"],
    marker="o",
    linewidth=2
)

plt.xlabel("Pressure (bar)")
plt.ylabel("Ethyl Acetate Purity")
plt.title("Pressure vs Purity")

plt.grid(True)

plt.figure(figsize=(8,5))

plt.plot(
    df["Pressure (bar)"],
    df["Annual Utility Cost"],
    marker="o",
    linewidth=2
)

plt.xlabel("Pressure (bar)")
plt.ylabel("Annual Utility Cost ($/yr)")
plt.title("Pressure vs Annual Utility Cost")

plt.grid(True)

plt.figure(figsize=(8,5))

plt.plot(
    df["Pressure (bar)"],
    df["Total Energy"],
    marker="o",
    linewidth=2
)

plt.xlabel("Pressure (bar)")
plt.ylabel("Total Energy (Gcal/hr)")
plt.title("Pressure vs Total Energy Consumption")

plt.grid(True)

plt.show()

aspen.Close()
del aspen