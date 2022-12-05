wel = "Введите символы через пробел:"
print(wel)
text = input()
new_text = text.split(' ')
for i, el in enumerate(new_text, 1):
    if len(el) > 10:
        print('%s\r\n%s' % (i[:10], i[11:]))
        continue
    print(f"{i}  {el}")
