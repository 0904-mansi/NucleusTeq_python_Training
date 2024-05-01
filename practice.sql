-- Creating databse
-- CREATE DATABASE employee_details;

-- Use database
-- USE employee_details;

-- Creating table
CREATE TABLE employee
(
emp_id INT PRIMARY KEY,
emp_name VARCHAR(20),
email_id VARCHAR(30),
city VARCHAR(25),
Verification_status CHAR(3)
);

-- Inserting values into the table
INSERT INTO employee VALUES (1,'Suhas','deshmukhsuhas4567@gmail.com','Mumbai','Yes');
INSERT INTO employee VALUES (2,'Yohani','missyohani@gmail.com','Mumbai','No');
INSERT INTO employee VALUES (3,'Reshama','reshah89000@gmail.com','Pune','Yes');
INSERT INTO employee VALUES (4,'Raj','shetheyraj8989@gmail.com','Bangalore','No');
INSERT INTO employee VALUES (5,'Shivani','shivanimore@gmail.com','Bangalore','Yes');
SELECT * FROM employee;

WITH mycte AS 
(
  SELECT  emp_name , Verification_status 
  FROM employee 
  WHERE Verification_status = 'No'
)
SELECT * FROM mycte;



CREATE TABLE product

(

p_id INT PRIMARY KEY,

p_name VARCHAR(20),

category VARCHAR(30)

);

-- Creating table sales

CREATE TABLE sales

(

p_id INT PRIMARY KEY,

p_name VARCHAR(20),

gross_sales DECIMAL

);

-- Inserting values into the table 'product'

INSERT INTO product VALUES (1, 'Mobile', 'Electronics');

INSERT INTO product VALUES (2, 'TV', 'Electronics');

INSERT INTO product VALUES (3, 'Car', 'Toy');

INSERT INTO product VALUES (4, 'Video game', 'Toy');

INSERT INTO product VALUES (5, 'Earphones', 'Electronics');

-- Inserting values into the table 'sales'

INSERT INTO sales VALUES (1, 'Mobile', 50000);

INSERT INTO sales VALUES (2, 'TV', 40000);

INSERT INTO sales VALUES (3, 'Car', 50000);

INSERT INTO sales VALUES (5, 'Earphones', 500000);

-- Show all columns from the table 'product'

SELECT * FROM product;

-- Show all columns from the table 'product'

SELECT * FROM sales;

WITH TEMP_CTE AS

(

SELECT p.category AS category,

       COUNT(*) AS No_of_products,

       SUM(s.gross_sales) AS Total_gross_sales

FROM product p JOIN sales s 

ON p.p_id=s.p_id

GROUP BY category

ORDER BY Total_gross_sales DESC

)

SELECT * FROM TEMP_CTE;

UPDATE product SET category = 'Accessories' WHERE p_id = 5;

UPDATE sales SET gross_sales = gross_sales + 10000 WHERE p_id = 1;

SELECT p_name, SUM(gross_sales) AS total_sales
FROM sales
GROUP BY p_name;


SELECT p_name, SUM(gross_sales) AS total_sales
FROM sales
GROUP BY p_name
HAVING SUM(gross_sales) > 50000;

SELECT p_name, SUM(gross_sales) AS total_sales
FROM sales
GROUP BY p_name
ORDER BY total_sales DESC;

SELECT s.p_name, SUM(s.gross_sales) AS total_sales
FROM sales s
JOIN product p ON s.p_id = p.p_id
WHERE p.category = 'Electronics'
GROUP BY s.p_name
HAVING SUM(s.gross_sales) > 50000;

