-- Task 1: Display the first name, last name, department number, and department name for each employee
SELECT e.first_name, e.last_name, e.department_id, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- Task 2: Display the first and last name, department, city, and state province for each employee
SELECT e.first_name, e.last_name, d.department_name, l.city, l.state_province
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id;

-- Task 3: Display the first name, last name, department number, and department name, for all employees for departments 80 or 40
SELECT e.first_name, e.last_name, e.department_id, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.department_id IN (80, 40);

-- Task 4: Display all departments including those where does not have any employee
SELECT d.department_name, e.first_name, e.last_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id;

-- Task 5: Display the first name of all employees including the first name of their manager
SELECT e.first_name AS employee_first_name, m.first_name AS manager_first_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;

-- Task 6: Display the job title, full name (first and last name) of the employee, and the difference between the maximum salary for the job and the salary of the employee
SELECT j.job_title, e.first_name || ' ' || e.last_name AS full_name, 
       (j.max_salary - e.salary) AS salary_difference
FROM employees e
JOIN jobs j ON e.job_id = j.job_id;

-- Task 7: Display the job title and the average salary of employees
SELECT j.job_title, AVG(e.salary) AS average_salary
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title;

-- Task 8: Display the full name (first and last name), and salary of those employees who work in any department located in London
SELECT e.first_name || ' ' || e.last_name AS full_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE l.city = 'London';

-- Task 9: Display the department name and the number of employees in each department
SELECT d.department_name, COUNT(e.employee_id) AS number_of_employees
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;
