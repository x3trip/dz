import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
from sklearn.preprocessing import OneHotEncoder
data = pd.DataFrame({'whoAmI':lst})
# Создаем экземпляр класса OneHotEncoder
one_hot_encoder = OneHotEncoder(sparse=False)
# Преобразуем столбец 'Цвет' в формат "one hot"
one_hot_encoded = one_hot_encoder.fit_transform(data[['whoAmI']])
# Создаем DataFrame с преобразованными данными
one_hot_encoded_df = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(['whoAmI']))
print(one_hot_encoded_df)
