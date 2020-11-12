def moveZeros(mantap):
    list_1 = mantap
    list_3 = list_1.copy()
    list_2 = []
    a_list = []
    for i in list_1:
        if i == 0:
            list_3.remove(0)
    print(list_3)

    for i,j in enumerate(list_1):
        print(i,j)
        if j == 0:
            list_2.append(i)
    print(list_2)

    for z in (list_2):
        list_3.append(list_1[z])
    print(list_3)
a = [1,0,4,0,5,0,7,1]
moveZeros(a)