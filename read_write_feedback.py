'''
Creata a text file named as "SQL_Bootcamp_Feedback.txt"

Write a program to read through this file and then copy only the feedback from 
this file and load it into a new file named "Feedback_file.txt"

Steps:
1) open the "SQL_Bootcamp_Feedback.txt" file
2) Loop through each line of this file:
3) If a line starts with "Feedback: " then move this line to a new file.
    You can use str.startswith() method for this purpose
'''
    



with open('SQL_Bootcamp_Feedback.txt', 'r') as fr:
    # print(fr.read()) 
    for line in fr:
        if line.startswith('Feedback: '):
            with open('feedback_file.txt', 'a') as fa:
                fa.write(line.replace('Feedback: ',''))
