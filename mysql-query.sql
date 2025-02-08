CREATE TABLE dummy_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


-- Step 2: Insert 10 rows of dummy data
INSERT INTO dummy_table (name, age, city)
VALUES 
('Alice', 25, 'New York'),
('Bob', 30, 'Los Angeles'),
('Charlie', 22, 'Chicago'),
('Daisy', 28, 'Houston'),
('Ethan', 35, 'Phoenix'),
('Fiona', 27, 'Philadelphia'),
('George', 29, 'San Antonio'),
('Hannah', 24, 'San Diego'),
('Isaac', 31, 'Dallas'),
('Julia', 26, 'San Jose');