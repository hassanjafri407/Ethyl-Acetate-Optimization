# Ethyl Acetate Production Process Optimization Using Aspen Plus and Python

## Overview

This project presents the simulation, heat integration, and optimization of an industrial ethyl acetate production process using Aspen Plus and Python. Aspen Plus is used to model the chemical process, while Python automates sensitivity studies, performs economic calculations, exports simulation data, and generates publication-quality plots.

The objective of the project is to determine operating conditions that maximize ethyl acetate purity while minimizing energy consumption and annual utility cost.

---

## Process Description

The simulated process consists of:

- Feed mixing
- RCSTR reactor
- Heat exchanger for heat integration
- Flash separator
- RadFrac distillation column
- Product purification

Heat integration is incorporated to reduce external heating requirements and improve overall energy efficiency.

---

## Reaction Kinetics

The reactor models the esterification reaction:

CH₃COOH + C₂H₅OH ⇌ CH₃COOC₂H₅ + H₂O

The kinetic parameters (pre-exponential factor **A₁** and activation energy **E₁**) used in the RCSTR model were obtained from:

> Atalay, F. S. (1994). *Kinetics of the Esterification Reaction Between Ethanol and Acetic Acid*. Developments in Chemical Engineering and Mineral Processing.

The Aspen Plus model assumes the reaction is catalyzed using **1.91 wt% sulfuric acid (H₂SO₄)**, and the corresponding kinetic parameters reported for this catalyst concentration were implemented in the reactor model.

---

## Project Objectives

- Simulate an industrial ethyl acetate production process
- Implement heat integration to reduce utility demand
- Automate Aspen Plus using Python
- Study the effect of:
  - Operating pressure
  - Distillation reflux ratio
  - Ethanol-to-acetic acid feed ratio
- Evaluate energy consumption
- Estimate annual utility cost
- Identify optimum operating conditions

---

## Optimization Studies

### Pressure Study

- Pressure vs Product Purity
- Pressure vs Total Energy Consumption
- Pressure vs Annual Utility Cost

### Reflux Ratio Study

- Reflux Ratio vs Product Purity
- Reflux Ratio vs Reboiler Duty
- Reflux Ratio vs Condenser Duty
- Reflux Ratio vs Annual Utility Cost

### Feed Ratio Study

- Feed Ratio vs Conversion
- Feed Ratio vs Product Purity
- Feed Ratio vs Annual Utility Cost

### Final Optimization

- Product Purity vs Annual Utility Cost

---

## Economic Analysis

The economic analysis estimates annual utility costs based on Aspen Plus simulation results and is intended for comparison of operating conditions rather than a complete plant economic evaluation.

### Assumptions

- Only utility operating costs were considered.
- Annual utility cost was estimated from the reboiler and condenser heat duties obtained from Aspen Plus.
- A plant operating time of 8,000 hours per year was assumed.
- Utility prices were assumed to remain constant throughout the analysis.
- Equipment purchase cost, installation cost, maintenance, depreciation, labour, taxes, and raw material costs were not included.
- Capital investment and equipment sizing were outside the scope of this study.
- Heat integration was evaluated based on reductions in utility demand rather than detailed exchanger network optimization.
- The economic analysis is intended for relative comparison between operating conditions rather than absolute estimation of industrial production costs.

Steam cost: $15/GJ
Cooling water cost: $0.5/GJ
Operating time: 8,000 h/year

The economic analysis is therefore intended for **relative comparison between operating conditions** rather than prediction of the total cost of an industrial plant.

---

## Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Required libraries:

- pandas
- numpy
- matplotlib
- pywin32

Additional software:

- Aspen Plus V14 (or compatible version)
- Python 3.x

---

## Technologies Used

- Aspen Plus
- Python
- Pandas
- NumPy
- Matplotlib
- pywin32

---

## Results

Python automation was used to perform multiple Aspen Plus sensitivity studies and automatically export simulation results. The project evaluates the effect of pressure, reflux ratio, and feed composition on:

- Ethyl acetate purity
- Conversion
- Reboiler duty
- Condenser duty
- Total energy consumption
- Annual utility cost

The final optimization compares purity against annual utility cost to identify the most favorable operating conditions.

---

## References

Atalay, F. S. (1994). *Kinetics of the Esterification Reaction Between Ethanol and Acetic Acid*. Developments in Chemical Engineering and Mineral Processing.
