str_a = input ('Gib eine Zahl ein:')
int_a = int (str_a)
# if bedingung mit == vergleichen : 
if int_a == 0: # hier wird einmal abgefragt nach nicht 0
    # konzept der Blöcke: nach if kommt Block1, dann else: Block2;
    #bei True kommt Block1 bei false kommt Block2
    #ein Block ist immer nach rechts versetzt, dann tab weglöschen um Block ende.
    int_a = int (input('Nicht Null'))
b = int (input('noch eine Zahl:'))
#while bedingung:
#   anweisung
while b == 0:
    print ("Division durch Null nicht möglich, bitte andere Zahl eingeben")
    b = int (input('Nicht Null')) # hier so oft fragen bis keine Null mehr
print ("Die Summe der Zahlen ist:", int_a + b)
print ("Die Differenz der Zahlen ist:", int_a - b)
print ("Das Produkt der Zahlen ist:", int_a * b)
print ("Der Quotient der Zahlen ist:", int_a / b)
print ("a^b=", pow(int_a, b))
print ("a^b=", int_a ** b)