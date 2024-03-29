'''
Project: Generating Random Quiz Files
Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals.
You’d like to randomize the order of questions so that each quiz is unique, making it impossible for any- one to crib answers from anyone else.

Here is what the program does:
1. Creates 35 different quizzes
2. Creates 50 multiple-choice questions for each quiz, in random order
3. Provides the correct answer and three random wrong answers for each question, in random order
4. Writes the quizzes to 35 text files
5. Writes the answer keys to 35 text files

This means the code will need to do the following:
1. Store the states and their capitals in a dictionary
2. Call open(), write(), and close() for the quiz and answer key text files
3. Use random.shuffle() to randomize the order of the questions and multiple-choice options

'''


import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for file_no in range(35):
    with open(f'Quiz_generator/Question_Paper_{file_no+1}.txt','w') as questionPaper:
        with open(f'Quiz_generator/Answer_Paper_{file_no+1}.txt','w') as answerPaper:
            questionPaper.write('\n\tName: \n\tDate: \n\tClass: \n')
            questionPaper.write(' '*20 + 'Random Quiz Generator - Question Paper - ' + str(file_no+1))
        
            for question_no in range(50):
                states = list(capitals.keys())
                random.shuffle(states)
                correct_ans=capitals[states[question_no]]
                wrong_ans=list(capitals.values())
                wrong_ans.remove(correct_ans)
                wrong_options=random.sample(wrong_ans,3)
                options=wrong_options + [correct_ans]
                random.shuffle(options)

                questionPaper.write('\n# ' + str(question_no+1) + '  What is the capital of ' + states[question_no]+' ?\n')

                # randomly change the position of each state within the list
                # Store the correct answer i.e capital of selected state 
                # to get all 3 wrong answer options, 
                    # first get capitals of all 50 states
                    # then remove the correct answer from this list
                    # using random.sample, fetch 3 values from above 49 wrong capitals
                # finally get the 4 options in a list: 3 wrong + 1 correct answer
                # shuffle the position of all 4 options

                # Display the question statement " what is capital of state?"
                
                for optionNum in range(4):
                    # display the options in question paper file
                    questionPaper.write(' ' *4 + 'ABCD'[optionNum]+'. '+  options[optionNum]+ '\n')
                    

                answerPaper.write(str(question_no+1) + '. '+ 'ABCD'[options.index(correct_ans)] + '\n')
                #display the answer for each question in answe paper file.
                
