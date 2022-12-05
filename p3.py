wel = "Введите номер месяца: "
print(wel)
text = int(input())
my_dict = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}
for keys in my_dict:
    if text in my_dict[keys]:
        text = keys
        break
print(text)

wel = "Введите номер месяца: "
print(wel)
month = int(input())
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
months_num = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1]
if month < 1 or month > 12:
    print('There is not such month')
else:
    print(seasons[months_num[month - 1] - 1])
