from validators import validate_name

def test_validate_name_empty():
    input = ""
    result = validate_name(input)
    assert isinstance(result, str)
    assert result == "Enter your name"

def test_validate_name_whitespace():
    input = "               "
    result = validate_name(input)
    assert isinstance(result, str)
    assert result == "Enter your name"

def test_validate_name_invalid_chars():
    input_number = "Sarah123"
    input_symbol = "+John/?"
    result_number = validate_name(input_number)
    result_symbol = validate_name(input_symbol)

    assert isinstance(result_number, str)
    assert isinstance(result_symbol, str)
    assert result_number == "Your name must only contain letters, spaces and hyphens"
    assert result_symbol == "Your name must only contain letters, spaces and hyphens"

def test_validate_name_allows_upper_lower():
    input = "Marisol"
    result = validate_name(input)
    assert isinstance(result, str)
    assert result == "Marisol"
    
    
def test_validate_name_allows_hyphen():
    input = "Mary-Jane"
    result = validate_name(input)
    assert isinstance(result, str)
    assert result == "Mary-Jane"

def test_validate_input_allows_central_space():
    input = "Emperor Palpatine"
    result = validate_name(input)
    assert isinstance(result, str)
    assert result == "Emperor Palpatine"