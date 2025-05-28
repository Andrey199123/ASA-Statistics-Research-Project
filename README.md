# Instacart Order Behavior Analysis

This project uses Python to analyze the Instacart Market Basket Analysis dataset, focusing on the distribution of order times by department. By applying the Kruskal–Wallis H-test, this research identifies statistically significant differences in the average hour products are ordered across departments. The goal is to uncover consumer behavior trends that can inform dynamic pricing strategies for online grocery platforms.

## Key Questions

- Do different departments have significantly different order time distributions?
- When is the best time of day to raise prices for certain product categories like frozen foods or beverages?

## Statistical Methodology

The analysis includes:
- Non-parametric hypothesis testing (Kruskal–Wallis) due to unequal variances between departments
- Ranking order times, computing department-level mean ranks, and evaluating their contributions to the test statistic
- Visualization of average order hour and product-level trends to support pricing strategy decisions

## Project Structure

| File                  | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `final_test.py`       | Runs the full Kruskal–Wallis test, computes rank contributions, and outputs table visualizations |
| `mean_hour.py`        | Computes and visualizes the average order hour per department               |
| `order_by_hour.py`    | Visualizes order frequency across different hours of the day                |
| `rank.py`             | Ranks all order hours and computes department-level rank averages           |
| `visualize.py`        | Generates matplotlib tables for statistical summaries                       |
| `visualize_aisles.py` | Analyzes and visualizes order time patterns at the aisle level              |

## Dataset

Instacart Market Basket Analysis  
The data can be found here: https://www.kaggle.com/datasets/yasserh/instacart-online-grocery-basket-analysis-dataset
## Requirements

Make sure to download the following CSVs and place them in your working directory:

- `orders_with_department.csv`
- `products.csv`
- `departments.csv`
- `aisles.csv`
- `order_products_prior.csv`

```bash
pip install pandas matplotlib scipy
