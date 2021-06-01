#pclass	sex	age	sibsp	parch	fare	embarked

import pickle
loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
clf = pickle.loads(loaded_model)

def checkChanceOfSurvival(pclass,sex,age,siblings,parentchild,fare,embarked):
    if sex == "Male":
        sex = 0
    else:
        sex = 1
    
    if embarked == "True":
        embarked = 1
    else:
        embarked = 0

    outcome = clf.predict([[pclass,sex,age,siblings,parentchild,fare,embarked]])[0]
    #print("outcome = ",outcome)
    if outcome == 1:
        return "High chance of  Survival"
    else:
        return "Low chance of survival"


pclass = input("Passenger class\t")
sex = input("Passenger Gender\t")
age = input("Passenger Age\t")
siblings = input("No. of siblings\t")
parentchild = input("No. of parents or spouse\t")
fare = input("Fare\t")
outcome = checkChanceOfSurvival(pclass,sex,age,siblings,parentchild,fare,0)
print("Outcome is ",outcome)

# # Use the loaded pickled model to make predictions
#print(clf.predict([[2,1,29,0,0, 211,0]])[0])
  
