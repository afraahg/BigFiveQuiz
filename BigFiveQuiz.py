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
    Function that handles user input for the bigfive quiz.
    It takes two arguments: an instance of the BigFive class and an instance of UserProfile class.
    The function will continue asking questions until it  has gathered all necessary information.
    After gathering all information, it will  create a new UserProfile object with this information 
    and add it to the list of users. 
  """
    big_five_obj.start_quiz(user_profile_obj)  

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

