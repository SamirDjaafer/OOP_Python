from Monster import Monster
from Student_Monster import *
from Course import *

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

# debugging options
    # check the original class
    # look for what get_skills method does
    # look what add skills method does

    #print the type

print(type(bobby.get_skills()))
for skill in bobby.get_skills():
    print(skill)
    #program until we get the result we want
    #       be a plumber of code !!

    #pointbreak() function
        #pointbreak stops your code in real time, allowing you to test/see your variables at that point in time.

# print(monster_course.skill_list)
#
# print("////////")
#
# for student in monster_course.list_of_students:
#     print(student.get_skills())



# EXTRA - get the list of students, itterate over it and print the students name

