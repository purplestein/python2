goods = []
while input('Добавить товар?') == 'да':
    number = int(input("Введите номер товара: "))
    features = {}
    feature_key = input("Введите название товара: ")
    feature_value = input("Введите количество товара: ")
    features[feature_key] = feature_value
    feature_unit = input("Введите единицы измерения товара: ")
    features['ед'] = feature_unit
    goods.append(tuple([number, features]))
print(goods)
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
            analitics[feature_key] = [feature_value]
print(analitics)
