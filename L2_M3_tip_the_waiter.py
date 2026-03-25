def amount(bill_amount,tip_amount):
   result= bill_amount*(1+0.01*tip_amount)
   result=round(result,2)
   print(result)
amount(150,10)
    
    