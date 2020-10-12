from thing_explainer2 import forget_and_explain
import random
classes = ["American", "America", "Cajun", "CajunSpiceTopping", "CaperTopping", "Capricciosa", "Caprina", "CheeseTopping", "CheeseyPizza", "VegetarianTopping", "Veneziana", "Italy", "England", "France", "Germany", "hasBase", "hasIngredient", "isBaseOf", "isIngredientOf", "hasSpiciness", "hasTopping"]


inputOntology = "datasets/pizza_super_simple.owl"
inputSubclassStatements = "datasets/subClasses.nt"
forgetOntology = "datasets/pizza_super_simple.owl"
method = '2'    
signature = "datasets/signature.txt"
allClassNames = ["American", "America", "Cajun", "CajunSpiceTopping", "CaperTopping", "Capricciosa", "Caprina", "CheeseTopping", "CheeseyPizza", "VegetarianTopping", "Veneziana", "Italy", "England", "France", "Germany", "hasBase", "hasIngredient", "isBaseOf", "isIngredientOf", "hasSpiciness", "hasTopping"] 
result = "result.owl"


Orders = []
#forget every class name in 10 different orders
while (len(Orders) != 10): 
    newOrder = sorted(classes, key=lambda k: random.random()) #same as random shuffle 
    if newOrder not in Orders:
        print("Current Forgetting Order" + newOrder)
        Orders.append(newOrder)
        forget_and_explain(inputOntology, inputSubclassStatements, newOrder)
        

