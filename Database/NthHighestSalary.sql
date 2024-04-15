/*
LeetCode [177]: Nth Highest Salary

Write a SQL query to get the nth highest salary from the Employee table. If there is no nth highest salary, then the query should return null.

SQL Schema:
Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| Id          | int     |
| Salary      | int     |
+-------------+---------+

Approach:
Use a subquery to select distinct salary values in descending order, and then skip the first (N-1) highest salaries to get the Nth highest salary.

Query:
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
    RETURN (
       SELECT DISTINCT Salary 
       FROM Employee 
       ORDER BY Salary DESC 
       LIMIT 1 OFFSET N
  );
END
