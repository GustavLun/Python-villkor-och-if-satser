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
if price >= level1 and price < level2:
    print("Grattis! Du har avancerat till nivå 1 och du får 10% rabatt.")
    discount = discount + 10
if price >= level2:
    print("Grattis Du har avancerat till nivå 2 och får 25% rabatt")
    discount = discount + 25

final_price = price * (100 -discount) / 100
print("Efterrabatter blir priset....." +str(final_price))

# 1.Vad är syftet med koden?
# Syftet med koden är att baserat på värdet av det kunden betalar ge kunden olika nivåer som direkt är kopplat till rabatt på köp.

# 2.Testkör koden med några olika värden.
# just nu funkar inte koden som tänkt, värdet blir mer än vad kunden väljer att handla för.

# 3.Finns det några direkta fel i koden? (fel som gör att programmet kraschar)
#Inget gör så programmet kraschar.

# 4.Finns det logiska fel? (programmet gör något annat än det är tänkt)
#Ja, just nu kommer rabatter från både level 1 och två att köras, man behöver speficifera mer att level 1 är från 100 och mindre än 300.
# Man skulle också behöva en annan uträkning för att visa köparen priset efter rabatten och inte värdet på rabatten

# 5.Diskutera möjliga lösningar på felen ni hittat.
# Vi bör sätta ett tak på level 1 till under 300, vi skulle även behöva lägga till 100 innan discount och subtrahera discount innan vi delar allt på 100 för att få aktuellt pris efter rabatten.

# 6.Diskutera möjliga förbättringar på koden.
# Man skulle kunna ta bort variablarna för levels och bara specifierar speficikt pristak för de olika rabatterna i if satsen.