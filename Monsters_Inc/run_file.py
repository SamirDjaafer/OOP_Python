from Monster import Monster
from Student_Monster import Student
from Course import Course

# Create two student objects
mike = Student('Mike', 123, 'Fluffy brown', 1)
bobby = Student('Bobby', 3445, "Furry", 2)


# Add a skill to each of your student
mike.add_skill("Super Strength")
bobby.add_skill("Stealth")


# Create(initialize) a course
monster_course = Course('Monster Training', start_date="02/06/2020")


# Append student object / instances to list of student attributes in one of the courses
# monster_course.add_student(mike)
# monster_course.add_student(bobby)

# monster_course.skill_list.append(mike.skill_list)

print(mike.get_skills())
print(bobby.get_skills())

print(monster_course.skill_list)

print("////////")

for student in monster_course.list_of_students:
    print(student.get_skills())



# EXTRA - get the list of students, itterate over it and print the students name

