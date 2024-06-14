if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # Calculate the average of the marks for the queried student
    query_marks = student_marks[query_name]
    average_marks = sum(query_marks) / len(query_marks)
    
    # Print the average marks to 2 decimal places
    print(f"{average_marks:.2f}")