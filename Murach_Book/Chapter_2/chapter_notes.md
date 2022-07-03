# How to write your first programs

## Basic coding skills

### How to code statements

**Coding Rules:**
1. Python relies on proper indentation. Incorrect indentation causes an error.
2. The standard indentation is four spaces whenever it is required.
3. With *implicit continuation*, you can divide statements after parentheses, brackets, and braces,
   and before or after operators like plus or minus.
4. With *explicit continuation*, you can use the `\` character to divide statements anywhere on a
   line.

**The Python code for a Test Scores program:**
```Python
#!/usr/bin/env python3

counter     = 0
score_total = 0
test_score  = 0

while test_score != 999:

    test_score = int(input("Enter test score: "))

    if (test_score >= 0) and (test_score <= 100)
        score_total += test_score
        counter += 1

    average_score = round(score_total / counter)

    print("Total Score: "   + str(score_total))
    print("Average Score: " + str(average_score))
```

**An indentation error**
```Python
print("Total Score: "   + str(score_total))
 print("Average Score: " + str(average_score))
```

**Two ways to continue one statement over two or more lines:**

**Implicit continuation**
```Python
print("Total Score: "     + str(score_total)
    + "\nAverage Score: " + str(average_score))
```

**Explicit continuation**
```Python
print("Total Score: "     + str(score_total) \
    + "\nAverage Score: " + str(average_score))
```

### How to code comments

