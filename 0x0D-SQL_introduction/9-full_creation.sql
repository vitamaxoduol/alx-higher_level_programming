--  Script that creates a table second_table in the database 
--  If the table second_table already exists, your script should not fail
--  You are not allowed to use the SELECT and SHOW statements
--  Script should create the given records

CREATE TABLE IF NOT EXISTS second_table (
	id INT, name VARCHAR(256), score INT);

INSERT INTO `second_table` (`id`, `name`, `score`)
VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);
