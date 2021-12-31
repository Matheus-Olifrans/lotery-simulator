import random

print('escolha os numeros sem repetir\n')
loteria = {int(input(f'digite o {a}° numero: ')) for a in range(1,7)}


class Numeros:
  def __init__(self, lotery):
    self.numbers = set(random.sample(range(1,61),6))
    self.acertado = self.numbers.intersection({8 ,9 ,32, 52 ,53, 57})


Matheus = Numeros(loteria)
#Samuel = Numeros(loteria)
print(f'numeros escolhidos para Matheus são "{Matheus.numbers}"\n')
#print(f'numeors escolhidos para Samuel são "{Samuel.numbers}"\n')
print(f'numeros corretos de Matheus foram "{Matheus.acertado}" acertando {len(Matheus.acertado)}\n')

#print(f'numeros corretos de Samuel foram "{Samuel.acertado}" acertando {len(Samuel.acertado)}')
