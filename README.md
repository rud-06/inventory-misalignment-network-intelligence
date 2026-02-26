Inventory Misalignment & Network Intelligence System
<div align="center">
A Multi-Dimensional Supply Chain Intelligence Engine

Detecting Stockout Risk, Phantom Inventory, Demand Decay, Behavioral Nervousness & Network-Level Economic Friction

<img src="https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Apache_Parquet-Optimized-orange.svg?style=for-the-badge&logo=apache&logoColor=white"> <img src="https://img.shields.io/badge/Power_BI-Executive_Dashboard-yellow.svg?style=for-the-badge&logo=powerbi&logoColor=black"> </div>

🔎 Executive Summary

In high‑velocity FMCG retail environments, inventory distortion silently erodes 2–5% of annual revenue through localized stockouts, phantom availability, demand decay, and behavioral replenishment inefficiencies.

A retail network can report 97% service levels while still bleeding material margin in the statistical tail.

This system processes 4.5+ million rows of hourly-resolution sales and stock data across an 897-store network to isolate, quantify, and prescribe action on structural supply chain friction.
🚀 Quantified Impact
Metric	Value	Insight
Data Processed	4.5M Rows	Hour-level resolution (19 variables)
Gross Revenue at Risk	$112,931	Theoretical loss before substitution
Net Revenue at Risk	~$65K	True loss after elasticity modeling
Substitution Recovery	42%	Structural revenue migration captured
Passive Neglect Stores	30.7%	Behavioral replenishment inefficiency
🧠 System Architecture

Each module converts theoretical supply chain distortion into a revenue-denominated decision variable.

⚙️ Core Analytical Modules

1️⃣ Demand‑Weighted Service (DWS)

Traditional Hourly Service Rate (HSR) treats a 3:00 AM stockout the same as a 6:00 PM Friday stockout.
DWS filled with 1 for zero-demand days.
We engineered a Demand‑Weighted Service metric:
Revenue_at_Risk=Sale_Amount×(1−DWS)
Revenue_at_Risk=Sale_Amount×(1−DWS)

This isolates economically meaningful downtime from overnight noise.

2️⃣ Revenue at Risk Engine

Separates perceived stockouts from financially material impact.
Forms the backbone for all downstream optimization.

3️⃣ Phantom Inventory Detection

Identifies invisible stock failures where:

    HSR > 0.80

    Zero recorded demand

    Positive expected demand (7-day rolling mean)

Captures operational distortion such as theft, misplacement, or WMS inconsistencies.

4️⃣ Velocity Divergence Modeling

Short vs medium-term rolling means:

    7-Day vs 30-Day demand comparison

    Velocity ratio classification

    Revenue exposure from declining SKUs

Adds predictive markdown intelligence and lifecycle diagnostics.

5️⃣ Supply Chain Nervousness (Bullwhip Index)
Nervousness=Inventory CVDemand CV
Nervousness=Demand CVInventory CV​

Behavioral Classification:

    > 1.5 → Panic / Over-Reactive

    < 0.5 → Passive / Neglect

    ≈ 1 → Synchronized

Bridges quantitative analytics with behavioral operations research.

6️⃣ Substitution Elasticity Engine

Aggregates surplus demand at category-store level to estimate revenue migration.

Outputs:

    Gross Revenue at Risk

    Net Revenue at Risk

    42% recoverable loss identified

Transforms alarmist stockout metrics into economically calibrated loss estimates.

7️⃣ Composite Store Risk Index

Multi-factor normalized scoring:

    Service Risk

    Decay Risk

    Markdown Risk

    Phantom Risk

Stores classified into quartile & absolute risk tiers for prioritized intervention.

8️⃣ Network Transshipment Optimizer

Identifies intra-city SKU rebalancing opportunities using:

    Net Revenue at Risk thresholds

    Velocity screening

    Transport cost adjustments

Generates prescriptive lateral inventory transfers ranked by economic value.

9️⃣ Economic Friction Frontier
Total Economic Drag=Cost_of_Waste+Cost_of_Wait
Total Economic Drag=Cost_of_Waste+Cost_of_Wait

Maps SKU-level tradeoffs:

    Cost of Waste → Capital trapped in slow-moving stock

    Cost of Wait → Margin lost due to demand-weighted stockouts

Upper-right quadrant SKUs trigger immediate P1 operational action.
🗄️ Data Architecture & Engineering

To avoid a 100M+ row relational explosion, the system leverages Apache Parquet array compression:

    hours_sale → 24-element vector

    hours_stock_status → 24-element vector

This enables vectorized NumPy transformations while preserving memory efficiency.
📊 Visualization Layer

Python outputs serve as the semantic layer for a 4-page Power BI dashboard suite featuring:

    Store Risk Matrix

    True vs Fake Risk Waterfall

    Nervousness Split

    Economic Friction Scatter

    Network Transfer Map

Designed for executive-level decision clarity.
🛠 Technology Stack

    Python 3.10+

    pandas / numpy

    scikit-learn (MinMaxScaler)

    Rolling Window Time-Series Modeling

    Coefficient of Variation Diagnostics

    Apache Parquet

    Microsoft Power BI (DAX, Power Query)

    Google Colab / Jupyter

📈 Key Contributions

    Replaced aggregate service metrics with demand-weighted precision modeling

    Quantified substitution elasticity at network scale

    Integrated bullwhip diagnostics with revenue attribution

    Converted descriptive analytics into prescriptive transshipment optimization

    Built a composite risk scoring engine for 897 stores

🎯 Applications

    FMCG Retail Networks

    Multi-Location Inventory Systems

    Supply Chain Risk Monitoring

    Working Capital Optimization

    Retail Operations Research

    Network Rebalancing & Capital Efficiency

👥 Authors

Rudra Ray, Ashmit Sinha

Jadavpur University (B.E.)

📌 Note

Raw dataset excluded due to size constraints.
Code and derived outputs included.
Dataset available upon academic request.
