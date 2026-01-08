   

# Question 1: What is the output of the following code?
a = 5
b = 10
print(a < b < 20) 
#(a<b) and (b<20)
# 5<10 ------True
# 10<20 -----True
# Output: True


# Question 2: Predict the output: 
x = True 
y = False 
print(x + y * x)
# True = 1
# False = 0
# y * x---0 * 1 = 0
# x + 0---1 + 0 = 1
#Output: 1



# Question 3: What does this expression evaluate to? 
print(4 ** 0 ** 2) 
# 0 ** 2 = 0
# 4 ** 0 = 1
#Output: 1




# Question 4: Find the result of this bitwise operation: 
a = 12   
b = 5    
print(a ^ b) 
# Binary conversion( Bitwise XOR)
# 12 = 1100
# 5 =  0101
    #  -----
    #  1001      
#Output: 9




# Question 5: Guess the output: 
print((3 and 0) or (0 and 3))
# and --- find 1st value false, then return
# or --- find True value, then return
# (3 and 0)--- 3 is True, but 0 is False ,----result = 0
# (0 and 3)--- 0 is False, ---result = 0
# 0 or 0,----result= 0 
# Output: 0



# Question 6: What's the output of this tricky comparison? 
print(256 is 256)
# is---- identity operator (same memory object ya nhi)  
# 256 is 256----same memory,---resutlt = True
# Output: True
print(257 is 257)  
# Expected Output: True



# Question 7: Evaluate this expression: 
a = 7 
print(~a + 1) # ~a---bitwise NOT
# -7 = -(7 +1 ) = -8
# -8 +1 = -7  
# Output: -7



# Question 8: What will this print? 
a = True 
b = False 
print((a or b) and not (a and b)) 
# (a or b)---True or False = True
# (a and b)---True and false = False
# bot False--- True -----True and True = True
# Output: True



# Question 9: What's the output? 
print(10 > 5 == True)
# 10 > 5 = True
# 5 == True ---(True = 1,)-----False
# True and False = False
# Output: False



# Question 10: Evaluate this expression: 
print(2 + 3 * 4 ** 2 // 8 % 3)
# 4 ** 2 = 16
# 3 * 16 = 48
# 48 // 8 = 6
# 6 % 3  = 0
# 2 + 0 = 2 
# Output: 2




# Question 11: What does this expression evaluate to? 
print(1 << 2 + 1) 
# Output: 8



# Question 12: Predict the output: 
a = 3 
b = 2 
a *= b + 1
print(a) 
# b+ 1 = 2 + 1 = 3
# a *= 3 ---a = a*3
# a = 3 * 3 = 9
# Output: 9



# Question 13: Evaluate this chained comparison: 
print(3 < 5 > 2 == 2) 
# 3 < 5 = True
# 5 > 2 = True
# 2 == 2 = True------ True and True and True = True
# Output: True




# Question 14: Guess the result: 
print(10 // 3 * 3 + 1 % 3) 
# 10 // 3 = 3
# 3 * 3 = 9
# 1 % 3 = 1
# 9 + 1 = 10
# Output: 10




# Question 15: What is the result of this? 
x = 10 
y = 20 
print(x & y | x ^ y) 
#------binary-- 10 = 1010, 20 = 10100 x & y--01010
                                            #10100
                                            #-----
                                            #00000 = 0
                                              
# Expected Output: 30

# Question 16: Trick with boolean and bitwise: 
a = True 
b = False 
print(a & b or a ^ b) 
# Expected Output: True

# Question 17: Evaluate this: 
x = 8 
print(x >> 1 << 2) 
# Expected Output: 16

# Question 18: What does this produce? 
print(5 + True * False + (not False)) 
# Expected Output: error>> 'not' after an operator must be parenthesized 
print(5 + True * False + (not False)) 
# Expected Output: 6

# Question 19: Operator confusion: 
print((not 0) * (False or 1)) 
# Expected Output: 1

# Question 20: Mix of precedence and associativity: 
print(4 + 3 * 2 ** 2 // 2 - 1) 

# Expected Output: 9