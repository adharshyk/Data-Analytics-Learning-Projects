# Netflix Content & Regional Trends Analytics

An end-to-end data analytics and business intelligence project examining catalog evolution, content mix, geographic concentration, and genre dominance across Netflix titles.

## Business Objective

The project analyzes **8,807 Netflix titles**[cite: 1] to help understand:

- Content acquisition volume and annual addition velocity[cite: 1, 2]
- Shifts in format distribution between Movies and TV Shows over time[cite: 1]
- Global geographic production hubs and regional catalog distribution[cite: 1, 2]
- Dominant genres across feature films versus episodic television[cite: 1, 2]
- Maturity rating distribution and target audience segmentation[cite: 1]
- Regional markets exhibiting unique content composition compared to the platform average[cite: 2]

## Key Features

- Data preprocessing, missing value handling, and runtime field parsing[cite: 1]
- Unnesting of multi-valued country and genre attributes using recursive CTEs[cite: 2]
- Year-over-year title addition and growth rate calculations via window functions (`LAG`)[cite: 2]
- Category and country ranking partitioned by content type (`RANK`)[cite: 2]
- Global benchmark comparisons of TV show market shares against overall platform averages[cite: 2]
- Trend visualizations tracking content type mix shifts across addition years[cite: 1]

## Tools & Technologies

- **Python** (Pandas, NumPy, Matplotlib)[cite: 1]
- **SQL** (MySQL)[cite: 2]
- **Recursive CTEs**[cite: 2]
- **Window Functions** (`RANK`, `LAG`)[cite: 2]
- **Exploratory Data Analysis (EDA)**[cite: 1]
- **Data Visualization**[cite: 1]

## Dataset

The analysis uses one primary dataset:

- `netflix_titles.csv` — 8,807 records covering Movies and TV Shows with 12 metadata attributes including title, director, cast, country, release year, date added, rating, duration, and genre categories[cite: 1].

## Analysis Structure

### Exploratory Data Analysis & Transformation (`netflix.ipynb`)
Handles data cleaning, imputation of missing fields (`director`, `cast`, `country`, `rating`), fixes misaligned duration values, standardizes date formats, and generates visual distributions for content mix, yearly additions, and top genres[cite: 1].

### Advanced SQL Analytics (`netflix.sql`)
Executes recursive string splitting to normalize multi-country and multi-genre rows, calculates annual growth percentages, ranks top contributors by format, and identifies countries exceeding the platform's baseline TV show share[cite: 2].

## Business Value

The project provides content strategists and acquisition teams with actionable insights into **catalog expansion patterns, audience demographic focus, regional production dependencies, and localized format preferences**, supporting data-driven decisions in licensing and original programming investments[cite: 1, 2].

## Skills Demonstrated

**Python · SQL · Recursive CTEs · Window Functions · Data Cleaning · Feature Engineering · Exploratory Data Analysis · Data Modeling · Business Analytics · Trend Analysis**

---
### Author

**Adharsh Kuttithazhath**