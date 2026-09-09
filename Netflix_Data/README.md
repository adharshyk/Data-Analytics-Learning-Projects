# Netflix Content & Regional Trends Analytics

An end-to-end data analytics and business intelligence project examining catalog evolution, content mix, geographic concentration, and genre dominance across Netflix titles.

## Business Objective

The project analyzes **8,807 Netflix titles** to help understand:

- Content acquisition volume and annual addition velocity
- Shifts in format distribution between Movies and TV Shows over time
- Global geographic production hubs and regional catalog distribution
- Dominant genres across feature films versus episodic television
- Maturity rating distribution and target audience segmentation
- Regional markets exhibiting unique content composition compared to the platform average
## Key Features

- Data preprocessing, missing value handling, and runtime field parsing
- Unnesting of multi-valued country and genre attributes using recursive CTEs
- Year-over-year title addition and growth rate calculations via window functions (`LAG`)
- Category and country ranking partitioned by content type (`RANK`)
- Global benchmark comparisons of TV show market shares against overall platform averages
- Trend visualizations tracking content type mix shifts across addition years

## Tools & Technologies

- **Python** (Pandas, NumPy, Matplotlib)
- **SQL** (MySQL)
- **Recursive CTEs**
- **Window Functions** (`RANK`, `LAG`)
- **Exploratory Data Analysis (EDA)**
- **Data Visualization**
## Dataset

The analysis uses one primary dataset:

- `netflix_titles.csv` — 8,807 records covering Movies and TV Shows with 12 metadata attributes including title, director, cast, country, release year, date added, rating, duration, and genre categories.
## Analysis Structure

### Exploratory Data Analysis & Transformation (`netflix.ipynb`)
Handles data cleaning, imputation of missing fields (`director`, `cast`, `country`, `rating`), fixes misaligned duration values, standardizes date formats, and generates visual distributions for content mix, yearly additions, and top genres.
### Advanced SQL Analytics (`netflix.sql`)
Executes recursive string splitting to normalize multi-country and multi-genre rows, calculates annual growth percentages, ranks top contributors by format, and identifies countries exceeding the platform's baseline TV show share.

## Business Value

The project provides content strategists and acquisition teams with actionable insights into **catalog expansion patterns, audience demographic focus, regional production dependencies, and localized format preferences**, supporting data-driven decisions in licensing and original programming investments.
## Skills Demonstrated

**Python · SQL · Recursive CTEs · Window Functions · Data Cleaning · Feature Engineering · Exploratory Data Analysis · Data Modeling · Business Analytics · Trend Analysis**

---
### Author

**Adharsh Kuttithazhath**
