students={}
def add_student(student_id,name,class_name):
    if student_id in students:
        print("Student already exits")
    else:
        students[student_id]={'name' : name , 'class' : class_name , 'grades' : []}

    print("student added succesfully")
    

def update_grades(student_id,new_grades):
    if student_id in students:
        students[student_id]['grades'].extend(new_grades)
        print("grades updated")
    else:
        print("No student")
        


def calculate_average(student_id):
    if student_id in students:
        grades = students[student_id]['grades']
        if grades:
            average = sum(grades)/len(grades)
            return average
        else:
            return 0.0
    else:
        print("No student")
        return None
    

def generate_top_students_report():
    top_students={}

    for student_id,details in students.items():
        class_name = details['class']
        average_grad = calculate_average(student_id)

        if class_name not in top_students or average_grad > top_students[class_name]['average']:
            top_students[class_name] = {'student_id' : student_id , 'name' : details['name'] , 'average' : average_grad}


    print("Top student report is : ")
    print(top_students)


add_student('1','Tejas','12A')
add_student('2','Rakshit','12B')
add_student('3','Abhishek','12C')

update_grades('1',[23,34,45,67])
update_grades('2',[34,14,56,100])
update_grades('3',[23,45,56,67])

generate_top_students_report()


        
    
