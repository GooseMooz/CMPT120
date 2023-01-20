smol_r = float(input("Input diameter of the small pizza: ")) / 2
smol_price = float(input("Input the price of the small pizza: "))
larg_r = float(input("Input the diameter of the large pizza: ")) / 2
larg_price = float(input("Input the price of the large pizza: "))
smol_area = 3.1415 * (smol_r ** 2)
larg_are = 3.1415 * (larg_r ** 2)
smol_ppi = smol_area / smol_price
big_ppi = larg_are / larg_price
if smol_ppi < big_ppi:
    print("The smol pizza is better.")
else:
    print("The larg pizza is better.")
