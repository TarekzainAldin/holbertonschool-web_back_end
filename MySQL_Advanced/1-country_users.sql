-- SQL script to create the users table with specific attributes:
--  - id: INTEGER, NOT NULL, AUTO_INCREMENT, PRIMARY KEY.
--  - email: VARCHAR(255), NOT NULL, UNIQUE.
--  - name: VARCHAR(255).
--  - country: ENUM('US', 'CO', 'TN'), NOT NULL, DEFAULT 'US' (first element of the enumeration).
-- If the table already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  
    email VARCHAR(255) NOT NULL UNIQUE,            
    name VARCHAR(255),                             
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'  
);