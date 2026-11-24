

velkobalenie = 12
pocet_kusov = input('Zadajte pocet kusov:')
pocet_kusov = int(pocet_kusov)

pocet_plnych_baleni = pocet_kusov // velkobalenie
zostatok_na_sklade = pocet_kusov % velkobalenie

print(f'pocet plnych baleni {pocet_plnych_baleni} a zostatok na sklade {zostatok_na_sklade}')