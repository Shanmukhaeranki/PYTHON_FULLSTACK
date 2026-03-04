print("---------TAKE A TEST----------")
score = 0

questions = [
    ("1) Which is a valid variable name?\nA) 1name\nB) name_1\nC) name-1\nD) name 1\nYour answer: ", "B"),
    ("2) Output of print(type(5))?\nA) str\nB) int\nC) float\nD) number\nYour answer: ", "B"),
    ("3) Symbol for comments?\nA) //\nB) /* */\nC) #\nD) --\nYour answer: ", "C"),
    ("4) 3 + 2 * 2 = ?\nA) 10\nB) 7\nC) 8\nD) 12\nYour answer: ", "B"),
    ("5) Immutable type?\nA) List\nB) Dict\nC) Set\nD) Tuple\nYour answer: ", "D"),
    ("6) len('Python')?\nA) 5\nB) 6\nC) 7\nD) Error\nYour answer: ", "B"),
    ("7) Keyword to define function?\nA) function\nB) define\nC) def\nD) func\nYour answer: ", "C"),
    ("8) 10 // 3 = ?\nA) 3.33\nB) 3\nC) 4\nD) 3.0\nYour answer: ", "B"),
    ("9) Which is a list?\nA) {1,2,3}\nB) (1,2,3)\nC) [1,2,3]\nD) <1,2,3>\nYour answer: ", "C"),
    ("10) 1 == 1 ?\nA) True\nB) False\nC) None\nD) Error\nYour answer: ", "A")
]

for q, ans in questions:
    user = input(q).upper()
    if user == ans:
        print("Correct ✅\n")
        score += 1
    else:
        print(f"Wrong ❌. The right answer is: {ans}\n")

print("Your final score is:", score, "/ 10")

