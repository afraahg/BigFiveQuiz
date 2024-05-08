# BigFiveQuiz
Big Five Personality Quiz for 326

## Instructions: 
When you open a terminal you have to type in " python BigFiveQuiz.py " then the 
program will run and ask the user for their 
-name (str)
-age (int)
-gender (str)
After that, it will ask users to answer a series of 50 questions from our json file 
for evaluating their personality traits. (10 Questions for each measurable trait)
These questions will appear one after the other and users will be expected to 
respond with a digit 1-5. 
If users respond with something other than 1,2,3,4, or 5 users will be asked to  
answer the question again. 
If the wrong input is detected more than 5 times a message will appear:
 " Clearly you don't pay attention to details." 
After the user completes all 50 ranked questions, 5 bar graphs will appear.
These bar graphs serve as visual depictions for each trait and the responses 
users gave to each of the 10 questions users answered. The X axis contains each
traits ID and the y axis are numbers that depict the ranking users answered with.
After that, a pie chart containing the Big 5 Traits, Openness to experience, 
Conscientiousness, Extraversion, Agreeableness, and Neuroticism will be split
into percentage sections that add up to 100%.
Shortly after, a file by the name of bigfive_ouput will update with the users 
name and the averages to each of their traits scores.
Our program is designed to run from the terminal. 
To run it, open a terminal and ensure that you are in the directory where 
your script and sample file are saved.
The program takes one required command-line argument (the path to a file of 
BigFiveQuiz, such as BigFiveQuiz.py). 
Below is an example of how to run the program and what should be entered into
your terminal. 
Mac users, type python3 instead of python when you run your program.
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