# You will have a number of elements and in the next n lines element of a list. 
# You have to create a list from the given strings. You have to sort the list 
# based on 2nd last character of a string

# For example: Given list = ['great','hello','hiyo','abc'] So your output_dictionary 
# should be ['great','abc','hello','hiyo']



def sort_list(lst):
    sorted_list = sorted(lst, key=lambda x: x[-2])
    return sorted_list

n = int(input("Enter how many elements: "))
lst = []
for i in range(n):
    lst.append(input())

sorted_list = sort_list(lst)
print(sorted_list)


#Output:- ['great', 'abc', 'hello', 'hiyo']

