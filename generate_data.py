"""Generate the synthetic sales dataset used by the dashboard.

All figures are randomly generated (seeded, so reproducible) for portfolio
demonstration. They do not come from any real company.
"""
import csv
import random
from datetime import date

random.seed(42)
N_ORDERS = 1500
YEAR = 2025

# (category, product, list price, unit cost, popularity weight, max units)
PRODUCTS = [
    ("Electronics", "Laptop", 780, 600, 3, 3),
    ("Electronics", "Smartphone", 520, 415, 4, 4),
    ("Electronics", "Headphones", 90, 58, 6, 6),
    ("Furniture", "Office Chair", 150, 82, 4, 4),
    ("Furniture", "Standing Desk", 320, 185, 2, 3),
    ("Furniture", "Bookshelf", 110, 62, 3, 4),
    ("Office Supplies", "Printer Paper (carton)", 28, 17, 6, 40),
    ("Office Supplies", "Notebook Pack", 12, 6, 7, 40),
    ("Office Supplies", "Pen Set", 9, 4.5, 7, 40),
]
REGIONS = (["West", "North", "South", "East"], [0.30, 0.28, 0.25, 0.17])
CHANNELS = {  # channel: (share, discount options, discount weights, unit multiplier)
    "Online": (0.45, [0, 0.05, 0.10, 0.15], [0.30, 0.30, 0.25, 0.15], 1),
    "Retail": (0.35, [0, 0.05, 0.10], [0.50, 0.30, 0.20], 1),
    "Distributor": (0.20, [0.10, 0.15, 0.20], [0.30, 0.40, 0.30], 3),
}
MONTH_WEIGHTS = [0.8, 0.8, 0.9, 0.95, 1.0, 1.0, 0.95, 1.0, 1.05, 1.1, 1.4, 1.6]

rows = []
for _ in range(N_ORDERS):
    month = random.choices(range(1, 13), MONTH_WEIGHTS)[0]
    d = date(YEAR, month, random.randint(1, 28))
    region = random.choices(*REGIONS)[0]
    channel = random.choices(list(CHANNELS), [c[0] for c in CHANNELS.values()])[0]
    _, disc_opts, disc_w, mult = CHANNELS[channel]
    cat, prod, price, cost, _, max_u = random.choices(PRODUCTS, [p[4] for p in PRODUCTS])[0]
    units = random.randint(1, max_u) * (mult if max_u > 4 else 1)
    discount = random.choices(disc_opts, disc_w)[0]
    rows.append([d, region, cat, prod, channel, units, price, cost, discount])

rows.sort(key=lambda r: r[0])
with open("data/sales_data.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Order ID", "Order Date", "Region", "Category", "Product", "Channel",
                "Units", "Unit Price", "Unit Cost", "Discount", "Revenue", "Cost", "Profit"])
    for i, (d, region, cat, prod, channel, units, price, cost, disc) in enumerate(rows, 1):
        revenue = round(units * price * (1 - disc), 2)
        total_cost = round(units * cost, 2)
        w.writerow([f"ORD-{i:04d}", d.isoformat(), region, cat, prod, channel, units,
                    price, cost, disc, revenue, total_cost, round(revenue - total_cost, 2)])
print("Wrote", len(rows), "rows")
