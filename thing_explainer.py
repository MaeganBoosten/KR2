
import string
import os
from myProgram import *


def forget_next(pizza_features):
    """this function only adds items in a list to the signature file
        which wil be used to call the forgetting tool
    """
    sig = open("datasets/signature.txt","a") 
    sig.seek(0)
    sig.truncate() #clear the file
    for feature in pizza_features:
        sig.write("\nhttp://www.co-ode.org/ontologies/pizza/pizza.owl#") #add the hyperlink first
        sig.write(feature)
    sig.close()


to_forget = ["ChickenTopping", "PizzaBase"] #the things that will be added to the file

forget_next(to_forget)

# to make the subclassstatements more legible by removing the hyperlinks
# def simplify(dataset):
#     f = open(dataset, "r")
#     for line in f:
#         scr = f.readline()
#         scr = scr.replace("http://www.co-ode.org/ontologies/pizza/pizza.owl#", "")
#         scr = scr.replace("http://www.w3.org/2000/01/rdf-schema#", "")
#         scr = scr.replace("http://www.w3.org/2000/01/rdf-schema#", "")
#         scr = scr.replace ("<subClassOf>", "is a")
#
#         print(scr)
#
# simplify("datasets\\subClasses.nt")
# simplify("datasets\exp-12.omn")
# simplify("result.owl")

#experimental UNFINISHED part for calling the explainer
#--------------------------------------------------------


#forgetOntology = inputOntology
def forget_and_explain(inputOntology, inputSubclassStatements, things_to_forget):
    method = '1'
    for i in things_to_forget:
        os.system('java -jar kr_functions.jar ' + 'printAllExplanations' + " " + inputOntology + " " + inputSubclassStatements)
        forget_next(i)
        signature = "datasets/signature.txt"
        os.system('java -cp lethe-standalone.jar uk.ac.man.cs.lethe.internal.application.ForgettingConsoleApplication --owlFile ' + forgetOntology + ' --method ' + method + ' --signature ' + signature)


forget_and_explain(inputOntology, inputSubclassStatements, to_forget)

