# x = 9
# y = 3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x%y)
# print(x/y)
# print(x**y)
# print(x//y)
# print(x/y+3)
# print((x/y)-3)


# print("daman's laptop")
# print("daman\'s laptop")
# print("daman "*10)
# print("daman's \n laptop")

# nums=['12','23','24','64']
# print(nums)

# name = ['daman','raman','harman']
# print(name)

# all = [nums + name]
# print(all)


# nums =[12,23,24,64]
# nums.remove(24)
# print(nums)
# nums.insert(2,27)
# print(nums)
# nums.pop(1)
# print(nums)
# nums.append('24')
# print(nums)


# del nums[2:]
# print(nums)


# print(min(nums))
# print(max(nums))
# print(nums.sort())
# print(sum(nums))


# print(bin(35))
# print(hex(10))
# print(oct(35))
# print(hex(35))


# class person:
#     def __init__(self,fname,lname):
#         self.firstname =fname 
#         self.lastname = lname

#         def printname(self):
#             print(self.firstname, self.lastname)

# class student(person):
#     pass

# x= student("mile","olsen")
# x.printname()

# x = input("enter 1st number")
# y = input("enter 2nd number")
# z = int(x)+int(y)
# print(z)
# import sys
# x = int(sys.argv[1])
# x = int(sys.argv[2])
# z= x + y 
# print(z) 


# i = 1
# while i<=5:
#     print("daman ",end="")
#     j=1
#     while j <= 5:
#         print(" singh",end="")
#         j+=1
#     i+=1
#     print() 

# x =['daman',65,2.5]
# for i in x:
#     print(i)

# x = 'daman'
# for i in x:
#     print(i)

# x = 'daman'
# for i in range(10):
#     print(i)

# x = 'daman'
# for i in range(11,21,2):
#     print(i)


# x = 'daman'
# for i in range(0,20,1):
#     if i%5!=0:
#         print(i)


# x=int(input("enter a number"))
# av = 10
# i = 1
# while i <= x:
#     if i>av:
#         break
#     print("candy",i)
#     i+=1




for i in range(1,101):

    if i%3==0 and i%5==0:
        continue
    print(i)
print("bye")
