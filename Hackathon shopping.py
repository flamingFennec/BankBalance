msi_rtxa5000_price = 4199.35
gigabyte_aero_price = 4295.54
razer_blade15_price = 3696.99
asus_zephyrus_m16_price = 1849.79

This = msi_rtxa5000_price + gigabyte_aero_price + razer_blade15_price + asus_zephyrus_m16_price 

Average = This / 4

def Laptop_prices(most_expensive, least_expensive, Ave):
    print(f"""The most expensive laptop amount is: {least_expensive}
    The least expensive laptop amount is {most_expensive}
    The rounded price for the MSI RTX 5000 is: {round(msi_rtxa5000_price)}
    The rounded price for the Gigabyte Aero is: {round(gigabyte_aero_price)}
    The rounded price for the Razer Blade 15 is: {round(razer_blade15_price)}
    The rounded price for the Asus Zephyrus is: {round(asus_zephyrus_m16_price)}
    The average price of all computers is: {Ave}""")

Laptop_prices(msi_rtxa5000_price, asus_zephyrus_m16_price, Average)