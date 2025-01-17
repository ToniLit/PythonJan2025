# baza de date
EUR=4.97
USD=4.87
HUF=0.012
PLN=1.16
 
# Input_data
amnt =input("waht is your price? :")
amnt = int(amnt)
# EUR = int(EUR)
# USD = int(USD)

# Calculation
final_EUR = amnt * EUR
final_USD = amnt * USD
final_HUF = amnt * HUF
final_PLN = amnt * USD

# Vizualizare
print ("Tota in USD:", final_USD)
print ("Total in EUR:", final_EUR)
print ("Total in HUF:", final_HUF)
print ("Total in PLN:", final_PLN)