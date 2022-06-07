argsDate = []

def fnSum(month,year,amount,category,totalAmount):
    
    for a in range(2021,2022,1):
        for m in range(1,12,1):
            if  category == "Casa":    
                totalAmount = totalAmount + amount
                argsDate.append(month,year,totalAmount)
            break  
        break  