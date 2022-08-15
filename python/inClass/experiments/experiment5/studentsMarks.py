# students_details = {
#     'sai': {'telugu':36, 'english':36, 'maths':40, 'physics':37, 'chemistry':40, 'it':40}, 
#     'srinadh': {'telugu':39, 'english':36, 'maths':40, 'physics':40, 'chemistry':40, 'it':40}, 
#     'sravan': {'telugu':38, 'english':36, 'maths':40, 'physics':40, 'chemistry':40, 'it':40}, 
#     'manikanta': {'telugu':39, 'english':36, 'maths':40, 'physics':40, 'chemistry':40, 'it':40}, 
#     'shreyash': {'telugu':39, 'english':36, 'maths':40, 'physics':40, 'chemistry':40, 'it':40}, 
#     'praneel': {'telugu':37, 'english':36, 'maths':40, 'physics':39, 'chemistry':40, 'it':40},     
# }

students_details = {}
subjects = ['telugu', 'english', 'maths', 'physics', 'chemistry', 'it']
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





#-----------------------#
#### using functions ####
#-----------------------#

# def studentsDetails():
#     students_details = {}
#     subjects = ['telugu', 'english', 'maths', 'physics', 'chemistry', 'it']
#     print('please enter student details with  \n')

#     for i in range(2):
#         student_marks_details = {}
        
#         name = input('Enter student name : ') 
        
#         for subject in subjects:
#             message = 'Enter ' + subject + ' marks : '
#             subject_marks = int(input(message))
#             student_marks_details[subject] = subject_marks
        
#         students_details[name] = student_marks_details
#         print()   

#     return students_details


# # the below function extracts students marks details from a dictionary which is in the below form
# # student_details = {'name' : {'subject1': marks, 'subject2': marks,'subject3': marks, 'subject4': marks,'subject5': marks, 'subject6': marks}}
# # returns the output in the below form
# # student_marks_details = {'name': total_marks, 'name': total_marks, 'name': total_marks, .....}
# def studentsMarks(students_details):
#     students_marks_details = {}

#     for student in students_details:
#         student_marks_details = students_details[student]
#         student_total_marks = 0
#         for subject in student_marks_details:
#             student_total_marks += student_marks_details[subject]

#         students_marks_details[student] = student_total_marks

#     return students_marks_details


# # the below fuction finds the topper in a given dictionary as the below format
# # it takes a dictionary containing student marks details in the below form
# # students_marks_details = {'name': marks}
# # returns a dictionary in the below form
# # topper = {name: total_marks}
# def findTopper(students_marks_details):
#     topper = {'name':'', 'marks':0}
#     for student in students_marks_details:
#         if students_marks_details[student] > topper['marks']:
#             topper['marks'] = students_marks_details[student]
#             topper['name'] = student

#     return topper

# students_details = studentsDetails() 

# students_marks_details = studentsMarks(students_details)

# topper = findTopper(students_marks_details)