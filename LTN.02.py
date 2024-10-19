"""Uma Letra do Tesouro Nacional é cotada a 10,25% a.a.o. para 130 dias úteis. Pede se:
a. A taxa ao dia útil;
b. O PU do título;
c. A taxa over mês."""

ltn = 1000
du = 130
aao =  0.1025

#Resolução letra A
dia = ((1 + aao) ** (1/252)) -1
print(f'A taxa ao dia útil é {dia * 100:.4f}%')
