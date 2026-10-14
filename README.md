# Sales Performance Dashboard (Excel / Power BI)

An interactive KPI dashboard that tracks sales, profit and margin so trends and problem areas can be spotted quickly.

> **About the data:** the 1,500 orders (FY2025) are **synthetic**, produced by `scripts/generate_data.py` with a fixed random seed. They are for portfolio demonstration and do not come from any real company.

## What's inside

| File | Purpose |
|---|---|
| `Sales_Performance_Dashboard.xlsx` | Dashboard sheet (KPI tiles, 4 charts, summary tables) + Data sheet. Every number is a live formula (`SUMIFS`, `COUNTIFS`, `INDEX/MATCH`), so edits to the Data sheet flow through. |
| `data/sales_data.csv` | The same dataset as a flat file, ready to load into Power BI, Python or SQL. |
| `scripts/generate_data.py` | Reproducible generator for the dataset. |

## Metrics

- **Revenue** = Units x Unit Price x (1 - Discount)
- **Profit** = Revenue - Units x Unit Cost
- **Margin** = Profit / Revenue

## What the dashboard shows

- **Electronics drives 49% of revenue but earns only a 19% margin**, versus about 38-39% for Furniture and Office Supplies.
- **Deeper discounts erode margin:** orders with no discount earn a 33.4% margin; orders at 20% off earn 20.7%. Orders discounted 15% or more make up about 24% of revenue.
- **Seasonality:** November and December together bring in 22.9% of annual revenue (an even split would be 16.7%).
- **Regions:** West is the largest region ($258K) but has the lowest margin (27.7%); North has the highest (29.6%).
- **Channels:** Retail has the best margin (about 31%); Distributor the lowest (about 27%), driven by heavier discounts.

## Using the workbook

1. Open `Sales_Performance_Dashboard.xlsx` and go to the **Dashboard** sheet.
2. To test a scenario, change `Units`, `Unit Price`, `Unit Cost` or `Discount` on the **Data** sheet; Revenue, Cost, Profit and every dashboard figure update automatically.

## Rebuilding it in Power BI

1. **Get Data > Text/CSV** and load `data/sales_data.csv`.
2. Create measures: `Total Revenue = SUM(sales_data[Revenue])`, `Total Profit = SUM(sales_data[Profit])`, `Margin % = DIVIDE([Total Profit], [Total Revenue])`.
3. Add cards for the three measures, a line chart (Order Date by month), clustered bars by Region / Category, and slicers for Region, Channel and Category.

## Possible next steps

Add year-over-year comparison, a forecast for the next quarter, and customer-level segmentation.
