# Write a Python program that operates a Deterministic Pushdown automata

# Step 1: Importing libraries

import sys 

# Step 2: Making a function that reads a DPDA description from a file that is specified on the command line and 
# stores the description in nested dictionaries

def read_data(filename):

    with open(filename, "r") as f:
        lines = f.read().splitlines()
        
        # Creating a list of letters in the alphabet of this DPDA file 
        alphabet = []
        
        for line in lines:
            if line.startswith("alphabet"):
                letters = line.split(" ")[1:]
                for letter in letters:
                    alphabet.append(letter)

        # Creating a list of states in this DPDA file
        dpda_states = []
        for line in lines:
            if line.startswith("states"):
                states = line.split(" ")[1:]
                for state in states:
                    dpda_states.append(state)

        # Defining the start and final state for this DPDA file
        for line in lines:
            if line.startswith("start"):
                start_state = line.split(" ")[1]
            if line.startswith("final"):
                final_state = line.split(" ")[1]   

        # Making the DPDA transitions dictionary

        dpda_transitions = {}

        for each_state in dpda_states:

            if each_state not in dpda_transitions:
                dpda_transitions[each_state] = {} 
        

        for line in lines:
            if line.startswith("trans"):
                transition_rule = line.split(" ")[1]

                current_state = transition_rule.split(":")[0]
                transition_symbol = transition_rule.split(":")[1]
                next_state = transition_rule.split(":")[2]
                stack_operation = transition_rule.split(":")[3]
                stack_symbol = transition_rule.split(":")[4]

                dpda_transitions[current_state][transition_symbol] = (next_state, stack_operation, stack_symbol)
        
    # Returning the values from this function
    return alphabet, start_state, final_state, dpda_transitions

# Step 3: Making a function that takes the DPDA data structure and the input string as input and returns True/False for ACCEPT/REJECT

def run_dpda(dpda_transitions, start_state, final_state, input_string):

    # Setting up the start state
    current_state = start_state

    # Stack starts with "$" at the bottom
    stack = ["$"]

    # Setting up the remaining input variable
    remaining_input = input_string

    while True:

        # Making a string version of the stack for printing
        stack_string = "".join(stack)

        # Printing the current configuration
        print((current_state, remaining_input, stack_string))

        # If no more remaining input left, then stop reading symbols
        if remaining_input == "":
            break

        #Reading the next input symbol
        symbol = remaining_input[0]
        remaining_input = remaining_input[1:]

        # If there is no transition for this symbol from this state, reject
        if symbol not in dpda_transitions[current_state]:
            print("REJECT")
            return False
        
        # look up the transitions
        next_state, stack_operation, stack_symbol = dpda_transitions[current_state][symbol]

        #Performing the stack operation

        if stack_operation == "push":
            # if there is no stack operation on a transition, leave the stack as it is
            if stack_symbol != "":
                stack.insert(0, stack_symbol)

        elif stack_operation == "pop":
             # if there is no stack operation on a transition, leave the stack as it is
            if stack_symbol != "":
                # if the stack is empty or the top of the stack does not match
                if len(stack) == 0 or stack[0] != stack_symbol:
                    print ("REJECT")
                    return False
                
                stack.pop(0)
        
        # Move to the next state
        current_state = next_state

    # After all input is read, accept the string based on whether we are in the final state or not
    if current_state == final_state:
        print("ACCEPT")
        return True
    else:
        print("REJECT")
        return False

# Step 4: Setting up the main program logic

def main():

    # Taking and validating the file name in the command line 
    if len(sys.argv) != 2:
        print("Usage: python3 DPDA.py d0.pda")
        sys.exit(1)

    dpda_file = sys.argv[1]

    # Reading and storing data from the file
    alphabet, start_state, final_state, dpda_transitions = read_data(dpda_file)
    
    while True:

        #Taking and validating user input string

        user_input = input("enter string to test: ")

        if user_input == "":
            print("Please input a Valid string")
            continue

        valid = True
        for letter in user_input:
            if letter not in alphabet:
                valid = False
                break

        if not valid:
            print(f"Please input a string made up of letters of the alphabet:{alphabet}")
            continue

        # Appending the user input string with "$" so that the input string can function with my DPDA transitions
        user_input = user_input+"$"

        # Running the DPDA
        run_dpda(dpda_transitions, start_state, final_state, user_input)

        #Repeating the loop
        while True:
            reply = input("Do you want to try another string (y/n)?")
            
            if reply not in ("y", "n"):
                print("Please input a valid next command")
                continue
            else:
                break

        if reply == "y":
            continue
        elif reply == "n":
            print("Bye!")
            break 


if __name__ == "__main__":
    main()

        


