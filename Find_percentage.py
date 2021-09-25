#This exercise will read in a dictionary containing key/value pairs of name:[marks] 
# for a list of students. Print the average of the marks array for the student name provided, 
# showing 2 places after the decimal.

#By: Aballey Wilson
    n= int(input()) #No. of students
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() #Name of student followed by their marks.  
        scores = list(map(float, line)) #Score of repective student is shown in a list.
        #print(scores)  #Uncomment to see how the marks has been showcase in a list.
        scores= sum(scores)/3
        student_marks[name] = scores
    query_name = input() #Name of student for the average to be calculated.
    print("{:.2f}".format(student_marks[query_name])) #Prints the marks of the student name given in two decimal places