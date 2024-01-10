students=[
    {"id":1,"name":"jhon","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":1,"name":"jain","skills":["python","js"],"exp":0,"qualification":"btec"},
    {"id":1,"name":"vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":1,"name":"tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":1,"name":"roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":1,"name":"vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":1,"name":"ravi","skills":["java","python"],"exp":3,"qualification":"btec"},
    {"id":1,"name":"tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":1,"name":"ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"},
   
    
]

# total no of students
# print(len(students))

#   print names of all students
# for s in students:
#     print(s.get("name"))

# exp > 1
# for s in students:
#     if s.get("exp")>1:
#         print(s.get("name"))

# # use list comprehension

# exp_gt_one=[s.get("name") for s in students if s.get("exp")>1]


# print python and java as skills
# for s in students:
#     if "java" in s.get("skills") and "python" in s.get("skills"):
#        print( s.get("name"))


# mca stdents names

# for s in students:
#     if s.get("qualification")=="mca":
#         print(s.get("name"))

# most experienced student

# most_exp=max(students, key=lambda s:s.get("exp"))
# print(most_exp)
# highest_exp=most_exp.get("exp")
# print(highest_exp)

# exp_students=[s.get("name")for s in students if s.get("exp")==highest_exp]
# print(exp_students)

# students with skills > 2
# for s in students:
#     if s.get("skills"):
#         if len (s.get("skills"))>2:
#             print(s.get("name"))


# students  name startswith "j"

# for s in students:
#     if s.get("name").startswith("j"):
#         print (s.get("name"))


#most chosen skill

skill_count={}

for s in students:
    skill=s.get("skills")
    # print(skill)

    for sk in skill:
        if sk in skill_count:
            skill_count[sk]+=1
        else:
            skill_count[sk]=1
print(skill_count)   
        


 