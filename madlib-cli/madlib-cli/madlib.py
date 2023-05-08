'''
import method  used to import module as re that mean { regular expression operations}
to manipulate with strings and doing pattern of matching
then i importd sys as module to ineract with command lins
'''
import re
import sys
print (
    '''
    Welcome to the Madlib Game!

Madlib is a fun word game where we provide you with a story template with missing words. Your task is to fill in the blanks with the appropriate words to complete the story. Let's get started!

To play the Madlib game, follow these steps:

1. Run the Madlib program from the command line.
2. The program will present you with a story template that contains blanks for you to fill in.
3. Read the instructions provided in the story template to understand the type of word required for each blank (e.g., noun, verb, adjective).
4. Enter a word of the requested type for each blank when prompted.
5. Once you've entered a word for each blank, the program will generate the completed story using your inputs.
6. The program will then display the final story on the screen for you to enjoy!

Remember to be creative and have fun while filling in the words. Your inputs will determine the outcome of the story!

Ready to start? Let's play Madlib!

    '''
)

''' to create a template.txt file:
1. initlizing the location of txt file.
by using file _path then i choose location and name of this file.
2 . after creatinng a file you must open it and put it in variable called file, 
take care about moode =w to erite lins.
3. using write  method to write in it.
4. dont forget close your file

'''
file_path = "madlib-cli/template.txt" 
file = open(file_path, "w")
file.write("""
Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name}'s Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.
""")

file.close()
#************
'''

The (read_template) function is to read file that stored in file_path
then i used try ans exceptation error when a user want to read file is not exicit.

'''
def read_template(file_path):
    try:
        with open(file_path, 'r') as file:
            template = file.read()
            return template
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
#*******
'''
parse_templat: to enable the user to manipulate with the file 
py using regex findle function that takes 2 parmeter  for searching the something and return it as list
r'{(.*?)}' any cuerly prakets in template file
'''
def parse_template(template):
    placeholders = re.findall(r'{(.*?)}', template)
    return placeholders
'''

'''



def prompt_user(placeholders):
    user_inputs = {}
    for placeholder in placeholders:
        user_input = input(f"Enter {placeholder.lower()}: ")
        user_inputs[placeholder] = user_input
    return user_inputs

def populate_template(template, user_inputs):
    for placeholder, value in user_inputs.items():
        template = template.replace("{" + placeholder + "}", value)
    return template

def display_result(result):
    print("\nGenerated Madlib:\n")
    print(result)

def main():
    print("Welcome to Madlib CLI!")
    print("Please provide words to fill in the blanks in the given template.\n")

    if len(sys.argv) != 2:
        print("Error: Please provide the path to the template file as a command line argument.")
        sys.exit(1)

    template_file = sys.argv[1]
    template = read_template(template_file)
    placeholders = parse_template(template)
    user_inputs = prompt_user(placeholders)
    result = populate_template(template, user_inputs)
    display_result(result)
    def write_completed_text(completed_text):
        with open(file_path, "w") as file:
          file.write(completed_text)

# Call the write_completed_text function with the completed_text variable
    completed_text = populate_template(template, user_inputs)

    write_completed_text(completed_text)

if __name__ == "__main__":
    main()
