import re


def intro():
    print(
        ''' Welcome to the **Madlib** Game! here you can fill a gaps ___ by using multi-typs of words: verbs,nouns, and adjectives to create a wone story.,, 
        let us try it *_^ '''
    )


def prompts(lst):
    input_arr = []
    for element in lst:
        user_input = input(f" enter a {element} :\t ")
        input_arr.append(user_input)
    return input_arr


def read_template(path):
    try:
        with open(path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {path}")


def parse_template(template):
    variables = re.findall(r"{([^}]+)}", template)
    stripped = re.sub("{ [^} ] + }", "{}", template)
    return stripped, tuple(variables)

def merge(template, parts):
    template = template.format(*parts)
    return template


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