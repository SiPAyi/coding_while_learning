# Write a program that has dictionary of names of students and a list of their marks
# in 4 subjects. Create another dictionary from this dictionary that has name of the
# students and their total marks . Find out topper and his/her score.

students_details = {}
subjects = ['maths', 'physics', 'chemistry', 'it']
print('please enter student details with  \n')
number_of_students = int(input('How many students details do you have : '))
for i in range(number_of_students):
    student_marks_details = {}
    
    name = input('Enter student name : ') 
    
    for subject in subjects:
        message = 'Enter ' + subject + ' marks : '
        subject_marks = int(input(message))
        student_marks_details[subject] = subject_marks
    
    students_details[name] = student_marks_details
    print()


students_marks_details = {}

for student in students_details:
    student_marks_details = students_details[student]
    student_total_marks = 0
    for subject in student_marks_details:
        student_total_marks += student_marks_details[subject]

    students_marks_details[student] = student_total_marks

topper = {'name':'', 'marks':0}
for student in students_marks_details:
    if students_marks_details[student] > topper['marks']:
        topper['marks'] = students_marks_details[student]
        topper['name'] = student

print(topper)