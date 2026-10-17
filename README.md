# Inter-Annotator Agreement (IAA) Calculator

## 📌 Project Overview
In AI and Machine Learning data pipelines, data quality is paramount. This repository provides a lightweight Python utility to calculate **Cohen's Kappa score**, a statistical metric used to measure the level of agreement between two independent annotators who classify datasets. 

This tool serves to help QA leads and Data Project Managers monitor grading rubric alignment and detect ambiguity in annotation guidelines.

## 🛠️ Features
*   Calculates **Observed Agreement ($P_o$)** and **Chance Agreement ($P_e$)**.
*   Outputs a precise **Cohen's Kappa score**.
*   Categorizes results based on standard data reliability metrics (from Slight to Almost Perfect agreement).

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the directory:
   ```bash
   cd inter-annotator-agreement-calculator
   ```
3. Run the script:
   ```bash
   python calculator.py
   ```
