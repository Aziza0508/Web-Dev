test_answer = int(input())
student_answer = int(input())


if student_answer == 1 and test_answer != 1:
    print("YES")
elif student_answer != 1 and test_answer == 1:
    print("NO")
else:
    print("YES" if student_answer == test_answer else "NO")
