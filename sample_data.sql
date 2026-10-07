DROP TABLE IF EXISTS sales;
CREATE TABLE sales
(
    sale_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    copies INTEGER NOT NULL,
    unit_price REAL NOT NULL
);

INSERT INTO sales (sale_id, title, genre, copies, unit_price) VALUES

(1, 'The Silent Witness', 'Crime', 3, 20.00), -- 60
(2, 'Midnight Alibi', 'Crime', 5, 10.00), -- 50
(3, 'Cold Case Files', 'Crime', 1, 20.00), -- 20
(4, 'Leaves of Ink', 'Poetry', 2, 15.00), -- 30
(5, 'Quiet Verses', 'Poetry', 1, 25.00), -- 25
(6, 'Stars Beyond Orion', 'Sci-Fi', 4, 30.00), -- 120
(7, 'The Last Colony', 'Sci-Fi', 2, 45.00), -- 90
(8, 'Baking at Home', 'Cooking', 4, 25.00); -- 100