/*
LeetCode [175]: Combine Two Tables

SQL Schema:
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.

Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.

Write a SQL query to combine information from the two tables to obtain the following information:

+-------------+---------+-------+-------+
| FirstName   | LastName| City  | State |
+-------------+---------+-------+-------+

Approach:
Perform a LEFT JOIN operation on the Person and Address tables using the PersonId column as the join key.

Query:
*/

SELECT p.FirstName, p.LastName, a.City, a.State 
FROM Person p 
LEFT JOIN Address a 
ON p.PersonId = a.PersonId;
