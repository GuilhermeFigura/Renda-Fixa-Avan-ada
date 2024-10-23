#Quantos dias úteis tem entre 23/12/2024 e 23/11/2024?

import pandas as pd
from datetime import datetime

def dias_uteis_pandas(data_inicial, data_final):
    # Cria um range de datas
    dias = pd.date_range(start=data_inicial, end=data_final)
    # Conta apenas dias de segunda a sexta (0-4)
    dias_uteis = len(dias[dias.dayofweek < 5])
    return dias_uteis

# Para usar:
data1 = datetime(2024, 10, 23)  # 23/10/2024
data2 = datetime(2024, 11, 23)  # 23/11/2024

dias = dias_uteis_pandas(data1, data2)
print(f"Dias úteis: {dias}")
