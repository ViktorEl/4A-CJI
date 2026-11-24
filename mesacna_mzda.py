# Vytvorte program, v ktorom používateľ zadá 
# počet odpracovaných hodín za mesiac
# hodinovú mzdu a vypočíta celkovú mesačnú mzdu. 

print('Program na vypocitanie mesacnej mzdy')

hodiny = input('Zadajte pocet odpracovanych hodin:')
hodiny = float(hodiny)

hodinova_mzda = input('Zadajte hodinovu mzdu:')
hodinova_mzda = float(hodinova_mzda)

celkova_mesacna_mzda = hodiny * hodinova_mzda

# priklad vystupu: Vasa mesacna mzda je 1200 eur. 
print(f'Vasa mesacna mzda je {celkova_mesacna_mzda} eur')
