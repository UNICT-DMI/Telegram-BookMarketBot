def find_book(message, dataframe):
    found = False
    v = []
    n = -1
    if(len(dataframe.columns) == 5):
        for i in range(len(dataframe)):
            if(message.lower() in str(dataframe['ISBN'][i]).lower() or  message.lower() in dataframe['Titolo'][i].lower() or message.lower() in dataframe['Autori'][i].lower()):
                found = True
                v.append(i)
        if(found):
            return(found, v)
        else:
            return(found, -1)
    else:
        for i in range(len(dataframe)):
            if(message.lower() in str(dataframe['ISBN'][i]).lower()):
                found = True
                return(found, i)
        return(found, -1)