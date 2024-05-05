##
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class UserProfile:
    
    def __init__(self, name, age, gender, scores):
        
        self.name=name
        self.age=age
        self.gender=gender
        #score tracker
        self.scores=scores
        """{'Extraversion': {'EXT1': 0, 'EXT2': 0, 'EXT3': 0,'EXT4': 0, 'EXT5': 0, 'EXT6': 0,'EXT7': 0, 'EXT8': 0, 'EXT9': 0, 'EXT10':0 },
                        'Agreeableness': {'AGR1': 0, 'AGR2': 0, 'AGR3': 0, 'AGR4': 0, 'AGR5': 0, 'AGR6': 0, 'AGR7': 0, 'AGR8': 0, 'AGR9': 0, 'AGR10': 0},
                        'Conscientiousness': {'CSN1': 0, 'CSN2': 0, 'CSN3': 0, 'CSN4': 0, 'CSN5': 0, 'CSN6': 0, 'CSN7': 0, 'CSN8': 0, 'CSN9': 0, 'CSN10':0},
                        'Neuroticism': {'EST1': 0, 'EST2': 0, 'EST3': 0, 'EST4': 0, 'EST5': 0, 'EST6': 0, 'EST7': 0, 'EST8': 0, 'EST9': 0, 'EST10': 0},
                        'Openness': {'OPN1': 0, 'OPN2': 0, 'OPN3': 0, 'OPN4': 0, 'OPN5': 0, 'OPN6': 0, 'OPN7': 0, 'OPN8': 0, 'OPN9': 0, 'OPN10': 0}
                        }"""

        
        #json profile
        self.profileJSON={self.name:self.scores}
        
    def DisplayGraph(self, type="user"):
        """DisplayGraph will display a graph based on the type passed in.
        (1)total graph: displays results from all users in directory
        (2)avg trait graph: displays avg responses for each trait for ALL users 
        (3)user graph: displays graph for responses in self

        Args:
            self (UserProfile): self profile to display 
            other (UserProfile): other graph to be compared to?
            type (str): _description_
        """
        
        # x axis is big five, y axis is the number of responses 
        # will need to loop through dictionary to convert responses to list for optimal output for graph
        #convert questions and responses to list objects

        extraRES=[]
        extraQ=[]
        for q,answers in self.scores['Extraversion'].items():
            extraQ.append(q)
            extraRES.append(answers)
        print(extraRES)
            
        agrRES=[]
        agrQ=[]
        for q,answers in self.scores['Agreeableness'].items():
            agrQ.append(q)
            agrRES.append(answers)
        print(agrRES)
        
        consRES=[]
        consQ=[]
        for q,answers in self.scores['Conscientiousness'].items():
            consQ.append(q)
            consRES.append(answers)
        print(consRES)
        
        neuroRES=[]
        neuroQ=[]
        for q,answers in self.scores['Neuroticism'].items():
            neuroQ.append(q)
            neuroRES.append(answers)
        print(neuroRES)
        
        openRES=[]
        openQ=[]
        for q,answers in self.scores['Openness'].items():
            openQ.append(q)
            openRES.append(answers)
        print(openRES)
        
        
        #self.scores keys: Extraversion, Agreeableness, Conscientiousness, Neuroticism, Openness
        
        #convert questions and responses to dataframe object
        extraDF=pd.DataFrame({'Extraversion Responses': extraRES, 'Extraversion Questions': extraQ})
        agrDF=pd.DataFrame({'Agreeableness Responses': agrRES, 'Agreeableness Questions': agrQ})
        consDF=pd.DataFrame({'Conscientiousness Responses': consRES, 'Conscientiousness Questions': consQ})
        neuroDF=pd.DataFrame({'Neuroticism Responses': neuroRES, 'Neuroticism Questions': neuroQ})
        openDF=pd.DataFrame({'Openness Responses': openRES, 'Openness Questions': openQ} )
        
        print(extraDF)
        print(agrDF)
        print(consDF)
        print(neuroDF)
        print(openDF)
        
        # (1) total graph: displays results from all users in directory
        if type == "total":
            
            print()
        
        # (2) avg trait graph: displays avg responses for each trait for ALL users 
        if type == "avg":
            
            print()
        
        
        # (3) user graph: displays graph for responses in self for each category
        if type == "user":
            
            
            #df.plot.bar(x, y)
            #need to figure out appropriate method to implement 
            extraDF.plot(kind='bar', x="Extraversion Questions", y="Extraversion Responses")
            agrDF.plot(kind='bar', x="Agreeableness Questions", y="Agreeableness Responses")
            consDF.plot(kind='bar',x="Conscientiousness Questions", y="Conscientiousness Responses")
            neuroDF.plot(kind='bar', x="Neuroticism Questions", y="Neuroticism Responses")
            openDF.plot(kind='bar', x="Openness Questions", y="Openness Responses")
            
            plt.show()

        
    
    def CompareUser(self, otherUser):
        """Checks if user is in directory

        Args:
            otherUser (UserProfile): other user to be compared to

        Returns:
            (boolean): if user is in directory
        """
        
        if self.name==otherUser.name:
            return True
        return False

    def __str__(self):
        """
            Gives a greeting for the user
            Returns: self.name
        """
        return f"Hi {self.name} !"

    def getProfile(self):
        """
            Retrieves data from JSON file
            Returns: self.JSON
        """
        return self.profileJSON
    
