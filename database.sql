CREATE DATABASE eduassist;

USE eduassist;

CREATE TABLE users(

id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(100),

email VARCHAR(100),

password VARCHAR(100)

);
CREATE TABLE progress(

id INT AUTO_INCREMENT PRIMARY KEY,

student VARCHAR(100),

quiz_score INT,

completed_date DATE

);
