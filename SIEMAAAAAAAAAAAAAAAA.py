# list = []
# i = 0
# for i in range(10):
#     if i < 5:
#
#         x = int(input("Podaj pierwszy składnik mnożenia : "))
#         y = int(input("Podaj drugi składnik mnożenia : "))
#         z=x*y
#         if z%2==0:
#             list.append(z)
#             i +=1
#     else:break
# print(list)
x = -4
while(x<=4):
    y=2*x**2-5*x-8
    print(f'f({x}),{y}')
    x=x+0.5

print('koniec')