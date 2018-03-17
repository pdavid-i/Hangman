class WordException(Exception):
    pass

def validate_word(string):
    for c in string:
        if c < 'A' or c > 'z':
            raise WordException("Format not permitted")
    return True
