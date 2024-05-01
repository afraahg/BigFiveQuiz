import json
import pandas as pd
import seaborn as sns

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
        for q,answers in self.scores['Extraversion']:
            extraQ.append(q)
            extraRES.append(answers)
            
        agrRES=[]
        agrQ=[]
        for q,answers in self.scores['Agreeableness']:
            agrQ.append(q)
            agrRES.append(answers)
        
        consRES=[]
        consQ=[]
        for q,answers in self.scores['Conscientiousness']:
            consQ.append(q)
            consRES.append(answers)
        
        neuroRES=[]
        neuroQ=[]
        for q,answers in self.scores['Neuroticism']:
            neuroQ.append(q)
            neuroRES.append(answers)
            
        openRES=[]
        openQ=[]
        for q,answers in self.scores['Openness']:
            openQ.append(q)
            openRES.append(answers)
        
        
        
        #self.scores keys: Extraversion, Agreeableness, Conscientiousness, Neuroticism, Openness
        
        #convert questions and responses to dataframe object
        extraDF=pd.DataFrame({'Extraversion Responses': extraRES}, {'Extraversion Questions': extraQ})
        agrDF=pd.DataFrame({'Agreeableness Responses': agrRES }, {'Agreeableness Questions': agrQ})
        consDF=pd.DataFrame({'Conscientiousness Responses': consRES}, {'Conscientiousness Questions': consQ})
        neuroDF=pd.DataFrame({'Neuroticism Responses': neuroRES}, {'Neuroticism Questions': neuroQ})
        openDF=pd.DataFrame({'Openness Responses': openRES}, {'Openness Questions': openQ} )
        
        
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
            print(extraDF.plot.bar(x="Extraversion Questions", y="Extraversion Responses"))
            print(agrDF.plot.bar(x="Agreeableness Questions", y="Agreeableness Responses"))
            print(consDF.plot.bar(x="Conscientiousness Questions", y="Conscientiousness Responses"))
            print(neuroDF.plot.bar(x="Neuroticism Questions", y="Neuroticism Responses"))
            print(openDF.plot.bar(x="Openness Questions", y="Openness Responses"))
        


if __name__== "__main__":
    
    # user profile init: (name, age, gender, scores)
    answerFile=None
    sampleProfile=None
    with open("quiz_questions_answers.json", "r") as file:
        answerFile = json.load(file)
        
    print(answerFile)
    for person,answers in answerFile:
        sampleProfile= UserProfile(person, 21, 'M', answers)
            
    sampleProfile.DisplayGraph()
    