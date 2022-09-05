#   Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x=int(input('введите значение Х: '))
y=int(input('введите значение Y: '))
z=int(input('введите значение Y: '))
boolean_1=not (x or y or z)
boolean_2= not (x) or not (y) or not (z)
result=boolean_1==boolean_2
print(result)


