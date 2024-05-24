if __name__ == '__main__':
    while True:
        N = int(input())
        if 1 <= N <= 5:
            break
        else:
            print("Please enter a number between 1 and 5.")

    students = []


    for _ in range(N):
        name = input()
        score = float(input())
        students.append([name, score])

    students.sort(key=lambda x: x[1])


    lowest_score = students[0][1]

   
    second_lowest_score = None
    for student in students:
        if student[1] > lowest_score:
            second_lowest_score = student[1]
            break

    for student in students:
        if student[1] == lowest_score:
            break
            
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]
    second_lowest_students.sort()
    for student_name in second_lowest_students:
        print(student_name)