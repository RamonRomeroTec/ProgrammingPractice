

ds=[
    {"Survived":0,"Pclass": 3, "Sex":"Male", "Age":22, "SibS":1, "Parch":3, "Fare": 33, "Cabin": "xsc", "Embarked": "s"},
    {"Survived":0,"Pclass": 3, "Sex":"Female", "Age":22, "SibS":1, "Parch":3, "Fare": 33, "Cabin": "xsc", "Embarked": "s"},
    ]

a = {}
allPopulations=len(ds)
count_males=0
avg=0
avg_men=0
avg_w=0
for i in ds:
    if i["Sex"]=="Male":
        count_males=count_males+1
        avg_men=avg_men+i["Age"]
    else:
        avg_w=avg_w+i["Age"]
    
    avg=avg+i["Age"]

avg=avg/allPopulations

count_femeales=allPopulations-count_males
avg_men=avg_men/count_males
avg_w=avg_w/count_femeales

print(allPopulations ,avg, avg_men, avg_w, count_femeales, count_males)



