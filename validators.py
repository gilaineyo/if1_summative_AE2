import re # Import regex module

def validate_form(form):
    errors = {}
    valid = {}
    name_input = form.get("nameInput", "")
    discipline_input = form.get("discipline", "")

    if not discipline_input:
        errors["discipline"] = "Select your discipline"
    else:
        valid["discipline"] = discipline_input

    name_result = validate_name(name_input)

    if (name_result != name_input.strip()):
        errors["name"] = name_result
    else:
        valid["name"] = name_result
    
    return errors, valid

def validate_name(input):
    """Validates name input from start page"""
    if (input.strip() == ""):
        return "Enter your name"
    else:
        if (re.fullmatch(r'[a-zA-Z-\s]+', input.strip())):
            return input.strip()
        else:
            return "Your name must only contain letters, spaces and hyphens"
        
def validate_question(form):
    answer_input = form.get("answerInput", "")
    if not answer_input:
        return "Please select an answer"
    return None
