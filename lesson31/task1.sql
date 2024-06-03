-- Create a sample table
CREATE TABLE sample_table (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);

-- Insert a couple of rows into the table
INSERT INTO sample_table (name, age) VALUES ('Alice', 30);
INSERT INTO sample_table (name, age) VALUES ('Bob', 25);

-- Rename the table to new_sample_table
ALTER TABLE sample_table RENAME TO new_sample_table;

-- Add a new column 'email' to the renamed table
ALTER TABLE new_sample_table ADD COLUMN email TEXT;

-- Update the inserted rows to add email addresses
UPDATE new_sample_table SET email = 'alice@example.com' WHERE name = 'Alice';
UPDATE new_sample_table SET email = 'bob@example.com' WHERE name = 'Bob';

-- Delete one of the rows
DELETE FROM new_sample_table WHERE name = 'Bob';

-- Verify the changes
SELECT * FROM new_sample_table;
