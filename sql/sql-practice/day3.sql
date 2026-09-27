USE salesdb;

-- Query 1
SELECT  * 
FROM customers
WHERE firstname LIKE '%A%'AND score>=500 ;

-- Query 1
SELECT * 
FROM customers
WHERE  country='USA' AND firstname LIKE '%A%';


-- Query 1
SELECT  firstname,country,score
FROM  customers
WHERE score BETWEEN 100 AND 500;


-- Query 1
SELECT * 
FROM customers 
WHERE customerid IN (1,2,5);


-- Query 1
SELECT * 
FROM customers
WHERE  firstname LIKE 'M%';

-- Query 1
SELECT * 
FROM customers 
WHERE firstname LIKE '%a%';








