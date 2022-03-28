import pandas as pd
from module.get_on_sale import get_on_sale
from module.shared import SHOP_DB_PATH

def add_item(isbn: str, title: str, authors:str, username:str, price:str) -> None:
    df = get_on_sale()
    new_row = pd.DataFrame({'ISBN':str(isbn),'Titolo':str(title), 'Autori':str(authors), 'Venditore':str(username), 'Prezzo':str(price)}, index=[len(df)])
    df = pd.concat([df, new_row])
    df.to_csv(SHOP_DB_PATH)
