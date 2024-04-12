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
    Main function to execute the Big Five personality quiz.
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

