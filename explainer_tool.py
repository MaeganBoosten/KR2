import string
import os
import sys


def forget_next(pizza_features):
    """this function only adds items in a list to the signature file
        which wil be used to call the forgetting tool
    """

    sig = open("datasets/signature.txt", "a")
    
    for feature in pizza_features:
        sig.write("http://www.co-ode.org/ontologies/pizza/pizza.owl#")  # add the hyperlink first
        sig.write(feature + '\n')
    
    sig.close()


# --------------------------------------------------------
inputOntology = "datasets/pizza_super_simple.owl"
inputSubclassStatements = "datasets/subClasses.nt"
forgetOntology = "datasets/pizza_super_simple.owl"
method = '3'  # the method that is chosen
signature = "datasets/signature.txt"
allClassNames = ["American", "America", "Cajun", "CajunSpiceTopping", "CaperTopping", "Capricciosa", "Caprina",
                 "CheeseTopping", "CheeseyPizza", "VegetarianTopping", "Veneziana", "Italy", "England", "France",
                 "Germany", "hasBase", "hasIngredient", "isBaseOf", "isIngredientOf", "hasSpiciness", "hasTopping"]


# just to make it easier some functions for calling the jar files
def SaveSubclasses(inputOntology):
    os.system('java -jar kr_functions.jar ' + 'saveAllSubClasses' + " " + inputOntology)


def SaveExplanations(inputOntology, inputSubclassStatements):
    os.system(
        'java -jar kr_functions.jar ' + 'saveAllExplanations' + " " + inputOntology + " " + inputSubclassStatements)


def ForgetSignature(inputOntology, inputSubclassStatements, signature):
    os.system(
        'java -cp lethe-standalone.jar uk.ac.man.cs.lethe.internal.application.ForgettingConsoleApplication --owlFile ' + forgetOntology + ' --method ' + method + ' --signature ' + signature)


def forget_and_explain(inputOntology, inputSubclassStatements, features_to_forget):
    """This function calls the LETHE forget command and
        adds a new feature to the signature file every time it is called again  """
    SaveSubclasses(inputOntology)  # create the list of subclass statements for which justifications can be made
    SaveExplanations(inputOntology,
                     inputSubclassStatements)  # save all the explanations that justify these subclass statements

    sig = open("datasets/signature.txt", "a")
    sig.seek(0)
    sig.truncate()  # clear the signature file so we can add things to forget
    sig.close()
    for i in range(len(features_to_forget)):
        new_signature = []
        new_signature.append(features_to_forget[i])  # add the next item you want to forget to signature
        forget_next(new_signature)  # write to signature file
        ForgetSignature(inputOntology, inputSubclassStatements, signature)


# call explain and forget function
classes_to_forget = ["American", "America", "Cajun", "CajunSpiceTopping", "CaperTopping", "Capricciosa", "Caprina",
                 "CheeseTopping", "CheeseyPizza", "VegetarianTopping", "Veneziana", "Italy", "England", "France",
                 "Germany", "hasBase", "hasIngredient", "isBaseOf", "isIngredientOf", "hasSpiciness", "hasTopping"]

forget_and_explain(inputOntology, inputSubclassStatements, classes_to_forget)