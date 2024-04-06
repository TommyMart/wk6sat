# Factorial

# 6! = 1 * 2 * 3 * 4 * 5 * 6 - factorial 

num = 6

fact_result = 1

for i in range(1, num + 1): # 1, 2, 3, 4
    fact_result *= i # 1 * 1 = 1, 1 * 2 = 2, 2 * 3 = 6, 6 * 4 = 24, 24 * 5 = 120 ....

print(fact_result)