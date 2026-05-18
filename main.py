# print("Hello if satser")
#
# Balance = int(input(" Input current balance "))
#
# if Balance > 0:
#     print("Balance is currently " +str(Balance))
# elif not Balance:
#     print("Balance is negative ")
#
# if Balance >= 100:
#     print("You are pretty rich")
# if 5<= Balance <=99:
#     print("You are medelklass")
# else:
#     print("You are very poor")

# Uppgift 1
is_member = False
level1 = 100
level2 = 300
discount = 0

price = input(" Välkommen, köp något dyrt" )
price = float(price)
if price > level1:
    print("Grattis! Du har avancerat till nivå 1 och du får 10% rabatt.")
    discount = discount + 10
if price >= level2:
    print("Grattis Du har avancerat till nivå 2 och får 25% rabatt")
    discount = discount + 25

final_price = price + (100 - discount) / 100
print("Efterrabatter blir priser....." +str(final_price))