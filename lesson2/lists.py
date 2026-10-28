# nums = []
# for i in range(6):
#     nums.append(i)

# print(nums)

# nums = [k for k in range(6)]
# print(nums)

# nums = [12, 5, 8, 99, 3, 8]
# print(nums[0], nums[-1])
# sum = 0
# for i in nums:
#     if i == 8:
#         print("have")
#         break
#     else:
#         print("have not")
#         break
#     sum += i
# print(sum)



# toys = ['Zeus', 'Apollo', 'Ares']
# toys.append('Hermes')
# print(toys)
# toys.insert(1,'Hades')
# print(toys)
# toys.remove('Apollo')
# print(toys)
# a = toys[-1]
# toys.pop(-1)
# print(toys)
# print(a)

# numbers = [4, 7, 10, 15, 18, 21, 24]
# for nums in numbers:
#     print(nums, end=" ")

# print()

# for nums in numbers:
#     if nums % 2 == 0:
#             print(nums, end=" ")

# print()

# count = 0
# for i , j in enumerate(numbers):
#      print(f"{i}   {j}")
#      if j > 10:
#           count += 1
     
# print(count)

text = input()
text1 = text.split()
print(text1)

text = '-'.join(text1)
print(text)