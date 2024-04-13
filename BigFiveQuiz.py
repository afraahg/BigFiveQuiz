##
import json
import pandas as pd

class UserProfile:
    
    def __init__(self, name, age, gender, scores):
        
        self.name=name
        self.age=age
        self.gender=gender
        #score tracker
        self.scores={'Extraversion': {'EXT1': 0, 'EXT2': 0, 'EXT3': 0,'EXT4': 0, 'EXT5': 0, 'EXT6': 0,'EXT7': 0, 'EXT8': 0, 'EXT9': 0, 'EXT10':0 },
                        'Agreeableness': {'AGR1': 0, 'AGR2': 0, 'AGR3': 0, 'AGR4': 0, 'AGR5': 0, 'AGR6': 0, 'AGR7': 0, 'AGR8': 0, 'AGR9': 0, 'AGR10': 0},
                        'Conscientiousness': {'CSN1': 0, 'CSN2': 0, 'CSN3': 0, 'CSN4': 0, 'CSN5': 0, 'CSN6': 0, 'CSN7': 0, 'CSN8': 0, 'CSN9': 0, 'CSN10':0},
                        'Neuroticism': {'EST1': 0, 'EST2': 0, 'EST3': 0, 'EST4': 0, 'EST5': 0, 'EST6': 0, 'EST7': 0, 'EST8': 0, 'EST9': 0, 'EST10': 0},
                        'Openness': {'OPN1': 0, 'OPN2': 0, 'OPN3': 0, 'OPN4': 0, 'OPN5': 0, 'OPN6': 0, 'OPN7': 0, 'OPN8': 0, 'OPN9': 0, 'OPN10': 0}
                        }

        
        #json profile
        self.profileJSON={self.name:self.scores}
        
    def DisplayGraph(self, type="user"):
        """DisplayGraph will display a graph based on the type passed in.
        (1)total graph: displays results from all users in directory
        (2)avg trait graph: displays avg responses for each trait for ALL users 
        (3)user graph: displays graph for responses in self

        Args:
            type (str): _description_
        """
        
        #pass in different values to display different type of graph?
        #to compare # of reson
        
        # x axis is big five, y axis is the number of responses 
        #histogram
        df=pd.DataFrame(self.scores)
        
        # (1)
        
        # (2)
        # (3)
        totalScores=df.sum()
        userGraph=df.plot.hist()

        print(userGraph)
    
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
        return f"Hi {self.name} !"

    def getProfile(self):
        return self.profileJSON
    

class BigFive:
    def __init__(self, jsonFile, userProfile):
        self.userProfile = userProfile
        with open(jsonFile) as f:
            self.questions = json.load(f)

    def startQuiz(self):
        for trait, question in self.questions.items():
            print(f"{question}")
            response = int(input(f"Enter your answer for {trait} trait, Please enter a number between 1-5: "))
            if 1 <= response <= 5:
                self.userProfile.scores[trait].append(response)
            else:
                print("Invalid, Enter a number between 1-5.")
                
    def saveUserProfile(self, filepath):
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

