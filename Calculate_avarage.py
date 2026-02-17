data={"student_1":{"name":"Aditya","marks":[80,86,90]},
      "student_2":{"name":"Sumit","marks":[70,76,54]},
      "student_3":{"name":"sujeet","marks":[70,76,45]},
      "student_4":{"name":"anurag","marks":[70,87,87]},
      "student_5":{"name":"ayush","marks":[70,43,87]},
      "student_6":{"name":"deepu","marks":[70,90,87]},
      "student_7":{"name":"anuj","marks":[70,73,87]},
      "student_8":{"name":"pranjal","marks":[70,78,87]},
      "student_9":{"name":"aryan","marks":[70,80,87]},
      "student_10":{"name":"hariom","marks":[70,61,87]},}

highest_avg=0
top_student=""

for student in data:
    marks=data[student]["marks"]
    average=sum(marks) / len(marks)

    if average>highest_avg:
        highest_avg=average
        top_student=data[student]["name"]

print("Highest average marks of student is :",top_student)