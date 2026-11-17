print('program na vypocet DPH podla zadanej sadzby')

suma_bez_dph = input('Zadajte sumu bez DPH:')
suma_bez_dph = float(suma_bez_dph)

sadzba = input('Zadajte sadzbu DHP:')
sadzba = float(sadzba)

dph = suma_bez_dph * sadzba / 100
suma_s_dph = suma_bez_dph + dph

print(f'Suma s DPH je {suma_s_dph}')


