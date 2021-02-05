'''
Equal Disconnected Segments
You are given a list of interval segments.Your task is to modify these segments such that:
1.All Segments are disconnected.
2.All segments are equal in length.Length of a segment is defined as the difference of its start and end.
3.Any modified segment created is subsegment of original segment

Return the maximal length after modifications

Example:
Input Segments:[2,6],[1,4],[8,12]
output:2.5
Explaination:
First [2,6] segment intersects with second [1,4],after making them disconnected they become
[1,3.5]and [3.5,6] each of size 2.5.
Now all segments are disconnected but length of third is not equal to first and second.After
making third equal is becomes [8,10.5]
So maximal length is 2.5.
'''