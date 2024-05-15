-- Connect to MySQL and create a database
CREATE DATABASE IF NOT EXISTS bookeat;
USE bookeat;
CREATE TABLE IF NOT EXISTS Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,  -- This assumes you have a Category table defined
    title VARCHAR(255),
    author VARCHAR(255),
    ISBN VARCHAR(20),
    genre VARCHAR(50),
    publication_date DATE,
    availability BOOLEAN
);

INSERT INTO Books (category_id, title, author, ISBN, genre, publication_date, availability)
VALUES
    (1, 'Book Title 1', 'Author 1', 'ISBN-1', 'Genre 1', '2024-01-01', true),
    (2, 'Book Title 2', 'Author 2', 'ISBN-2', 'Genre 2', '2024-02-01', false),
    (3, 'Book Title 3', 'Author 3', 'ISBN-3', 'Genre 3', '2024-03-01', true);
