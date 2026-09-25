-- Query 1
SELECT *
FROM job_postings_fact
WHERE job_title_short = 'Data Analyst';

-- Query 2
SELECT
    job_title_short,
    job_via,
    salary_year_avg
FROM job_postings_fact
WHERE salary_year_avg >= 0;

-- Query 3
SELECT
    job_title_short,
    job_location,
    job_via,
    salary_year_avg
FROM job_postings_fact
WHERE job_title_short = 'Data Analyst'
    AND salary_year_avg > 90000
ORDER BY salary_year_avg ASC,job_location DESC;

-- Query 4
SELECT
    job_title_short,
    job_location,
    job_via,
    salary_year_avg
FROM job_postings_fact
WHERE job_title_short = 'Data Analyst'
    AND job_location IN ('Argentina', 'Turkey', 'Canada');
