USE lib; -- use the existing database

SELECT * FROM authors;

SELECT  * FROM books;

SELECT * FROM borrowed_books;

SELECT * FROM users;


INSERT INTO authors (name, biography)
VALUES ( 'Gayle Mcdowell', 'fouder of careercup'),
('Simon Sinek', 'motivational speaker'),
('Noam Wasserman','associate professor'),
('Jiawei Han', 'computer scientist and writer'),
('Ben Millspaugh', 'aviation writer');



INSERT  INTO books(title,author_id,isbn, publication_date)
VALUES ('Cracking the coding interview',1,'9780984782857','2021-02-04'),
( 'Leader eat last', 2, '9781591848011', '2014-01-01'),
( 'The founders dilemmas', 3, '9780691149134','2012-01-01'),
( 'Data Mining Concepts and techniques', 4, '9780123814791','2011-07-06'),
( 'Aerospace the journey of flight', 5, '9780615188584', '2008-01-01');

INSERT INTO users(name, library_id)
VALUES('Tim Testpilot', '5555');



