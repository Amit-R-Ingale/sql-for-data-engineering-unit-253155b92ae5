import os
import sqlite3
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))

def read_sql(name):
    with open(os.path.join(HERE, name), encoding="utf-8-sig") as f:
        return f.read()

class SalesReportTest(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.db.executescript(read_sql("sample_data.sql"))

    def tearDown(self):
        self.db.close()

    def use_rows(self, rows):
        self.db.execute("DELETE FROM sales")
        self.db.executemany(
    "INSERT INTO sales (title, genre, copies, unit_price) VALUES (?, ?, ?, ?)",
    rows
)

    def report(self):
        return self.db.execute(read_sql("sales_report.sql")).fetchall()

    def test_example_from_the_task(self):
        self.use_rows([
            ("A", "Crime", 3, 20.0),
            ("B", "Crime", 5, 10.0),
            ("C", "Crime", 1, 20.0),
            ("D", "Poetry", 2, 15.0),
            ("E", "Poetry", 1, 25.0)
        ])

    def test_sample_data_report(self):
        self.assertEqual(self.report(), [("Sci-Fi", 210, 2, 1),
                                         ("Crime", 130, 3, 2),])

    def test_revenue_multiple_copies_by_price(self):
        self.use_rows([("A", "Travel", 7, 20.0)])
        genre, revenue, count, rank = self.report()[0]
        self.assertEqual(revenue, 140)
        self.assertEqual(count, 1)

    def test_genres_ranked_highest_revenue_first(self):
        self.use_rows([
            ("A", "Mid", 1, 200.0),
            ("B", "Top", 1, 500.0),
            ("C", "Low", 1, 150.0),
        ])
        self.assertEqual(self.report(), [
            ("Top", 500, 1, 1),
            ("Mid", 200, 1, 2),
            ("Low", 150, 1, 3),
        ])

    def test_revenue_of_exactly_100_is_executed(self):
        self.use_rows([
            ("A", "Cooking", 4, 25.0),
            ("B", "History", 1, 100.5),
        ])

        self.assertEqual(self.report(), [("History", 100.5, 1, 1)])

    def test_tied_genres_share_a_rank(self):
        self.use_rows([
            ("A", "Romance", 1, 300.0),
            ("B", "Fantasy", 1, 150.0),
            ("C", "Fantasy", 1, 150.0),
            ("D", "Horror", 1, 120.0),
        ])
        self.assertEqual(self.report(), [
            ("Fantasy", 300, 2, 1),
            ("Romance", 300, 1, 1),
            ("Horror", 120, 1, 3),
        ])

    def test_no_genre_above_100_gives_empty_report(self):
        self.use_rows([("A", "Poetry", 1, 10.0)])
        self.assertEqual(self.report(), [])

if __name__ == "__main__":
    unittest.main()

