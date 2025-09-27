# container setup
a_tuple = (1,2,3,'saloni')
a_list = [1,2,3,'saloni']

print(a_tuple)
print(a_list)

print(len(a_tuple))
print(len(a_list))

#this cannot be done on a tuple.
a_list.append('sharma')
print(a_list)

# a set can only have unique values
a_set = {1,2,3,4,4}
print(a_set)
alist = [1,2,2,3,4,5] # now we can remove duplicate value by converting this list into set
print(list(set(alist)))# the list function retains the data as a list and not as a set.

a_dictionary = {'key': 'value' , 123: [1,2,3]}
a_dictionary['new key']= 1.5
print(a_dictionary)

# how to get values from a container
user_list  = ['bob','lisa','john','shiv','veer']
# indexing
print(user_list[3])
print(user_list[0:3])

#slicing
print(user_list[0:3:2])

print(a_dictionary['key'])



