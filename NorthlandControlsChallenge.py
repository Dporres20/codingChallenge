# Given an arbitrary list of positive integers as an input, 
# print an output that shows the factors that make up the number, 
# sorted by most factors to least factors. 
# For example, with an input of [10, 357, 17, 128, 81], 
# print an output that looks something like this:

# 128 has 8 factors: 1, 2, 4, 8, 16, 32, 64, 128
# 357 has 8 factors: 1, 3, 7, 17, 21, 51, 119, 357
# 81 has 5 factors: 1, 3, 9, 27, 81
# 10 has 4 factors: 1, 2, 5, 10
# 17 has 2 factors: 1, 17

# Thought process:
# Start by creating function that finds the factors and returns a list of those factors
# Follow by creating function that orders them based on the most to least factors
# Last print out the list in order

#Function to find factors
#Returns ordered list of info [{key:[val]}]
def findFactors(lis):
    # Create an empty list
    unordered_ls = []
    
    # loop through the list of given values
    for el in lis:

        # create empty dictionary
        # dictionary holds:
        # key: count for factors
        # value: list of factors
        thisset = {}
        factors = []
        count = 0

        # Loop through the number to find factors
        for factor in range(1, el+1):
            if el % factor == 0:
                count += 1
                factors.append(factor)
                #print(factor)

        # {key: value}
        # {count: [factors]}
        thisset[count] = factors
        
        # Append unordered list with new set of info
        unordered_ls.append(thisset)
        #print(factors)

    #print(unordered_ls)

    #Sorted list of info
    sorted_ls = sorted(unordered_ls, key=lambda d_el: list(d_el.keys())[0], reverse= True)
    #print(sorted_ls)

    return sorted_ls

#function to print out info
def print_order(lis):
    #loop through list
    for el in lis:
        #print(el.values())
        #convert values in element to a list
        vals_ls = list(el.values())[0]
        #print(vals_ls)

        # takes list items and joins them together based on separator
        values_string = ', '.join(str(el) for el in vals_ls)
        
        print(str(vals_ls[-1]) + " has " + str(len(vals_ls)) + " factors: " + values_string )
        #print(vals[0])

        # for val in vals[0]:
        #     print(str(val) + ", ")

        #print(vals[0])
        #print("")


        

nums = [10, 357, 17, 5, 128, 81, 36]

sorted_dict = findFactors(nums)

print_order(sorted_dict)

