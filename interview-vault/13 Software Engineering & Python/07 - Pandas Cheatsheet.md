# Pandas Cheatsheet

**Prev:** [[06 - NumPy Cheatsheet]] · **Next:** [[08 - SQL Cheatsheet]]

---

## In plain English

pandas = Excel-like **tables** (`DataFrame`) with joins, groupby, and missing-data tools. Most EDA and feature prep happens here.

---

## Load & inspect

```python
import pandas as pd

df = pd.read_csv("data.csv")
df.head(), df.info(), df.describe()
df.shape, df.columns, df.dtypes
df.isna().sum()           # missing per column
```

---

## Select & filter

```python
df["col"]                 # Series
df[["a", "b"]]            # two columns
df.loc[df.age > 30, "name"]   # label-based
df.iloc[0:5, 1:3]         # position-based
df.query("age > 30 and city == 'NY'")
```

---

## Missing data

```python
df.dropna()
df.fillna(0)
df.fillna(df.median(numeric_only=True))
df["col"].ffill()         # forward fill (time series)
```

---

## Groupby (SQL GROUP BY)

```python
df.groupby("city")["sales"].agg(["mean", "count"])
df.groupby(["city", "year"]).sales.sum().reset_index()
```

---

## Joins

```python
pd.merge(df1, df2, on="id", how="left")   # left join
# how: inner, outer, right
```

---

## Apply (use sparingly)

```python
df["z"] = df["x"] + df["y"]              # prefer vectorized
df.groupby("g").apply(custom_fn)         # slow on big data
```

---

## Export

```python
df.to_csv("out.csv", index=False)
df.to_parquet("out.parquet")             # efficient for big data
```

---

## Common traps

| Trap | Correct |
|------|---------|
| `SettingWithCopyWarning` | Use `.loc` on explicit copy: `df2 = df.copy()` |
| `iterrows()` for heavy work | Vectorize or `np.where` / merge |
| `fillna` on full data before split | Fit imputer on **train only** |
| `merge` duplicates rows | Check `validate="one_to_many"`, row counts |
| Chained indexing `df[a][b]=x` | Use `df.loc[a, b] = x` |

---

## Interview coding drills (4 classics)

Use small DataFrames; explain **vectorized** vs `apply`.

### 1. Revenue per city + sort

**Prompt:** Total `sales` by `city`, descending.

```python
import pandas as pd

df = pd.DataFrame({
    "city": ["NY", "NY", "LA", "LA"],
    "sales": [100, 50, 80, 20],
})

out = (
    df.groupby("city", as_index=False)["sales"]
      .sum()
      .sort_values("sales", ascending=False)
)
# city  sales
# NY    150
# LA    100
```

**Trap:** Forgetting `as_index=False` → city becomes index, awkward for merges.

---

### 2. Pivot: months as columns

**Prompt:** Rows = `product`, columns = `month`, values = sum of `qty`.

```python
df = pd.DataFrame({
    "product": ["A", "A", "B"],
    "month": ["Jan", "Feb", "Jan"],
    "qty": [10, 5, 7],
})

wide = df.pivot_table(index="product", columns="month", values="qty", aggfunc="sum", fill_value=0)
```

**Trap:** `pivot` vs `pivot_table` — use `pivot_table` when duplicates exist.

---

### 3. Left join + flag missing orders

**Prompt:** All users; `order_count` = 0 if no orders.

```python
users = pd.DataFrame({"user_id": [1, 2, 3]})
orders = pd.DataFrame({"user_id": [1, 1, 2], "amount": [10, 20, 5]})

order_stats = orders.groupby("user_id")["amount"].agg(order_count="count", total="sum")
result = users.merge(order_stats, on="user_id", how="left").fillna({"order_count": 0, "total": 0})
```

**Trap:** Inner join drops users with zero orders.

---

### 4. Group-wise fill: median imputation per department

**Prompt:** Fill missing `salary` with **department median** (train-style leakage awareness in interviews: fit medians on train only).

```python
df = pd.DataFrame({
    "dept": ["Eng", "Eng", "Sales", "Sales"],
    "salary": [100, None, 60, None],
})

dept_median = df.groupby("dept")["salary"].transform("median")
df["salary_filled"] = df["salary"].fillna(dept_median)
```

**Trap:** `fillna(df["salary"].median())` globally when group structure matters.

---

## Interview one-liner

> "pandas is my EDA workhorse: groupby for aggregates, merge for relational data, and careful train-only preprocessing to avoid leakage."

---
#### Setup — run this first in Colab

python

