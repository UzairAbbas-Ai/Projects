def collect_student_data():
    students = []
    student_id = 1
    while True:
        name = input("Please enter the student's name (or type 'stop' to finish)= ")
        
        if name.lower() == 'stop':
            break
        
        if any(student[1].lower() == name.lower() for student in students):
            print("This name is already in the list")
        else:
            students.append((student_id, name))
            student_id = student_id+1
    
    return students

def print_student_data(students):
    
    print("\nComplete List of Students (Tuples)=")
    print(students)

    print("\nList of Students with IDs=")
    for student in students:
        print(f"ID= {student[0]}, Name= {student[1]}")

    total_students = len(students)
    total_length = sum(len(student[1]) for student in students)

    longest_name_student = None
    shortest_name_student = None

    for student in students:
        if longest_name_student is None or len(student[1]) > len(longest_name_student[1]):
            longest_name_student = student
        
        if shortest_name_student is None or len(student[1]) < len(shortest_name_student[1]):
            shortest_name_student = student

    print(f"\nTotal number of students= {total_students}")
    print(f"Total length of all student names combined= {total_length}")
    if longest_name_student:
        print(f"The student with the longest name is= {longest_name_student[1]}")
    if shortest_name_student:
        print(f"The student with the shortest name is= {shortest_name_student[1]}")

students = collect_student_data()
print_student_data(students)
