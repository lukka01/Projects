import random


OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

total_problems = 10
import time

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr,answer

wrong_answers = 0

input("Press enter to start")
print("------------------")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem number #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong_answers += 1

end_time = time.time()
time_needed = round(end_time - start_time, 2)


print("------------------"
print('Nice work, You needed ', time_needed, "seconds to finish the test")




