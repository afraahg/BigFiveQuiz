##
import json

class UserProfile:
    
    def __init__(self, name, age, gender, scores):
        
        self.name=name
        self.age=age
        self.gender=gender
        #score tracker
        self.scores=scores
        
        #json profile
        self.profileJSON={self.name:self.scores}
        
    def DisplayGraph():
        
        #pass in different values to display different type of graph?
        #to compare # of reson
        
        # x axis is big five, y axis is the number of responses 
        #histogram
        #
        
        
        pass
    
    def CompareUser(otherUser):
        #json dump, load or something here
        pass

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
        return self.JSON
    
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
    
def display_question(self, user_name, question):
    """
    Displays a formatted question to the user with their name included. This method is used during
    a quiz session to present each question in a personalized format, enhancing the user's engagement.

    Parameters:
    user_name (str): The name of the user taking the quiz, used to personalize the question display.
    question (str): The text of the question to be displayed.
    """
    print(f"{user_name}:\n{question}")

def __str__(self):
    """
    Returns a string representation of the user profile associated with an instance of the class.
    This method provides a convenient way to quickly view the user profile's contents in a string format,
    which can be useful for debugging or logging purposes.

    Returns:
    str: A string representation of the user profile data.
    """
    return str(self.user_profile)
 
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
        with open(jsonFile) as f:
            self.questions = json.load(f)

    def startQuiz(self):
        """Starts Big Five Personality Quiz and updates responses
        """
        for trait, question in self.questions.items():
            print(f"{question}")
            response = int(input(f"Enter your answer for {trait} trait, Please enter a number between 1-5: "))
            if 1 <= response <= 5:
                self.userProfile.scores[trait].append(response)
            else:
                print("Invalid, Enter a number between 1-5.")
                
    def saveUserProfile(self, filepath):
        """Saves user personality test results

        Args:
            filepath (str): JSON file path
        """
        with open(filepath, "w") as f:
            json.dump(self.userProfile.getProfile(), f)

def calculate_score(scores):
    """
    Calculates overall scores for each Big Five personality traits based on user's responses.

    Args:
        scores (dict): Dictionary containing user responses for each personality trait.

    Returns:
        dict: Dictionary containing the overall scores for each personality trait.
    """
    trait_scores = {}
    for trait, answers in scores.items():
        total_score = sum(answers.values())
        trait_scores[trait] = total_score / len(answers)
    return trait_scores

def main():
    """
    Executes Big Five Quiz
    """
    with open("quiz_questions.json", "r") as file:
        questions = json.load(file)
    big_five = BigFive(questions)
    user_profile = UserProfile()
    big_five.start_quiz(user_profile)
    trait_scores = calculate_score(user_profile.scores)
    for trait, score in trait_scores.items():
        print(f"{trait}: {score}")
    print(user_profile)

