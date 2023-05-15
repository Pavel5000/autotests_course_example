# 1 задание. Периметр квадрата, площадь, диагональ. +
a = 4
b = a
c = a
d = a
print("периметр квадрата", a + b + c + d)
print("площадь квадрата", a * b)
print("диагональ квадрата", (a ** 2 + b ** 2) ** .5)

#2 Корни квадратного уровнения до 2 знаков после запятой.
a = 8.1
b = 4.2
c = 2
# D = b ** 2 - 4 * a * c
x1 = (-b + d ** (1 / 2)) / 2 * a
x2 = (-b - d ** (1 / 2)) / 2 * a
print("первый корень", round(x1, 2))
print("второй корень", round(x2, 2))

#3 Объеденить 2 строки, разделить пробелом, поменять первые 2 символа первой строки на вторую.
string1 = "Часто узким переулком"
string2 = "проходил я в тёмный дом"
y = string1.replace("Ча", "пр")
z = string2.replace("пр", "Ча")
print(string1, string2)
print(y)
print(z)

#4 Вывести название файла без расширения, название диска, корневую папку
string1 = r"C:\python\name.txt"
print(string1[:14])
print(string1[:1])
print(string1[3:-9])

#5 a и b. Вывести на экран их сумму и произведение.
a = 3
b = 2
print("""{} + {} = {} """. format(a, b, a + b))
print("""{} * {} = {} """. format(a, b, a * b))

#6 Удаление символов из строки.
string11 = "Удаление символов из строки"
print(string11[::2])

#7 2 строки из неповторяющихся симоволов.
first_string = "wtf"
second_string = "brick quz jmpy veldt whangs fox"
index1 = second_string.find(first_string[0])
index2 = second_string.find(first_string[1])
index3 = second_string.find(first_string[2])
min_index = min(index1, index2, index3)
max_index = max(index1, index2, index3)
print(second_string[min_index:max_index])

