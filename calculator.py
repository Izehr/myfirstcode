elements = input("Введите выражение:").split(" ")
i = 0
while i != len(elements):
    if elements[i] == '#':
       result = float(elements[i - 1]) ** (1 / float(elements[i + 1]))
       elements.pop(i + 1)
       elements[i] = result
       elements.pop(i - 1)
       continue
    elif elements[i] == '^':
       result = float(elements[i - 1]) ** float(elements[i + 1])
       elements.pop(i + 1)
       elements[i] = result
       elements.pop(i - 1)
       continue
    i = i + 1
i = 0
while i != len(elements):
    if elements[i] == '/':
       result = float(elements[i - 1]) / float(elements[i + 1])
       elements.pop(i + 1)
       elements[i] = result
       elements.pop(i - 1)
       continue
    elif elements[i] == '*':
       result = float(elements[i - 1]) * float(elements[i + 1])
       elements.pop(i + 1)
       elements[i] = result
       elements.pop(i - 1)
       continue
    i = i + 1
i = 0
while i != len(elements):
    if elements[i] == '+':
       result = float(elements[i - 1]) + float(elements[i + 1])
       elements.pop(i + 1)
       elements[i] = result
       elements.pop(i - 1)
       continue
    elif elements[i] == '-':
       result = float(elements[i - 1]) - float(elements[i + 1])
       elements.pop(i + 1)
       elements[i] = result
       elements.pop(i - 1)
       continue
    i = i + 1

print(f'Результат:{elements[0]}')

