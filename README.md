# BigFiveQuiz
Big Five Personality Quiz for 326

## Instructions: 
When you open a terminal you have to type in " python BigFiveQuiz.py " then the 
program will run and as the user for their name, their age and their Gender, 
after that it will ask user to answer a series of question from our json file 
for evaluationg their personality trait.Then will have to answer the questions 
with a digit 1-5. If they choose something other than 1-5 it will ask them the 
same question again. If they put wrong input more than 5 times it will pop up a 
message saying " Clearly you don't pay attention to details." After the user done 
with answeing the questions, it will show up 5 different bar graph for our 
Big five traits Openness to experience, Conscientiousness, Extraversion, 
Agreeableness, 
Neuroticism.
Then it will show up a bar graph which will have the traits sorted out according 
to their answers. 
our program is designed to run from the terminal. To run it, open a terminal and
 ensure you are in the directory where your script and sample file are saved.
The program takes one required command-line argument (the path to a file of 
BigFiveQuiz, such as BigFiveQuiz.py). Below is an example of how to run the 
program. Mac users, type python instead of python3 when you run your program.
python BigFiveQuiz.py
## Attributions Table:


| Function/ Method        | Author         |Techniques Used              |
| ----------------        |:-----------:   | ------------------------:   |
| DisplayGraph()          | Afraah Goshu   | Tuple Unpacking             |
| DisplayGraph()          | Afraah Goshu   | Optional Parameters         |
| saveUserProfile()       | Garrett        |    With Statement           |
| UserProfile str()       | Garrett        |    F string                 |
| DisplayPie()            | Eveana         |  Data vis with pyplot       |
| BigFive str()           | Eveana         |    magic method             |
| calculate_score()       | CJ             |   use of a key function     |
| main()                  | CJ             |    List comprehension       |
| BigFive init()          | Arielle        |    Use of json.load         |
| startQuiz()             | Arielle        |  Conditional expression     |