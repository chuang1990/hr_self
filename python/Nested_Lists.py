# if __name__ == '__main__':
#     students = []
#     for _ in range(int(input())):
#         students.append([input(), float(input())])
#     # print(students)
#     second_lowest = sorted(set([s for n,s in students]))[1]
#     students.sort()
#     # print(students)
#     # print(lowest, second_lowest)
#     for student, score in students:
#         if score == second_lowest:
#             print(student)
#     # print(students)
    

# Nested Lists python
if __name__ == '__main__':
    n = int(input())
    students = [[input(), float(input())] for _ in range(n)]
    second_lowest = sorted(set([s for n,s in students]))[1]
    students.sort()
    # print(students)
    # print(lowest, second_lowest)
    for student, score in students:
        if score == second_lowest:
            print(student)
    # print(students)
    