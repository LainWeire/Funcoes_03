# - Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.


def calcular_area_base(raio):
    area = (3.14 * (raio**2))
    return area

a = int(input("Digite o raio do circulo:  "))
raio = calcular_area_base(a)

def calcular_volume_cilindro(altura):
    volume = (calcular_area_base(a) * altura)
    return volume

h = int(input("Digite a altura do cilindro:   "))
volume2 = calcular_volume_cilindro(h)

print (raio)
print (volume2)