# 🧠 2-Week Learning Plan for NumPy & Pandas (2 Hours/Day)

> **Goal:** Learn NumPy and Pandas simultaneously in 2 weeks with daily 2-hour sessions.

---

## 📅 Week 1: Foundations & Core Operations

### ✅ Day 1 – NumPy + Pandas Intro
- 📌 What is NumPy and Pandas? Why use them?
- 🧮 NumPy: Create arrays using `array`, `zeros`, `ones`, `arange`, `linspace`
- 📊 Pandas: Create Series & DataFrame from dict/list
- 📝 Practice: Explore small datasets using `head()`, `info()`

---

### ✅ Day 2 – Indexing & Slicing
- 🧮 NumPy: Indexing, slicing, Boolean filtering
- 📊 Pandas: Access rows/columns using `loc`, `iloc`
- 📝 Practice: Extract subsets of data

---

### ✅ Day 3 – Math & Vectorized Operations
- 🧮 NumPy: Element-wise operations, broadcasting
- 📊 Pandas: Column operations (add, subtract, transform)
- 📝 Practice: Calculate new columns like BMI, total price, etc.

---

### ✅ Day 4 – Aggregation & Summary Stats
- 🧮 NumPy: `mean()`, `sum()`, `std()`, `max()`, `min()`
- 📊 Pandas: `describe()`, `groupby()`, `agg()`
- 📝 Practice: Analyze and group data (e.g., sales by region)

---

### ✅ Day 5 – Data Cleaning Basics
- 🧮 NumPy: Use `np.where`, `np.isnan`, `np.nan`
- 📊 Pandas: `isnull()`, `fillna()`, `dropna()`, `astype()`
- 📝 Practice: Clean messy dataset (missing values, wrong types)

---

### ✅ Day 6 – Reshaping & Sorting
- 🧮 NumPy: `reshape()`, `ravel()`, `transpose()`
- 📊 Pandas: `sort_values()`, `sort_index()`, `reset_index()`
- 📝 Practice: Organize and reformat data

---

### ✅ Day 7 – Review + Mini Project
- 🔁 Review all concepts so far
- 🧪 Mini Project: Load a dataset (e.g., student marks, products), clean it, and do basic stats
- 📈 Use NumPy for calculations & Pandas for data analysis

---

## 📅 Week 2: Intermediate Features & Real-World Practice

### ✅ Day 8 – Combining & Joining Data
- 🧮 NumPy: `concatenate()`, `stack()`
- 📊 Pandas: `merge()`, `concat()`, `join()`
- 📝 Practice: Combine multiple datasets (e.g., users + transactions)

---

### ✅ Day 9 – Advanced Filtering & Logic
- 🧮 NumPy: Advanced Boolean filtering with multiple conditions
- 📊 Pandas: Filter rows using complex conditions
- 📝 Practice: Filter high/low-performing entries

---

### ✅ Day 10 – Custom Functions & Apply
- 📊 Pandas: Use `apply()`, `map()`, `lambda` for column-wise operations
- 🧮 NumPy: Use `vectorize()` for custom ops
- 📝 Practice: Apply functions to transform data

---

### ✅ Day 11 – Pivoting & Reshaping
- 📊 Pandas: `pivot_table()`, `melt()`, `stack()/unstack()`
- 🧮 NumPy: Work with multi-dimensional reshaping
- 📝 Practice: Create pivot tables for sales/metrics analysis

---

### ✅ Day 12 – Handling Time & Text Data
- 📊 Pandas: `to_datetime()`, `.dt`, string operations (`.str`)
- 🧮 NumPy: Optional practice with `datetime64`
- 📝 Practice: Analyze time series or clean text columns

---

### ✅ Day 13 – Real-World Project
- 🎯 Choose a dataset (e.g., Titanic, Superstore, COVID-19)
- ✅ Clean, analyze, group, and visualize data
- 💡 Use both NumPy and Pandas throughout

---

### ✅ Day 14 – Final Review + Practice
- 🔁 Go over tricky topics (GroupBy, Apply, Reshape)
- 📊 Optional: Try a new dataset
- 🏁 Goal: Feel confident to explore and analyze new data on your own!

---

