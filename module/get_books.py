import pandas as pd

def get_books():
    table = pd.read_csv('books.csv', dtype='str', usecols= ['ISBN', 'Titolo', 'Autori'])
    return table