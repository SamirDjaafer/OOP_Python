from Monster import Monster


class Student(Monster):
    def __init__(self, name, tax_number, fur, student_no, skill_list=None):
        super().__init__(name, tax_number, fur)
        if skill_list is None:
            skill_list = []
        self.__student_no = student_no
        self.skill_list = skill_list

    def get_student_no(self):
        return self.__student_no

    def set_student_no(self, student_no):
        self.__student_no = student_no

    def add_skill(self, skill):
        self.skill_list.append(skill)

    def get_skills(self):
        # all_skills = ""
        # for skill in self.skill_list:
        #     all_skills += f'{skill}, '
        # return all_skills
        return self.skill_list
