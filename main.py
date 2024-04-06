# Built-in imports
def reverse(text):
    """
    Reverses a given string text
    Parameter
    ----------
    text: str
        text to be reversed
        
    Returns
    --------
    str
    reversed text
    """
    if len(text) == 0: #basecase
        return ''
    if len(text) == 1:
        return text
    else:
        return text[-1] + reverse(text[:-1]) 
    
def is_palindrome(text):
    """
    Checks if a given string is a palindrome
    Parameter
    ----------
    text: str
        text to be checked if it is a palindrome

    Returns
    --------
    Boolean
    True if text is a Palindrome
    False if text is not a Palindrome
    """
    if len(text) == 0:
        return True
    if len(text) == 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False




    
