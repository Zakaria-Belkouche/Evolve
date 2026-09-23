## Data Definition language commands (DDL):

DDL commands are used to define and manage the schema of the database. 

- Deals with the structure of the database structure itself.
- Only for describing and altering the structure of the database
- Creates new databases, tables, views, indexes, users and other database objects.
- Can not touch stored data in the database. 

Common DDL commands include:

- CREATE: Used to create new database objects such as tables, views, and indexes.
- ALTER: Used to modify the structure of existing database objects, such as adding or dropping columns in a table.
- DROP: Used to delete existing database objects, such as tables or views.
- TRUNCATE: Used to remove all records from a table, but not the table itself.

## Data Manipulation Language commands (DML):

DML commands are used to manipulate the data stored in the database. 

- Deals with the manipulation of data stored in the database.
- Used for inserting, updating, deleting, and retrieving data from the database.
- Always deals with rows of data in the database tables. Not used for adding/removing columns as this falls under the structure of the database and is handled by DDL commands.

Common DML commands include:

- INSERT: Used to add new records to a table.
- UPDATE: Used to modify existing records in a table.
- DELETE: Used to remove existing records from a table.
- SELECT: Used to retrieve data from one or more tables in the database.

## Transaction control commands (TCL):

- Used to manage the changes made by SQL commands. After changes are made, they can be committed or rolled back to maintain the integrity of the database.
- Common TCL commands include: COMMIT, ROLLBACK, SAVEPOINT

Example: 

```sql
BEGIN;

UPDATE accounts
SET balance = balance - 100
WHERE id = 1;

COMMIT;
```

```sql
BEGIN;

DELETE FROM users
WHERE id = 5;

ROLLBACK;
```

## Data Control Language commands (DCL):

DCL commands are used to control access to the data in the database. They are used to grant or revoke permissions on database objects.

Common DCL commands include:

- GRANT: Used to give users permission to perform certain operations on database objects.
- REVOKE: Used to remove permissions from users.

Example:

```sql
GRANT SELECT, INSERT ON users TO john;
```

```sql
REVOKE INSERT ON users FROM john;
```

## Examples

Write a query to create a new database and a table with three columns:

```sql
CREATE DATABASE EVOLVE_db;

USE EVOLVE_db; -- This command ensures you are connected to EVOLVE_db

CREATE TABLE dept (
	dept_id INT,
	dept_name VARCHAR(20),
	location VARCHAR(20)
);
```

Write a query to alter the `dept` table by adding a new column:

```sql
ALTER TABLE dept
ADD COLUMN dept_size INT(5);
```

Write a query to drop a column:

```sql
ALTER TABLE dept
DROP COLUMN dept_size;
```

Write a query to insert multiple records into selected columns:

```sql
INSERT INTO dept (dept_id, dept_name)
VALUES
	(3, 'DEVOPS'),
	(4, 'INFRASTRUCTURE');
```

Write a query to update a department's location and name:

```sql
UPDATE dept
SET location = 'Reading',
	dept_name = 'Software Engineering'
WHERE dept_id = 4;
```

Write a query to delete a department by ID:

```sql
DELETE FROM dept
WHERE dept_id = 5;
```

Write a query to display department names and locations:

```sql
SELECT dept_name, location
FROM dept;
```

## Constraints

A constraint is a rule that governs the data that can be entered into a table. SQL supports several types of constraints:

### PRIMARY KEY

A primary key uniquely identifies each record in a table. A table can have only one primary key, which is usually an ID column.

### FOREIGN KEY

A foreign key is a column in a child table that refers to a primary key in a parent table. It creates a relationship between the two tables and helps maintain referential integrity.

### NOT NULL

The `NOT NULL` constraint ensures that a column must always contain a value.

### CHECK

The `CHECK` constraint ensures that values meet a specified condition before they can be stored.

### DEFAULT

The `DEFAULT` constraint provides a value automatically when no value is supplied.

### UNIQUE

The `UNIQUE` constraint ensures that all values in a column are different. For example, it can prevent two users from registering with the same username: "Username is already taken."

## Tables with Constraints

When creating related tables, follow these rules:

- Populate the parent table before populating the child table.
- Drop the child table before dropping the parent table.

!(SQL example Image)[../../../images/SQL-Diagram1.png]

The `dept` table is the parent table because it contains the primary key that the `employee` table refers to.

Create the parent table first:

```sql
CREATE TABLE dept (
	dept_id INT PRIMARY KEY,
	dept_name VARCHAR(20),
	location VARCHAR(20)
);
```

Create the child table with a primary key, a unique email address, and a foreign key referencing `dept`:

```sql
CREATE TABLE employee (
	emp_id INT PRIMARY KEY,
	emp_name VARCHAR(20),
	email VARCHAR(20) UNIQUE,
	dept_id INT,
	FOREIGN KEY (dept_id) REFERENCES dept(dept_id)
);
```

## Sorting and Counting

### Sort Employee Details

Use `ORDER BY` to sort employee details by name in ascending order. Use `DESC` instead of `ASC` for descending order.

```sql
SELECT *
FROM employee
ORDER BY emp_name ASC;
```

### Count Employees

Use `COUNT(*)` to count the number of employee records. The `AS` keyword gives the result a readable alias.

```sql
SELECT COUNT(*) AS "Employee Count"
FROM employee;
```

## SQL Joins

SQL joins are used to retrieve related data from multiple tables. Common join types include:

- `INNER JOIN`
- `LEFT JOIN`
- `RIGHT JOIN`
- `FULL JOIN` (database-dependent and not supported by all databases)
- `SELF JOIN`

### INNER JOIN

Display the department name, employee name, employee ID, and department ID for employees that belong to a department:

```sql
SELECT d.dept_name, e.emp_name, e.emp_id, e.dept_id
FROM dept AS d
INNER JOIN employee AS e
    ON d.dept_id = e.dept_id;
```

### LEFT JOIN

Return all departments, including departments that do not currently have employees:

```sql
SELECT d.dept_name, e.emp_name, e.emp_id, e.dept_id
FROM dept AS d
LEFT JOIN employee AS e
    ON d.dept_id = e.dept_id;
```

### RIGHT JOIN

Return all employees, including employees whose department is not represented in the result from the left table:

```sql
SELECT d.dept_name, e.emp_name, e.emp_id, e.dept_id
FROM dept AS d
RIGHT JOIN employee AS e
    ON d.dept_id = e.dept_id;
```

### Table Aliases

Aliases make queries shorter and easier to read. In the examples above, `d` represents `dept` and `e` represents `employee`.

