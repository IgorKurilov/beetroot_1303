# Create task2.sql file with the required queries
sql_queries = """
-- 1. Display the names (first_name, last_name) using alias "First Name", "Last Name":
SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees;

-- 2. Get the unique department ID from the employee table:
SELECT DISTINCT department_id FROM employees;

-- 3. Get all employee details from the employee table ordered by first name, descending:
SELECT * FROM employees ORDER BY first_name DESC;

-- 4. Get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary):
SELECT first_name, last_name, salary, salary * 0.12 AS PF FROM employees;

-- 5. Get the maximum and minimum salary from the employees table:
SELECT MAX(salary) AS Max_Salary, MIN(salary) AS Min_Salary FROM employees;

-- 6. Get a monthly salary (round to 2 decimal places) of each and every employee:
SELECT first_name, last_name, ROUND(salary / 12, 2) AS Monthly_Salary FROM employees;
"""

# Save to task2.sql
with open('/mnt/data/task2.sql', 'w') as file:
    file.write(sql_queries)
