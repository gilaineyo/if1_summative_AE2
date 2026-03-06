import re # Import regex module

def validate_form(form):
    '''
    Validates user's name and discipline inputs from Flask HTML form. Calls validate_name() for name input string, validates discipline in place by checking for empty string. 

    Returns error messages and/or valid values for user name and discipline inputs.

            Parameters:
                    form (werkzeug.datastructures.ImmutableMultiDict[str, str]): HTML form data from Flask request

            Returns:
                tuple[dict[str, str], dict[str, str]]
                    Tuple ``(errors, valid)`` where:
                    - errors : dict[str, str]
                        Maps field names to error messages where validation fails i.e. stores a key of "disipline" and value "Select your discipline" where discipline input is invalid.
                    - valid : dict[str, str]
                        Stores values against keys of "name" and "discipline" where inputs from the form are assessed as valid
                    
    '''
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
    '''
    Validates name passed by the validate_form() function.
     
    Checks for empty string (when stripped of leading and trailing whitespace) and regex match allowing all alpha characters, hyphens and whitespace.

    Returns a cleaned version of the input string if validation passed, or a bespoke error message string.

            Parameters:
                    input (str): name input string obtained by validate_form() from HTML form data from Flask request

            Returns:
                    str: cleaned input string or one of two error message strings
                    
    '''
    if (input.strip() == ""):
        return "Enter your name"
    else:
        if (re.fullmatch(r'[a-zA-Z-\s]+', input.strip())):
            return input.strip()
        else:
            return "Your name must only contain letters, spaces and hyphens"
        
def validate_question(form):
    '''
    Checks than an answer has been selected upon attempted submission.

            Parameters:
                    form (werkzeug.datastructures.ImmutableMultiDict[str, str]): HTML form data from Flask request

            Returns:
                    str or None: error message string returned if input is empty string, otherwise returns None
                    
    '''
    answer_input = form.get("answerInput", "")
    if not answer_input:
        return "Please select an answer"
    return None
