'''
To solve any question in Python, first focus on these three terms:
1. What input is given?
2. What output you need?
3. What type of condition/middle logic will need to put into the input and get the desired output?
'''
'''
What this task has given:
- You are given three integers X, Y, and Z and an Integer N
- Print a list of all possible cordinates (i,j,k) such that:
    "0 <= i <= X"
    "0 <= j <= Y"
    "0 <= k <= Z"
    The sum of i + j + k is not equal to N"
'''
# Now break the each aspects of this question
# What is input?
# Three integer X, Y, Z --> which tells you the limit
# One integer N --> which restrict the sum

# What output we need according to question?
# List of all (i, j, k)
# Where i range is from 0 to X; j range is 0 to Y; k range is 0 to Z
# But i + j + k != N ; means summ of all three cordinates will not equal to N
# We can use nested loops here:

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

# Nested Loop + filttering with if
result = [[i, j, k]
          for i in range(x+1)
          for j in range(y+1)
          for k in range(z+1)
          if i + j + k != n]

print(result)




