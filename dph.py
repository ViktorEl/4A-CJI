
suma = input('Zadajte sumu bez DPH:')
suma = float(suma)

dph = input('Zadajte vysku dph:')
dph = float(dph)

dan = suma * (dph / 100)
suma_s_dph = suma + dan

print('Vasa dan je:', dan)
print('Suma s DPH je:', suma_s_dph)
