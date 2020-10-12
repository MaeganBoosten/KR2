import os

# This is an example puython programme which shows how to use the different stand-alone versions of OWL reasoners and forgetting programme

# Choose the ontology (in the OWL format) for which you want to explain the entailed subsumption relations.
inputOntology = "datasets/pizza_super_simple.owl"

# Choose the set of subclass for which you want to find an explanation.
# this file can be generated using the second command (saveAllSubClasses)
inputSubclassStatements = "datasets/subClasses.nt"

# Choose the ontology to which you want to apply forgetting. This can be the inputOntology, but in practise
# should be a smaller ontology, e.g. created as a justification for a subsumption
forgetOntology = "datasets/pizza_super_simple.owl"

# Decide on a method for the forgetter (check the papers of LETHE to understand the different options).
# The default is 1, I believe.
# 1 - ALCHTBoxForgetter
# 2 - SHQTBoxForgetter
# 3 - ALCOntologyForgetter
method = "2" #

# Choose the symbols which you want to forget.
signature = "datasets/signature.txt"

# 1. PRINT ALL SUBCLASSES (inputOntology):
# print all subClass statements (explicit and inferred) in the inputOntology
# --> uncomment the following line to run this function
#os.system('java -jar kr_functions.jar ' + 'printAllSubClasses' + " " + inputOntology)

# 2. SAVE ALL SUBCLASSES (inputOntology):
# save all subClass statements (explicit and inferred) in the inputOntology to file datasets/subClasses.nt
# --> uncomment the following line to run this function
#os.system('java -jar kr_functions.jar ' + 'saveAllSubClasses' + " " + inputOntology)

# 3. PRINT ALL EXPLANATIONS (inputOntology, inputSubclassStatements):
# print explanations for each subClass statement in the inputSubclassStatements
# --> uncomment the following line to run this function
#os.system('java -jar kr_functions.jar ' + 'printAllExplanations' + " " + inputOntology + " " + inputSubclassStatements)

# 4. SAVE ALL EXPLANATIONS (inputOntology, inputSubclassStatements):
# save explanations for each subClass statement in the inputSubclassStatements to file datasets/exp-#.owl
# --> uncomment the following line to run this function
# os.system('java -jar kr_functions.jar ' + 'saveAllExplanations' + " " + inputOntology + " " + inputSubclassStatements)


# For running LETHE forget command:
# --> uncomment the following line to run this function
os.system('java -cp lethe-standalone.jar uk.ac.man.cs.lethe.internal.application.ForgettingConsoleApplication --owlFile ' + forgetOntology + ' --method ' + method  + ' --signature ' + signature)

