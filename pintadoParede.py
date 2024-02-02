# Inputar os dados de altura e largura obtidas da parede
altura = int(input('Digite altura da parede: '))
largura = int(input('Digite largura da parede: '))
# Cálculo para medir área da parede 
area = (altura * largura)
# Cálculo para medir quantidade de tinta necessária, considerando que cada lata pinta 2m²
tinta = area / 2

print(f'O cômodo tem {area} m² de área, e serão necessários {tinta} litros de tinta')