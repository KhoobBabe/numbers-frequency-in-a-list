no_in_list = int(input("How many numbers do you want in the list: "))

n = 0
#our intial list will be empty like the brain of a student
lists = []

for n in range(no_in_list):
    
    #done so we can take the number of inputs as we requested
    n+=1
    
    #input for list 
    numbers = int(input(f"enter the number {n}: "))

    #we store new entries through this
    lists.append(numbers)

#the list is sorted with the most frequency entries coming in first

lists.sort(key = lists.count, reverse=True)

freq = {x:lists.count(x) for x in lists}

print("number", "\t", "frequency")

#to print the entries in the table with most entries one coming first
for i in freq:
    if freq[i] > 1:
        print(i, "\t", freq[i])

#another list which removes the repeating entries 
dup_list = [] 
for i in lists: 
    if i not in dup_list: 
        dup_list.append(i) 
print("The list without the repeating entries is : ", dup_list)

