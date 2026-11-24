import math

print('Program na zistenie poctu krabic')



pocet_vyrobenych_kusov = input('Zadajte pocet vyrobenych kusov')
pocet_vyrobenych_kusov = int(pocet_vyrobenych_kusov)

kapacita_krabice = input('Zadajte kapacitu jednej krabice:')
kapacita_krabice = int(kapacita_krabice)

pocet_krabic = pocet_vyrobenych_kusov / kapacita_krabice
# pocet_krabic = math.ceil(pocet_krabic) # zaokruhlujem na cele cislo nahor

pocet_krabic = math.floor(pocet_krabic) # zaokruhlujem na cele cislo nadol

print(pocet_krabic)