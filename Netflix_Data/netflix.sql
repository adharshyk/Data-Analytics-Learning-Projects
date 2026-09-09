CREATE DATABASE netflix_analysis;

USE netflix_analysis;

select * from netflix_titles ;

SELECT COUNT(*)
FROM netflix_titles;

-- 1. Which countries contribute the most content to Netflix?

WITH RECURSIVE countries AS (
    SELECT
        show_id,
        TRIM(SUBSTRING_INDEX(country, ',', 1)) AS country,
        SUBSTRING(country, LENGTH(SUBSTRING_INDEX(country, ',', 1)) + 2) AS remaining
    FROM netflix_titles
    WHERE country IS NOT NULL
      AND country <> 'Unknown'

    UNION ALL

    SELECT
        show_id,
        TRIM(SUBSTRING_INDEX(remaining, ',', 1)) AS country,
        SUBSTRING(remaining, LENGTH(SUBSTRING_INDEX(remaining, ',', 1)) + 2) AS remaining
    FROM countries
    WHERE remaining <> ''
)

SELECT
    country,
    COUNT(DISTINCT show_id) AS total_titles
FROM countries
WHERE country <> ''
GROUP BY country
ORDER BY total_titles DESC
LIMIT 15; 

-- 2.How has Netflix's content addition changed year-over-year?

WITH yearly_content AS (
    SELECT
        YEAR(date_added) AS year,
        COUNT(*) AS titles_added
    FROM netflix_titles
    WHERE date_added IS NOT NULL
    GROUP BY YEAR(date_added)
),

yearly_comparison AS (
    SELECT
        year,
        titles_added,
        LAG(titles_added) OVER (ORDER BY year) AS previous_year
    FROM yearly_content
)

SELECT
    year AS Year,
    titles_added AS `Titles Added`,
    previous_year AS `Previous Year`,
    titles_added - previous_year AS `Change`,
    ROUND(
        (titles_added - previous_year) / previous_year * 100,
        2
    ) AS `Growth %`
FROM yearly_comparison
ORDER BY year;


-- 3. What are the top countries for Movies vs TV Shows?

WITH RECURSIVE country_split AS (
    SELECT
        show_id,
        type,
        TRIM(SUBSTRING_INDEX(country, ',', 1)) AS country,
        SUBSTRING(
            country,
            LENGTH(SUBSTRING_INDEX(country, ',', 1)) + 2
        ) AS remaining
    FROM netflix_titles
    WHERE country IS NOT NULL
      AND country <> 'Unknown'

    UNION ALL

    SELECT
        show_id,
        type,
        TRIM(SUBSTRING_INDEX(remaining, ',', 1)) AS country,
        SUBSTRING(
            remaining,
            LENGTH(SUBSTRING_INDEX(remaining, ',', 1)) + 2
        ) AS remaining
    FROM country_split
    WHERE remaining <> ''
),

country_type_counts AS (
    SELECT
        type,
        country,
        COUNT(DISTINCT show_id) AS total_titles
    FROM country_split
    WHERE country <> ''
    GROUP BY type, country
),

ranked_countries AS (
    SELECT
        type,
        country,
        total_titles,
        RANK() OVER (
            PARTITION BY type
            ORDER BY total_titles DESC
        ) AS country_rank
    FROM country_type_counts
)

SELECT
    type,
    country,
    total_titles,
    country_rank
FROM ranked_countries
WHERE country_rank <= 10
ORDER BY type, country_rank;


-- 4.Which genres dominate Movies vs TV Shows? 

WITH RECURSIVE genre_split AS (
    SELECT
        show_id,
        type,
        TRIM(SUBSTRING_INDEX(listed_in, ',', 1)) AS genre,
        SUBSTRING(
            listed_in,
            LENGTH(SUBSTRING_INDEX(listed_in, ',', 1)) + 2
        ) AS remaining
    FROM netflix_titles
    WHERE listed_in IS NOT NULL

    UNION ALL

    SELECT
        show_id,
        type,
        TRIM(SUBSTRING_INDEX(remaining, ',', 1)) AS genre,
        SUBSTRING(
            remaining,
            LENGTH(SUBSTRING_INDEX(remaining, ',', 1)) + 2
        ) AS remaining
    FROM genre_split
    WHERE remaining <> ''
),

genre_counts AS (
    SELECT
        type,
        genre,
        COUNT(DISTINCT show_id) AS total_titles
    FROM genre_split
    WHERE genre <> ''
    GROUP BY type, genre
),

ranked_genres AS (
    SELECT
        type,
        genre,
        total_titles,
        RANK() OVER (
            PARTITION BY type
            ORDER BY total_titles DESC
        ) AS genre_rank
    FROM genre_counts
)

SELECT
    type,
    genre,
    total_titles,
    genre_rank
FROM ranked_genres
WHERE genre_rank <= 10
ORDER BY type, genre_rank;


-- 5.Which countries have a higher proportion of TV Shows than Netflix overall? 

WITH RECURSIVE country_split AS (

    SELECT
        show_id,
        type,
        TRIM(SUBSTRING_INDEX(country, ',', 1)) AS country,
        SUBSTRING(
            country,
            LENGTH(SUBSTRING_INDEX(country, ',', 1)) + 2
        ) AS remaining
    FROM netflix_titles
    WHERE country IS NOT NULL
      AND country <> 'Unknown'

    UNION ALL

    SELECT
        show_id,
        type,
        TRIM(SUBSTRING_INDEX(remaining, ',', 1)) AS country,
        SUBSTRING(
            remaining,
            LENGTH(SUBSTRING_INDEX(remaining, ',', 1)) + 2
        ) AS remaining
    FROM country_split
    WHERE remaining <> ''
),

country_stats AS (

    SELECT
        country,
        COUNT(DISTINCT show_id) AS total_titles,
        COUNT(DISTINCT CASE
            WHEN type = 'TV Show' THEN show_id
        END) AS tv_shows
    FROM country_split
    WHERE country <> ''
    GROUP BY country
),

country_share AS (

    SELECT
        country,
        total_titles,
        tv_shows,
        ROUND(tv_shows / total_titles * 100, 2) AS tv_show_share
    FROM country_stats
),

overall_average AS (

    SELECT
        COUNT(DISTINCT CASE
            WHEN type = 'TV Show' THEN show_id
        END)
        / COUNT(DISTINCT show_id) * 100 AS overall_tv_share
    FROM netflix_titles
    WHERE type IS NOT NULL
)

SELECT
    c.country,
    c.total_titles,
    c.tv_shows,
    c.tv_show_share,
    ROUND(o.overall_tv_share, 2) AS overall_tv_share
FROM country_share c
CROSS JOIN overall_average o
WHERE c.tv_show_share > o.overall_tv_share
ORDER BY c.tv_show_share DESC;