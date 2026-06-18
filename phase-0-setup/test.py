



# def addnumbers(a,b):
#     return (a+b)

# result = addnumbers(5,3)

# print(result)


# list=[1,2,3,4,5]
# for index, value in enumerate(list):
#     print(index,value)


# list=[2,5,7,3,6,9]
# target=9
# seen={}
# for index, value in enumerate(list):
#  needed = target - value
#  if needed in seen:
#    print (seen[needed],index)
#  else:
#    seen[value]=index



# list = [3,4,6,8,5,7,9,5]
# target = 9
# seen={}

# for index, value in enumerate (list):
#     needed = target - value
#     if needed in seen:
#         print (seen[needed],index)
#     else:
#         seen[value]=index
#  
# list = [2,4,5,6,7,8,9,10]
# target = 10
# seen={}

# for index, value in enumerate(list):
#     needed = target - value
#     if needed in seen:
#         print (seen[needed],index)
#     else:
#         seen[value] = index



list = [11,3,5,7,14,6,8,9,0]
target = 14
seen = {}
for index, value in enumerate(list):
    needed = target - value 
    if needed in seen:
        print (seen[needed],index)
    else:
        seen[value]=index
    

