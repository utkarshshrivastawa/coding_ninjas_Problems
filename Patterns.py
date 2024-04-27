# Problem statement
# Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

# For every value of ‘N’, help sam to print the corresponding N-dimensional forest.

# Example:
# Input: ‘N’ = 3

# Output: 
# * * *
# * * *
# * * *
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1  <= N <= 25
# Time Limit: 1 sec
# Sample Input 1:
# 3
# Sample Output 1:
# * * *
# * * *
# * * *
# Explanation Of Sample Input 1 :
# For N = 3, fill all the rows and columns in 3x3 matrix with ‘*’.
# Sample Input 2 :
# 1
# Sample Output 2 :
# *
# Sample Input 3 :
# 4
# Sample Output 3 :
# * * * *
# * * * *
# * * * *
# * * * *

#  code 
def nForest(n:int) ->None:
    # Write your solution here.
    for i in range (n) :
        for j in range (n) : 
            print("*", end = " ")
        print()
    pass

# Problem statement
# Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

# An N/2-dimensional forest is represented by the lower triangle of the pattern filled with ‘*’.

# For every value of ‘N’, help sam to print the corresponding N/2-dimensional forest.

# Example:
# Input:  ‘N’ = 3

# Output: 
# * 
# * *
# * * *
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1  <= N <= 25
# Time Limit: 1 sec
# Sample Input 1:
# 3
# Sample Output 1:
# * 
# * *
# * * *
# Explanation Of Sample Input 1 :
# For N = 3, fill all the rows and columns in the lower triangle of 3x3 matrix with ‘*’.
# Sample Input 2 :
# 1
# Sample Output 2 :
# * 

#  code 
def nForest(n:int) ->None:
    # Write your solution here.
    for i in range (n):
        for j in range (i+1):
            print("*",end = " ")
        print()
    pass


# Problem statement
# Sam is making a Triangular painting for a maths project.

# An N-dimensional Triangle is represented by the lower triangle of the pattern filled with integers representing the row number.

# For every value of ‘N’, help sam to print the corresponding Triangle.

# Example:
# Input: ‘N’ = 3

# Output: 
# 1
# 2 2 
# 3 3 3
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1  <= N <= 25
# Time Limit: 1 sec
# Sample Input 1:
# 3
# Sample Output 1:
# 1 
# 2 2 
# 3 3 3
# Sample Input 2 :
# 1
# Sample Output 2 :
# 1
# Code 
def triangle( n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range ( i+1):
            print(i+1 ,end= " ")
        print()
    pass


# Problem statement
# Sam is making a Triangular painting for a maths project.

# An N-dimensional Triangle is represented by the lower triangle of the pattern filled with integers starting from 1.

# For every value of ‘N’, help sam to print the corresponding N-dimensional Triangle.

# Example:
# Input: ‘N’ = 3

# Output: 
# 1
# 1 2 
# 1 2 3
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1  <= N <= 25
# Time Limit: 1 sec
# Sample Input 1:
# 3
# Sample Output 1:
# 1
# 1 2 
# 1 2 3
# Sample Input 2 :
# 1
# Sample Output 2 :
# 1

#  Code 
def nTriangle(n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):
            print(j+1 , end=" ")
        print()
    pass

# Problem statement
# Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Diamond.

# Example:
# Input: ‘N’ = 3

# Output: 

#   *
#  ***
# *****
# *****
#  ***
#   *
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1  <= N <= 20
# Time Limit: 1 sec
# Sample Input 1:
# 3
# Sample Output 1:
#   *
#  ***
# *****
# *****
#  ***
#   *    
# Sample Input 2 :
# 1
# Sample Output 2 :
# *
# *

def nStarDiamond(n: int) -> None:
    # Write your code here.
    a = n
    for i in range(0,2*n,2):
        a = a-1
        for j in range(a):
            print(" ", end="")
        for j in range(i+1):
            print("*",end="")
        print()
    a = 0
    b = n 
    for i in range (0, 2*n,2):
        for j in range(a):
            print(" ", end="")
        a = a+1
        for j in range ((2*b)-1):
            print("*",end= "")
        b =b-1
        print()
    pass
