DROP DATABASE bookeat;
CREATE DATABASE bookeat;
USE bookeat;

CREATE TABLE IF NOT EXISTS account (
  user_id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(45) NOT NULL,
  username VARCHAR(60) NOT NULL,
  password VARCHAR(45) NOT NULL,
  user_type ENUM('admin', 'user') NOT NULL DEFAULT 'user',
  PRIMARY KEY (user_id),
  UNIQUE KEY email_UNIQUE (email)
);



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

CREATE TABLE IF NOT EXISTS warehouse (
    base_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_book INT,
    quantity INT,
    FOREIGN KEY (id_book) REFERENCES books(book_id)
); 

CREATE TABLE IF NOT EXISTS requested_books (
  request_id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  request_content VARCHAR(100) NOT NULL,
  request_date DATETIME NOT NULL,
  book_id INT NOT NULL,
  quantity INT NOT NULL,
  status VARCHAR(10) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (request_id),
  KEY reqbooks_fk_user_id_idx (user_id),
  KEY reqbooks_fk_book_id_idx (book_id),
  CONSTRAINT reqbooks_fk_book_id FOREIGN KEY (book_id) REFERENCES books (book_id),
  CONSTRAINT reqbooks_fk_user_id FOREIGN KEY (user_id) REFERENCES account (user_id)
);

CREATE TABLE wishlist(
user_id INT NOT NULL,
book_id INT NOT NULL
);
CREATE TABLE favourites(
user_id INT NOT NULL,
book_id INT NOT NULL
);
CREATE TABLE recommendedBooks (
user_id INT NOT NULL,
book_id INT NOT NULL
);

CREATE TABLE rooms
 (
    room_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    room_name VARCHAR(255),
    status VARCHAR(50)
 );

CREATE TABLE announcements (
  announcement_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  title varchar(45) NOT NULL,
  texting text(255) NOT NULL
);

CREATE TABLE event (
  event_id INT NOT NULL,
  date_hour datetime,
  location varchar(45),
  available_seats INT,
  interested_users INT,
  FOREIGN KEY (event_id) REFERENCES announcements(announcement_id)
);

CREATE TABLE requests
 (
    request_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    members INT(5),
    timer INT(3),
    FOREIGN KEY (request_id) REFERENCES rooms(room_id)
 );

CREATE TABLE equipment (
  equipment_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  request_id INT,
  equipment_name VARCHAR(255) NOT NULL,
  FOREIGN KEY (request_id) REFERENCES requests(request_id)
);

-- Inserting sample users
INSERT INTO account (email, username, password, user_type) VALUES ('user1@example.com', 'user1', 'user1', 'user');

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

-- Inserting sample data into the warehouse table
INSERT INTO warehouse (id_book, quantity) VALUES ((SELECT book_id FROM books WHERE title = 'To Kill a Mockingbird' LIMIT 1), 20);
INSERT INTO warehouse (id_book, quantity) VALUES ((SELECT book_id FROM books WHERE title = '1984' LIMIT 1), 15);
INSERT INTO warehouse (id_book, quantity) VALUES ((SELECT book_id FROM books WHERE title = 'Pride and Prejudice' LIMIT 1), 30);
INSERT INTO warehouse (id_book, quantity) VALUES ((SELECT book_id FROM books WHERE title = 'The Great Gatsby' LIMIT 1), 10);
INSERT INTO warehouse (id_book, quantity) VALUES ((SELECT book_id FROM books WHERE title = 'To the Lighthouse' LIMIT 1), 5);
INSERT INTO warehouse (id_book, quantity) VALUES ((SELECT book_id FROM books WHERE title = 'Moby-Dick' LIMIT 1), 25);

INSERT INTO rooms(room_name, status) VALUES ('Dexameni Project', 'available'); 

INSERT INTO requests(members, timer) VALUE ('2', '2');


INSERT INTO equipment( request_id, equipment_name) VALUES ('1','laptop');
INSERT INTO equipment( request_id, equipment_name) VALUES ('1','board');
INSERT INTO equipment(request_id, equipment_name) VALUES ('1','pens');
