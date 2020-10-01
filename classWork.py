# def shift ( list , b ):
    # if b < 0 :
    # return list[-b:]+list[:-b]
    # else:
    #     return list[len(list)-b:]+list[:len(list)-b]
#
# f = [1,2,3,4,5,6,7]
# print(shift(f, 3))
# print(shift(f, -3))

# def equal_diff (list) :
#     b = True
#     scale = list[1]-list[0]
#     for i in range(len(list)-2):
#         if list[i + 2]-list[i + 1] != scale :
#             b = False
#     return b
#
# f = [5,10,15,20,24]
# print(equal_diff(f))

# def intersection(list1, list2):


# def myfunc2(array1 , **kwargs):
#     e1 = kwargs.get('root', None)
#     e2 = kwargs.get('sum', None)
#     e3 = kwargs.get('absolut', None)
#     result = array1
#
#     if e3 :
#         result = [abs(x) for x in result]
#     if e1  :
#         result = [x ** 0.5 for x in result]
#     if e2 :
#         result = sum(array1)
#     return result
#
#
#
# print(myfunc2([4,1,9,16,-25] , root=False , sum=False , absolut=True))


def intersection(arr1 , arr2 , result):

    arr1 = set(arr1)
    for i in arr1 :
        for e in arr2 :
            if i == e :
                result.append(i)
    print(result)

a = [1,2,3,4,5,1,5]
b = [1,2,5,5,6]
c = []
intersection(a, b, c )