def userInput(big_five_obj, user_profile_obj):
    """
    Function that handles user input for the BigFive personality quiz. It interacts with the user
    to gather responses to personality trait questions. Once all responses are collected, a new UserProfile
    object is created and added to a list of users.

    Parameters:
    big_five_obj (BigFive): An instance of the BigFive class that contains and manages the personality quiz.
    user_profile_obj (UserProfile): An instance of the UserProfile class where the user's personal data and quiz responses are stored.

    Returns:
    list: Returns a list containing the updated or newly created user profiles.
    """
    big_five_obj.start_quiz(user_profile_obj)  
    
def display_question(self, user_name, questions):
    """
    Displays a formatted question to the user with their name included. This method is used during
    a quiz session to present each question in a personalized format, enhancing the user's engagement.

    Parameters:
    user_name (str): The name of the user taking the quiz, used to personalize the question display.
    question (str): The text of the question to be displayed.
    """
    print(f"{user_name}:\n{questions}")

def calculate_score(scores):
    """
    Calculates overall scores for each Big Five personality traits based on user's responses.

    Args:
        scores (dict): Dictionary containing user responses for each personality trait.

    Returns:
        dict: Dictionary containing the overall scores for each personality trait.
    """
    trait_scores = {}
    for trait, responses in scores.items():
        total_score = sum(response[trait] for response in responses)
        trait_scores[trait] = total_score / len(responses)
    return trait_scores

 
class BigFive:
    """Represents BigFive Quiz
    
    Attributes:
        jsonFile (str): Path to JSON file containing BigFive quiz questions
        userProfile: UserProfile object for user taking the BigFive quiz
    """
    def __init__(self, jsonFile, userProfile):
        """Initializes BigFive class object

        Args:
            jsonFile : Path to the file containing BigFlive quiz questions
            userProfile : UserProfile object for user taking the BigFive quiz
        """
        self.userProfile = userProfile
        with open("quiz_questions.json", "r") as jsonFile:
            self.questions = json.load(jsonFile)
    def __str__(self):
        """
        Returns a string representation of the user profile associated with an instance of the class.
        This method provides a convenient way to quickly view the user profile's contents in a string format,
        which can be useful for debugging or logging purposes.

        Returns:
        str: A string representation of the user profile data.
        """
        return str(self.user_profile)

    def startQuiz(self):
        """Starts Big Five Personality Quiz and updates responses
        """
        for trait, questions in self.questions.items():
            print(f"{questions}")
            response = int(input(f"Enter your answer for {trait} trait, Please enter a number between 1-5: "))
            if 1 <= response <= 5:
                self.userProfile.scores[trait].append({trait: response})
            else:
                print("Invalid, Enter a number between 1-5.")
                
    def saveUserProfile(self, filepath):
        """Saves user personality test results

        Args:
            filepath (str): JSON file path
        """
        with open(filepath, "w") as f:
            json.dump(self.userProfile.getProfile(), f)

def main():
    """
    Executes Big Five Quiz
    """
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    jsonFile = "quiz_questions.json"  # Provide the path to your JSON file.
    questions = jsonFile
    user_profile = UserProfile(name, age, gender, {
        'Extraversion': [], 'Agreeableness': [],
        'Conscientiousness': [], 'Neuroticism': [],
        'Openness': []
    })
<<<<<<< HEAD
    big_five = BigFive(questions, user_profile)
    big_five.startQuiz()
=======
    big_five = BigFive(jsonFile, user_profile)
    big_five.start_quiz(user_profile)
>>>>>>> f50a4663347758efd101e9298a2cee7c67782ae8
    trait_scores = calculate_score(user_profile.scores)
    for trait, score in trait_scores.items():
        print(f"{trait}: {score}")
    print(user_profile)



    
if __name__== "__main__":
    main()