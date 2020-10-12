output = open("output.txt")
all_lines_output = output.readlines()
axioms_file = open("output_axioms", "a")
axioms_size_file = open("output_axioms_size", "a")
definers_file = open("output_definers", "a")
restrictions_file = open("output_restrictions", "a")
for line in all_lines_output:
    if "Result Number of Axioms" in line:
        axioms_file.write(line)
    elif "Result Average Axiom size" in line:
        axioms_size_file.write(line)
    elif "Result Definers" in line:
        definers_file.write(line)
    elif "Result Number Restrictions" in line:
        restrictions_file.write(line)

axioms_file.close()
axioms_size_file.close()
definers_file.close()
restrictions_file.close()
