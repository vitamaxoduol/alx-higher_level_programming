--  Script that creates a table called first_table in the current database
--  If the table first_table already exists, your script should not fail
--  You are not allowed to use the SELECT or SHOW statements

CREATE TABLE IF NOT EXISTS first_table(
	id INT, name VARCHAR(256)
);
