import pandas as pd
from module.shared import SHOP_DB_PATH

def get_on_sale() -> pd.DataFrame:
    table = pd.read_csv(SHOP_DB_PATH, dtype='str', usecols= ['ISBN', 'Titolo', 'Autori', 'Venditore', 'Prezzo'])
    return table
