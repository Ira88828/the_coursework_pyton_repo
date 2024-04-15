# Шаг 1. Для начала необходимо создать DataFrame.
# Шаг 2. Преобразуем заданные значения столбца whoAml в вид one not, 
# без применения метода pd.get_dumies путем алгоритмического преобразования 
# с ипользованием лямбда функции.



import pandas as pd
data = pd.DataFrame({'whoAmI': lst})

data['is_robot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
data['is_human'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)

data.head()