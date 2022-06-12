#!/usr/bin/python3

import random
import urllib.request
import sys
import json

from configparser import ConfigParser as cp

input("""########################### Yellowtail Python Automation Course - Icebreaker ########################## 
###                                Press any key to start randomizer.                               ### 
#######################################################################################################""")

questions_per_student = 3

# Open Roster file of students
f = open('roster.txt', 'r')
students = f.readlines()
f.close()

#Open icebreaker questions
f = open('icebreaker_questions.txt', 'r')
questions = f.readlines()
f.close()

# File output results
results_file = open("Student_Responses.txt", "w")

while students:
    random_student = random.choice(students)
    print(random_student.strip())
    results_file.write(random_student.strip() + "\'s Questions & Responses:\n")
    
    # Set/reset already_asked question outside of total range of questions bank to handle avoiding repeated question for one student
    already_asked = []
    total_questions = len(questions)
    for q in range(questions_per_student):	
        # Pull a random question
        random_question = random.choice(questions)
        question_index = questions.index(random_question)
	
        # Before asking question, confirm that it hasnt been asked yet, if question already asked for student randomize for another question
        if question_index in already_asked:
            print("Selected random question already asked! Next question...")
            results_file.write("%d. Student received the same random question!")            
        else:
            response = input(random_question)
            results_file.write("\t%d. %s\n" %  (q + 1, random_question))
            results_file.write("\t\t" + response + "\n")
            already_asked.append(question_index)

    # Get index number of randomized student and remove from list	
    index = students.index(random_student)
    students.pop(index)

    if students:
        input("Press any key to randomzie for next student...")

results_file.close()
 
