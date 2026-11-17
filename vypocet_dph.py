print('Program na vypocitanie sumy s DPH')

suma_bez_dph = input('Zadajte sumu bez dph:')
suma_bez_dph = float(suma_bez_dph)  # desatinne cislo

suma_s_dph = suma_bez_dph * 1.23
# print(suma_s_dph)
print(f'Vasa suma s DPH je {suma_s_dph}') # alternativny vypis pomocou f-string alebo formatovany string


