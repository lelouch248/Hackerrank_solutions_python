def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        dif = 5 - grades[i]%5
        if (grades[i]+dif)<40:
            continue
        elif dif <3:
            grades[i] = grades[i] + dif
    return grades
  
