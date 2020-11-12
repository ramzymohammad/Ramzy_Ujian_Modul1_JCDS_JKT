# User menginput '1234567890' maka akan diubah ke '(123) 456-7890'

number = input('masukkan nomer anda: ')
number_1 = [char for char in number]  #[1,2,3,4,5,6,7,8,9,0]
tuple_1 = []
tuplex = ()
number_2 = []
number_3 = ['-']
number_4 = []
number_5 = []
for i in range(len(number)):
    if i == 0 or i == 1 or i == 2:
        tuple_1.append(number_1[i])
    elif i == 3 or i == 4 or i == 5:
        number_2.append(number_1[i])
    else:
        number_3.append(number_1[i])
print(tuple_1)
tuple_2 =''.join(tuple_1)
print(tuple_2)
tuple_3 = int(tuple_2)
tuplex = tuplex + (tuple_3,)
print(tuplex)
number_4.append(str(tuplex))
number_4
number_2

number_5 = number_4 + number_2 + number_3
print(number_5)
number_6 = ''.join(number_5)
print(number_6)
