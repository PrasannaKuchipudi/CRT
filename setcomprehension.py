#Set Comprehension 
#Set comprehension creates a set using a single line of code. 
#Set removes duplicates automatically 
# #Square of numbers
# squares={x**2 for x in range(5)}
# print(squares)
# # Unique letters in a word 
# letters={ch for ch in "hello"}
# print(letters)
#From a list with duplicates 
nums=[1,2,3,4,1,2,6,4,2,8]
unique={x for x in nums}
print(unique)
