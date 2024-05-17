
CREATE TABLE IF NOT EXISTS categories (
  category_id INT NOT NULL AUTO_INCREMENT,
  category_name VARCHAR(45) NOT NULL,
  PRIMARY KEY (category_id),
  KEY category_name_idx (category_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    cat_id INT,
    author VARCHAR(100),
    date DATE,
    description TEXT,
    FOREIGN KEY (cat_id) REFERENCES categories(category_id)
);
-- Inserting sample categories
INSERT INTO categories (category_name ) VALUES ('Classic' );
INSERT INTO categories (category_name ) VALUES ('Dystopian');
INSERT INTO categories (category_name ) VALUES ('Romance');
INSERT INTO categories (category_name ) VALUES ('Modernist');
INSERT INTO categories (category_name ) VALUES ('Stream of Consciousness');
INSERT INTO categories (category_name) VALUES ('Adventure');

INSERT INTO books (title, cat_id, author, date, description) VALUES ('To Kill a Mockingbird', 1, 'Harper Lee', '1960-07-11', 'To Kill a Mockingbird is a novel by Harper Lee published in 1960. It is set in the fictional town of Maycomb, Alabama, during the Great Depression.');
INSERT INTO books (title, cat_id, author, date, description) VALUES ('1984', 2, 'George Orwell', '1949-06-08', '1984 is a dystopian social science fiction novel by George Orwell. It depicts a totalitarian regime controlling every aspect of life.');
INSERT INTO books (title, cat_id, author, date, description) VALUES ('Pride and Prejudice', 3, 'Jane Austen', '1813-01-28', 'Pride and Prejudice is a romantic novel by Jane Austen, first published in 1813. The story follows the main character Elizabeth Bennet as she deals with issues of manners, upbringing, morality, education, and marriage in the society of the landed gentry of the British Regency.');
INSERT INTO books (title, cat_id, author, date, description) VALUES ('The Great Gatsby', 4, 'F. Scott Fitzgerald', '1925-04-10', 'The Great Gatsby is a novel by American writer F. Scott Fitzgerald. Set in the Jazz Age on Long Island, the novel depicts narrator Nick Carraway\'s interactions with mysterious millionaire Jay Gatsby and Gatsby\'s obsession to reunite with his former lover, Daisy Buchanan.');
INSERT INTO books (title, cat_id, author, date, description) VALUES ('To the Lighthouse', 5, 'Virginia Woolf', '1927-05-05', 'To the Lighthouse is a novel by Virginia Woolf. The novel centres on the Ramsay family and their visits to the Isle of Skye in Scotland between 1910 and 1920.');
INSERT INTO books (title, cat_id, author, date, description) VALUES ('Moby-Dick', 6, 'Herman Melville', '1851-10-18', 'Moby-Dick; or, The Whale is an 1851 novel by American writer Herman Melville. The book is the sailor Ishmael\'s narrative of the obsessive quest of Ahab, captain of the whaling ship Pequod, for revenge on Moby Dick, the giant white sperm whale that on the ship\'s previous voyage bit off Ahab\'s leg at the knee.');
