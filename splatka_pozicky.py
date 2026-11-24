# Vytvorte program, v ktorom používateľ zadá 
# celkovú sumu pôžičky a počet mesiacov za 
# koľko chce túto pôžičku splatiť a program 
# vypočíta a vypíše výšku mesačnej splátky (bez úrokov).

suma = input('Zadajte sumu pozicky:')
suma = float(suma)

pocet_mesiacov = input('Zadajte pocet mesiacov:')
pocet_mesiacov = int(pocet_mesiacov)

vyska_splatky = suma / pocet_mesiacov
print(vyska_splatky)