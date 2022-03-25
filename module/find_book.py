from typing import Tuple
from pandas import DataFrame

def find_book(message: str, dataframe: DataFrame) -> Tuple:
    v = []
    if len(dataframe.columns) == 5:
        for i in range(len(dataframe)):
            if(message.lower() in str(dataframe['ISBN'][i]).lower() or  message.lower() in dataframe['Titolo'][i].lower() or message.lower() in dataframe['Autori'][i].lower()):
                v.append(i)
        if len(v) > 0:
            return(True, v)
        
        return(False, -1)
    
    for i in range(len(dataframe)):
        if message.lower() in str(dataframe['ISBN'][i]).lower():
            return(True, i)
    return(False, -1)
