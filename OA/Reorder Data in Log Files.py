'''
First question was to reorder list of orders, which was differentiated by prime order and non prime
orders. Each order has unique identifier which is alphanumeric. Prime order has meta data which are
in form of space seperated alphanumeric words. Non prime orders have metadata as space separated
positive integers. first word is always the identifier. prime orders have higher priority than non
prime and are sorted lexicographically based on their meta data. if meta data is also same, tie is
broken by unique identifier. non prime order are added in final list as original order and have lower
priority than prime orders.
'''

'''amazon plans to open treasure truck pop-ups at x. x is represented by m*n blocks. each block is a 
park area rep by 1 or commercial area by 0. adjacent blocks with value 1 are considered as contigous 
park. Diagonal blocks with 1 are not part of same contiguity. they plan to have truck pop in each 
contigous park. write an algo to find the no of treasure truck pop-up they can open.

Input :
it has 3 arguments.
rows an int rep by rows in grid
column,int rep the nubmer of cols in the grid
grid,a 2d int array rep by x
output:
Return an int rep the no of treasure Truck pop-up that they can open in the area x.'''
