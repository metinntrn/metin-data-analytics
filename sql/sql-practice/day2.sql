--Query 1
SELECT 
	job_title_short,
    job_location,
    job_via,
    salary_year_avg
FROM
	job_postings_fact
WHERE 
	job_location IN('Torrance, CA','Los Angeles, CA','Anywhere') AND
(
	(job_title_short='Data Analyst' AND salary_year_avg>90000)OR
  	(job_title_short='Business Analyst' AND salary_year_avg>70000)
);

--Query2
SELECT 
	job_title_short,
    job_location,
    job_via,
    salary_year_avg
FROM
	job_postings_fact
WHERE 
	--job_title_short LIKE '%Analyst%'
    job_title_short LIKE '%Business%Analyst%';

--Query 3
SELECT
  	job_id,
    job_title,
    job_posted_date 
FROM
	job_postings_fact 
WHERE 
	job_title LIKE '%Engineer%'	;
--Query 4
