-- SQL script to create the users table
-- This table ensures that emails are unique and cannot be null.
-- If the table already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  
    email VARCHAR(255) NOT NULL UNIQUE,          
    name VARCHAR(255)                            
);
