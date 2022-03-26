import pandas as pd

def get_books() -> pd.DataFrame:
    table = pd.read_csv('data/books_db.csv', dtype='str', usecols= ['ISBN', 'Titolo', 'Autori'])
    return table
