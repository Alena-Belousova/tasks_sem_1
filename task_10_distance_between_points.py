#Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.
x_A=int(input('введите каординату точки А (по оси ОХ): '))
y_A=int(input('введите каординату точки А (по оси ОY): '))
x_B=int(input('введите каординату точки B (по оси ОХ): '))
y_B=int(input('введите каординату точки B (по оси ОY): '))
# ((xB-xA)^2+((YB-YA)^2)^0.5
distance=((x_B-x_A)**2)+((y_B-y_A)**2)**0.5
print(' A(',x_A,';',y_A,')\n B(',x_B,';',y_B,')')
print('расстояние равно: ',distance)

