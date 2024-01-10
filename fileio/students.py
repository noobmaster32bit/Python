
all_stud=open("E:\\Luminar\\Python\\fileio\\students.txt", "r")
fail_stud=open("E:\\Luminar\\Python\\fileio\\failed.txt", "r")

# all_stud_set=set()
# failed_set=set()

# for st in all_stud:
#     students=st.rstrip("\n")
#     all_stud_set.add(students)

all_stud_set={st.rstrip("\n") for st in all_stud}
fail_stud_set={st.rstrip("\n") for st in fail_stud}


# for st in fail_stud:
#     student=st.rstrip("\n")
#     failed_set.add(student)

passed_students=all_stud_set.difference(fail_stud_set)

print(passed_students)

