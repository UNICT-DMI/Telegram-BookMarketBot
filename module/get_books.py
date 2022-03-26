import pandas as pd
from module.shared import BOOKS_DB_PATH

def get_books() -> pd.DataFrame:
    table = pd.read_csv(BOOKS_DB_PATH, dtype='str', usecols= ['ISBN', 'Titolo', 'Autori'])
    return table
