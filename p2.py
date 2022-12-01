text = 'Введите символы:'
print(text)
text_list = list(input())
for i in range(0, len(text_list)-1, 2):
    text_list[i],text_list[i+1] =text_list[i+1],text_list[i]

print(text_list)