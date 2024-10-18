"""Admita que uma instituição financeira tenha adquirido um lote de LTN em mercado primário. O prazo do título é de 108 dias corridos,
correspondendo a 76 dias úteis. A instituição define uma taxa over anual de 11,8%. Pede-se:
a. PU equivalente (valor de face igual a R$ 1.000,00);
b. Qual é a taxa de retorno do investimento (ao período)? """

ltn = 1000
du = 76
aao = 11.8 / 100

PV = ltn / (1 + aao) ** (76/252)

print(f'O P.U de compra por quantidade de LTN foi R$ {PV:.2f}.')
