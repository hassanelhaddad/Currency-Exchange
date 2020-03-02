#=============================================
#currency.py
#convert currency to currency
#Hassan El-Haddad
#2/3/20
#=============================================




userFromCurrency = input("What currency do you want to convert from ")

if (userFromCurrency == "USD"):
    userToCurrency = input("What currency do you want to convert to ")
    if(userToCurrency == "EUR"):
        usdValue = float(input("Enter a USD amount:\n"))
        eurAns = usdValue * 0.90231
        eurAns = round(eurAns, 2)
        print(eurAns)
    elif(userToCurrency == "GBP"):
        usdValue = float(input("Enter a USD amount:\n"))
        gbpAns = usdValue * .81752
        gbpAns = round(gbpAns, 2)
        print(gbpAns)
    elif(userToCurrency == "INR"):
        usdValue = float(input("Enter a USD amount:\n"))
        inrAns = usdValue * 71.7937
        inrAns = round(inrAns, 2)
        print(inrAns)
    elif(userToCurrency == "AUD"):
        usdValue = float(input("Enter a USD amount:\n"))
        audAns = usdValue * 1.48338
        audAns = round(audAns, 2)
        print(audAns)
elif(userFromCurrency == "EUR"):
    userToCurrency = input("What currency do you want to convert to ")
    if(userToCurrency == "USD"):
        eurValue = float(input("Enter a EUR amount:\n"))
        usdAns = eurValue * 1.10827
        usdAns = round(usdAns, 2)
        print(usdAns)
    elif(userToCurrency == "GBP"):
        eurValue = float(input("Enter a EUR amount:\n"))
        gbpAns = eurValue * 0.90603
        gbpAns = round(gbpAns, 2)
        print(gbpAns)
    elif(userToCurrency == "INR"):
        eurValue = float(input("Enter a EUR amount:\n"))
        inrAns = eurValue * 79.5668
        inrAns = round(inrAns, 2)
        print(inrAns)
    elif(userToCurrency == "AUD"):
        eurValue = float(input("Enter a EUR amount:\n"))
        audAns = eurValue * 1.64399
        audAns = round(audAns, 2)
        print(audAns)
elif(userFromCurrency == "GBP"):
    userToCurrency = input("What currency do you want to convert to ")
    if(userToCurrency == "USD"):
        gbpValue = float(input("Enter a GBP amount:\n"))
        usdAns = gbpValue * 1.22321
        usdAns = round(usdAns, 2)
        print(usdAns)
    elif(userToCurrency == "EUR"):
        gbpValue = float(input("Enter a GBP amount:\n"))
        eurAns = gbpValue * 1.10371
        eurAns = round(eurAns, 2)
        print(eurAns)
    elif(userToCurrency == "INR"):
        gbpValue = float(input("Enter a GBP amount:\n"))
        inrAns = gbpValue * 87.8187
        inrAns = round(inrAns, 2)
        print(inrAns)
    elif(userToCurrency == "AUD"):
        gbpValue = float(input("Enter a GBP amount:\n"))
        audAns = gbpValue * 1.81449
        audAns = round(audAns, 2)
        print(audAns)
elif(userFromCurrency == "INR"):
    userToCurrency = input("What currency do you want to convert to ")
    if(userToCurrency == "USD"):
        inrValue = float(input("Enter a INR amount:\n"))
        usdAns = inrValue * 0.01393
        usdAns = round(usdAns, 2)
        print(usdAns)
    elif(userToCurrency == "EUR"):
        inrValue = float(input("Enter a INR amount:\n"))
        eurAns = inrValue * 0.01257
        eurAns = round(eurAns, 2)
        print(eurAns)
    elif(userToCurrency == "GBP"):
        inrValue = float(input("Enter a INR amount:\n"))
        gbpAns = inrValue * 0.01139
        gbpAns = round(gbpAns, 2)
        print(gbpAns)
    elif(userToCurrency == "AUD"):
        inrValue = float(input("Enter a INR amount:\n"))
        audAns = inrValue * 0.02066
        audAns = round(audAns, 2)
        print(audAns)
elif(userFromCurrency == "AUD"):
    userToCurrency = input("What currency do you want to convert to ")
    if(userToCurrency == "USD"):
        audValue = float(input("Enter a AUD amount:\n"))
        usdAns = audValue * 0.67414
        usdAns = round(usdAns, 2)
        print(usdAns)
    elif(userToCurrency == "EUR"):
        audValue = float(input("Enter a AUD amount:\n"))
        eurAns = audValue * 0.60828
        eurAns = round(eurAns, 2)
        print(eurAns)
    elif(userToCurrency == "GBP"):
        audValue = float(input("Enter a AUD amount:\n"))
        gbpAns = audValue * 0.55112
        gbpAns = round(gbpAns, 2)
        print(gbpAns)
    elif(userToCurrency == "INR"):
        audValue = float(input("Enter a GBP amount:\n"))
        inrAns = audValue * 48.3987
        inrAns = round(inrAns, 2)
        print(inrAns)
    
