def find_second_lowest_students():
    students = []
    
    # Read the number of students
    n = int(input().strip())
    
    # Read the student names and grades
    for _ in range(n):
        name = input().strip()
        grade = float(input().strip())
        students.append([name, grade])
    
    # Extract all grades and find the second lowest grade
    grades = sorted(set([grade for name, grade in students]))
    second_lowest_grade = grades[1]
    
    # Collect names of students with the second lowest grade
    second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    
    # Print the names
    for student in second_lowest_students:
        print(student)

if __name__ == '__main__':
    find_second_lowest_students()
