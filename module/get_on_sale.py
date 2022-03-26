import pandas as pd

def get_on_sale() -> pd.DataFrame:
    table = pd.read_csv('data/on_sale.csv', dtype='str', usecols= ['ISBN', 'Titolo', 'Autori', 'Venditore', 'Prezzo'])
    return table