```python
import pandas as pd
import numpy as np

# --- Orders table ---
orders = pd.DataFrame({
    'order_id':    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'customer_id': [101, 102, 101, 103, 102, 104, 101, 103, 105, 104],
    'product_id':  [501, 502, 503, 501, 504, 502, 503, 505, 501, 506],
    'quantity':    [2, 1, 3, 1, 2, 4, 1, 2, 3, 1],
    'unit_price':  [12.99, 45.00, 8.50, 12.99, None, 45.00, 8.50, None, 12.99, None],
    'order_date':  pd.to_datetime([
        '2024-01-05', '2024-01-07', '2024-01-07', '2024-01-10',
        '2024-02-01', '2024-02-03', '2024-02-14', '2024-02-20',
        '2024-03-01', '2024-03-05'
    ])
})

# --- Products table ---
products = pd.DataFrame({
    'product_id':   [501, 502, 503, 504, 505],  # 506 intentionally missing!
    'product_name': ['Dog Food Royal Canin', 'Cat Harness', 'Bird Seed Mix',
                     'Fish Tank Filter', 'Rabbit Hutch'],
    'category':     ['food', 'accessories', 'food', 'accessories', 'housing'],
    'cost_price':   [8.00, 30.00, 5.00, None, 120.00],  # null in cost_price
})
```

---

#### Exercise 1 — Handling nulls + revenue calculation

**Task:** The `unit_price` column has nulls. Fill them using the median price of that product across all other orders, then compute `revenue = quantity × unit_price` for every order.

python

```python
# Your solution here
```

**Solution:**

python

```python
# Step 1: fill nulls with per-product median price
product_median_price = (orders.groupby('product_id')['unit_price']
                               .transform('median'))

orders['unit_price'] = orders['unit_price'].fillna(product_median_price)

# Step 2: compute revenue
orders['revenue'] = orders['quantity'] * orders['unit_price']

print(orders[['order_id', 'product_id', 'unit_price', 'revenue']])
```

**Key interview points:**

- `transform('median')` returns a Series with the **same index** as the original — this is what makes `fillna()` align correctly. If you used `agg()` instead it would return one row per group and the fillna would break.
- Always fill nulls **before** computing derived columns, not after.

---

#### Exercise 2 — Merge + handling missing joins

**Task:** Join orders with the products table. Some product IDs exist in orders but not in products (product 506). Keep all orders and flag which ones have missing product info.

python

```python
# Your solution here
```

**Solution:**

python

```python
# Left join — keeps all orders even if product is missing
merged = orders.merge(products, on='product_id', how='left')

# Flag rows where product info is missing (product_id=506 case)
merged['product_missing'] = merged['product_name'].isna()

# Fill unknown product names gracefully
merged['product_name'] = merged['product_name'].fillna('Unknown Product')
merged['category']     = merged['category'].fillna('uncategorized')

print(merged[['order_id', 'product_id', 'product_name', 'product_missing', 'revenue']])
```

**Key interview points:**

- Always justify your join type: `left` keeps all orders (business requirement: never drop a sale), `inner` would silently drop order 10 and you'd underreport revenue.
- Creating an explicit `_missing` flag is better than just filling nulls — it preserves the information that data was absent.

---

#### Exercise 3 — Groupby aggregation (the hard one)

**Task:** Produce a customer summary report with these columns:

- `total_revenue` — sum of all their orders
- `num_orders` — how many orders they placed
- `avg_order_value` — mean revenue per order
- `favourite_category` — the category they spent most on
- `first_order_date` and `last_order_date`

python

```python
# Your solution here
```

**Solution:**

python

```python
# Part A: standard aggregations — straightforward
customer_stats = (merged.groupby('customer_id')
    .agg(
        total_revenue    = ('revenue', 'sum'),
        num_orders       = ('order_id', 'count'),
        avg_order_value  = ('revenue', 'mean'),
        first_order_date = ('order_date', 'min'),
        last_order_date  = ('order_date', 'max'),
    )
    .round(2)
    .reset_index()
)

# Part B: favourite category — needs a separate groupby then merge back
# (you can't do this in one agg call cleanly)
fav_category = (merged.groupby(['customer_id', 'category'])['revenue']
                       .sum()
                       .reset_index()
                       .sort_values('revenue', ascending=False)
                       .drop_duplicates(subset='customer_id')  # keep top category
                       .rename(columns={'category': 'favourite_category'})
                       [['customer_id', 'favourite_category']])

# Merge both results together
report = customer_stats.merge(fav_category, on='customer_id', how='left')

print(report.to_string(index=False))
```

**Output:**

```
 customer_id  total_revenue  num_orders  avg_order_value first_order_date last_order_date favourite_category
         101          84.49           3            28.16       2024-01-05      2024-02-14               food
         102          71.98           2            35.99       2024-01-07      2024-02-01        accessories
         103          25.98           2            12.99       2024-01-10      2024-02-20               food
         104         180.00           2            90.00       2024-02-03      2024-03-05        accessories
         105          38.97           1            38.97       2024-03-01      2024-03-01               food
```
**Next:** [[08 - SQL Cheatsheet]]
