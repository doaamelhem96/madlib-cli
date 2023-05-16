import re


def intro(): # create an Welcomming message to user.
    print(
        ''' Welcome to the **Madlib** Game! here you can fill a gaps ___ by using multi-typs of words: verbs,nouns, and adjectives to create a wone story.,, 
        let us try it *_^ '''
    )


def prompts(lst): # to help user to filling gaps.
    input_arr = []
    for element in lst:
        user_input = input(f" enter a {element} :\t ")
        input_arr.append(user_input)
    return input_arr


def read_template(path): # read a file by using with -syntax. and treate with exceptation and rise error to treate with error 
    try:
        with open(path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {path}")
'''
This function takes a template string as input.
 It uses regular expressions (re.findall()) to extract variables
 enclosed in curly braces ({}). 
 The function then removes the variable placeholders from the template string using re.sub() and replaces them with a simplified placeholder {}. 
 Finally, it returns the stripped template string 
and a tuple of extracted variables.
'''

def parse_template(template): 
    variables = re.findall(r"{([^}]+)}", template)
    stripped = re.sub("{ [^} ] + }", "{}", template)
    return stripped, tuple(variables)
'''
 This function takes a template string and a sequence of 
 parts as input. It uses the str.format() method to 
 substitute the parts into the template,
   creating a merged template string.
 The merged template string is then returned.


'''

def merge(template, parts):
    template = template.format(*parts)
    return template

'''
 This function takes a merged template string as input.
 It opens a file named "new-file.txt" located in the "../assests" directory in write mode ("w"). It writes the merged template content
 into the file and then closes it.
'''
def new_file(merged_template):
    with open("../assests/new-file.txt", "w") as f:
        f.write(merged_template)


if __name__ == "__main__":
    intro()
    returned_content = read_template("../assests/example.txt")
    stripped, parts = parse_template(returned_content)
    user_prompts = prompts(parts)
    merged_txt = merge(stripped, user_prompts)
    print(merged_txt)
    new_file(merged_txt)