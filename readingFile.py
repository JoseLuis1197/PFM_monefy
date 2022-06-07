import pandas
from functions import fnSum

data = pandas.read_csv(\
                        filepath_or_buffer="C:/Users/P029700/Downloads/monefy-2022-06-07_09-13-13.csv",\
                        sep=";",\
                        decimal=".")

##Sumar entretenimiento

sumHome = 0
contador = 0

limite = data["date"].index
_totalAmount = 0

while contador < limite.size:  

    _date = data["date"][contador]    
    _month = int(_date[3:5])
    _year = int(_date[6:])
    _amount = float(data["amount"][contador])
    _category = data["category"][contador]    

    fnSum(_month,_year,_amount,_category,_totalAmount)            

    contador += 1


