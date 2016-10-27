#function to convert a string of words seperated by spaces into list of words
def string_to_array(string):
    #check for empty string
    if not string:
        return ['']
    #string splits into list by default on space character
    return string.split()
