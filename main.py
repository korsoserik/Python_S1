a = int(input("Adja meg az 'a' oldal hosszúságát méterben: "))
b = int(input("Adja meg a 'b' oldal hosszúságát méterben: "))
c = int(input("Adja meg a 'c' oldal hosszúságát méterben: "))
m_a = int(input("Adja meg az 'a' oldalra merőleges magasságot méterben: "))
if ((a < (b + c)) and (b < (a + c)) and (c < (a + b))):
    haromszog_kerulet = a+b+c
    haromszog_terulet = (a * m_a) / 2
else:
    print("Nem szerkeszthető!")
print("A Háromszög területe:", haromszog_terulet, ("m2"))
print("A Háromszög kerulete:", haromszog_kerulet, ("m"))
