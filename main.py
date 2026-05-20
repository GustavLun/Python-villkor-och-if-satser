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

# # Uppgift 1
# is_member = False
# level1 = 100
# level2 = 300
# discount = 0
#
#
# price = input(" Välkommen, köp något dyrt" )
# check_membership = input(" Är de medlem ? Svar med ja eller nej ")
# if check_membership == "ja":
#     is_member =True
# else:
#     is_member = False
# price = float(price)
# if (is_member == True) and price >= level1 and price < level2:
#     print("Grattis! Du har avancerat till nivå 1 och du får 10% rabatt.")
#     discount = discount + 10
# elif (is_member == True) and price >= level2 :
#     print("Grattis Du har avancerat till nivå 2 och får 25% rabatt")
#     discount = discount + 25
# else:
#     print("Tyvärr du får inga rabatter")
#
# final_price = price * (100 -discount) / 100
# print("Ditt slutpris blir....." +str(final_price))

# 1.Vad är syftet med koden?
# Syftet med koden är att baserat på värdet av det kunden betalar ge kunden olika nivåer som direkt är kopplat till rabatt på köp.

# 2.Testkör koden med några olika värden.
# just nu funkar inte koden som tänkt, värdet blir mer än vad kunden väljer att handla för.

# 3.Finns det några direkta fel i koden? (fel som gör att programmet kraschar)
# Finns ett fel, sista printen kan inte printas eftersom det är en float men vi försöker skriva ut en sträng som inte är specificerat.
#is_member används inte i koden alls.

# 4.Finns det logiska fel? (programmet gör något annat än det är tänkt)
#Ja, just nu kommer rabatter från både level 1 och två att köras, man behöver speficifera mer att level 1 är från 100 och mindre än 300.
# Man skulle också behöva en annan uträkning för att visa köparen priset efter rabatten och inte värdet på rabatten

# 5.Diskutera möjliga lösningar på felen ni hittat.
# Först bör vi sätta ännu en input för att verifiera om köparen är medlem eller inte, därav endast inkludera köparen i if satsen om is_member = true.
# Vi bör sätta ett tak på level 1 till under 300 för att separera de olika rabatter så de ej adderas.
# Specificera i sista printen att floaten vi vill skriva ut skall vara en str istället för float eller gör en f sträng.


# 6.Diskutera möjliga förbättringar på koden.
# Genom att lägga till en funktion för att checka om köparen är medlem eller ej kan vi inkludera is_member som en variabel som skall uppfyllas för att köra if satserna på rabatten.
# Därav kan vi förfina och skriva om if satserna för att ge mer kontroll

# 2 Balder

# rider_height = int(input("Hur lång är du? Svara i CM "))
# if rider_height < 130:
#     print(" Tyvärr du är för kort och får ej åka ")
# else:
#     print(" Du är lång nog för att åka ")

    # Vi måste testa 3 värden för att kunna kolla om exakt värde fungerar samt över eller under. Det finns totalt 3 scenarios att testa.
    # Vi använder just dessa värden för att ett värde testar under gränsen, en den exakta gränsen och den sista över gränsen.
    # Att lägga till 129 CM är onödigt och testas redan i genom att skriva 121.

    # 3 Sportresultat

#Version1
# goals_tottenham = int(input("Hur många mål gjorde Tottenham? "))
# goals_liverpool = int(input("Hur många mål gjorde Liverpool? "))
#
# if goals_tottenham > goals_liverpool:
#         print(" Matchen är över, räknar ut resultatet ")
#         print(f" Tottenham gjorde {goals_tottenham} mål och Liverpool gjorde {goals_liverpool} ")
#         print(f"Tottenham gjorde {goals_tottenham - goals_liverpool} mer mål än Liverpool")
#         print(" Tottenham vann! ")
# elif goals_tottenham < goals_liverpool:
#         print(" Matchen är över, räknar fram resultatet")
#         print(f"Tottenham gjorde {goals_tottenham} och Liverpool gjorde {goals_liverpool}")
#         print(f" Liverpool gjorde {goals_liverpool - goals_tottenham} mer mål än Tottenham)")
#         print(" Liverpool vann! ")
# else:
#          print(" Matchen är över, räknar fram resultatet")
#          print(f" Tottenham gjorde {goals_tottenham} och Liverpool gjorde {goals_liverpool} ")
#          print(" Its a tie! ")

# 4 Temperaturomvandling
# grader_celsius = int(input(" Skriv in antal grader celsius "))
# farenheit = grader_celsius * 9 / 5 + 32
# print(f" Det är {grader_celsius} vilket i Farenheit är {farenheit}")

Temp_formula = input(" Använder du celsius eller farenheit? ")

