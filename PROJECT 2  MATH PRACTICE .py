import random
import time
OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr,answer
wrong = 0
input("press enter to start")
print("********************")
print("you time start now")
start_time = time.time()
for i in range(TOTAL_PROBLEMS):
    expr,answer = generate_problem()
    while True:
     guess = input("problem #" + str(i + 1) + ":" + expr + " = ")
     if guess == str(answer):
        break
    wrong += 1

end_time = time.time()
total_time = round(end_time - start_time,2)    
print("********************")
print("you cought off")
print("Nice Work ! , you finish in ",total_time,"seconds")