## ✅ Optional Resources
- Datasets: [Kaggle](https://www.kaggle.com/datasets), [UCI ML Repo](https://archive.ics.uci.edu/ml/index.php)
- Practice: [numpy.org](https://numpy.org), [pandas.pydata.org](https://pandas.pydata.org)
- Books: *Python for Data Analysis* by Wes McKinney

---

## 📦 Real-World Projects (with Dataset Links & Tasks)

> Use these small projects to apply both **NumPy** and **Pandas** skills.

---

### ✅ Project 1: 🛍️ Superstore Sales Analysis
- **Dataset Link:** [Download from Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Skills Used:** Pandas (`groupby`, `merge`, `pivot_table`), NumPy stats
- **What to Do:**
  - Clean missing values
  - Analyze total sales, profit by region/category
  - Find top-selling products
  - Use `groupby()` to analyze trends
  - Bonus: Use `pivot_table()` for summary dashboard

---

### ✅ Project 2: 🚢 Titanic Survival Analysis
- **Dataset Link:** [Download from Kaggle](https://www.kaggle.com/competitions/titanic/data)
- **Skills Used:** Filtering, `isnull()`, `fillna()`, `apply()`, boolean logic
- **What to Do:**
  - Clean missing `Age`, `Cabin`, `Embarked`
  - Analyze survival rates by gender, class, age group
  - Use `apply()` to create new feature like “child” or “elderly”
  - Bonus: Find correlation between fare and survival

---

### ✅ Project 3: 🌍 World Population Data
- **Dataset Link:** [Download from Kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset)
- **Skills Used:** Sorting, filtering, NumPy math, custom functions
- **What to Do:**
  - Sort countries by population
  - Calculate population growth %
  - Filter countries with low/high density
  - Group by continent and get average population

---

### 💡 Tips for Projects
- Use Pandas for data loading, filtering, and grouping
- Use NumPy for calculations (mean, sum, conditions)
- Visualize results with `matplotlib` or `seaborn` (optional)

---

## 📦 Real-World Projects (with Tasks & Expected Results)

---

### ✅ Project 1: 🛍️ Superstore Sales Dashboard

- **Dataset Link:** [Kaggle: Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Objective:** Analyze regional sales & product performance.

#### 🛠️ Tasks:
- Clean the data (remove nulls in `Postal Code`)
- Group total `Sales`, `Profit` by `Region`, `Category`, and `Sub-Category`
- Find:
  - Top 10 products by total sales
  - Most profitable region
  - Category with lowest profit margin
- Create a pivot table: Sales by `Region` vs. `Category`

#### ✅ Expected Output:
- Table of top-selling products
- Pivot table like:

  | Region     | Furniture | Office Supplies | Technology |
  |------------|-----------|------------------|------------|
  | East       | 200k      | 250k             | 300k       |
  | West       | ...       | ...              | ...        |

- Print insights like:
  - "Technology had the highest sales in East."
  - "Chairs were the best-selling sub-category."

---

### ✅ Project 2: 🚢 Titanic Survival Insight Report

- **Dataset Link:** [Kaggle: Titanic Dataset](https://www.kaggle.com/competitions/titanic/data)
- **Objective:** Analyze survival patterns based on demographics.

#### 🛠️ Tasks:
- Fill missing `Age` with median; fill `Embarked` with mode
- Create new column: `IsChild` → Age < 16
- Survival rate comparison:
  - Male vs. Female
  - Class-wise (`Pclass`)
  - Children vs. Adults
- Find correlation between `Fare` and `Survived`

#### ✅ Expected Output:
- Survival rate summary table:

  | Group      | Survival Rate |
  |------------|----------------|
  | Male       | 18%            |
  | Female     | 74%            |
  | Children   | 58%            |

- Printed insights:
  - "Females had significantly higher survival rate."
  - "1st Class passengers had better chances of survival."

---

### ✅ Project 3: 🌍 World Population Summary

- **Dataset Link:** [Kaggle: World Population Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset)
- **Objective:** Analyze population trends and density.

#### 🛠️ Tasks:
- Clean data, check for missing/invalid values
- Sort countries by `Population` (top 10)
- Calculate population density: `Population / Land Area`
- Create new column: `Growth %`
- Group by `Continent`:
  - Average population
  - Total land area
  - Avg. density

#### ✅ Expected Output:
- Top 10 countries by population (table)
- Printed insights:
  - "Asia has the highest average population density."
  - "India and China make up over 30% of world population."

- Optional chart (if using matplotlib):
  - Bar chart of top 10 countries
  - Pie chart of population by continent

---

### 📌 Tools to Use:
- **Pandas:** Filtering, `groupby()`, `pivot_table()`, cleaning
- **NumPy:** Stats, calculations, `np.where()`, conditions
- **(Optional)** Matplotlib/Seaborn: Basic plots (bar, pie, hist)

---