# программа считывает количество учеников и кол-во яблок и выводит сколько целых яблок останется не разделенными между учениками
number_of_pupils = int(input("Введите количество школьников: "))
number_of_apples = int(input("Введите количество яблок: "))
print(number_of_apples % number_of_pupils)
