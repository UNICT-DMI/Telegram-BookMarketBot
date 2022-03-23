import pandas as pd

def get_on_sale():
    table = pd.read_csv('data.csv', dtype='str', usecols= ['ISBN', 'Titolo', 'Autori', 'Venditore', 'Prezzo'])
    return table