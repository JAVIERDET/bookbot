#! python3
import string

def create_dict() -> dict:
    """
    Creates a dict where keys are alphabet characters and values are None
    """
    return {letter:None for letter in string.ascii_lowercase}

def count_characters(text:str) -> dict:
    """
    Counts the number of times a character is used within a text and stores the
    result in a dict
    """
    # Create dict with empty values (None)
    alph_dict = create_dict()

    # Lowercase the text
    text_lc = text.lower()

    # Count and store the value
    for key in alph_dict.keys():
        alph_dict[key] = text_lc.count(key)

    return alph_dict

def order_dicts(data_dict:dict) ->list[dict]:
    """
    Takes a dict with string-int key-values pair and returns an ordered dict list
    """

    # Create non-ordered list of tuples
    tp_list =[]
    for key, value in data_dict.items():
        tp_list.append((value,key))

    # Order the list of tuples
    tp_list.sort(reverse=True)

    # Create the list of dicts
    dict_list = []
    for tp in tp_list:
        dict_list.append({
            "char":tp[1],
            "value":tp[0]
        })

    return dict_list

def count_words(text:str)->None:
    """
    Returns the number of words of a text.
    """
    return len(text.split())
