number_key_algos = ['ceasar', 'transposition']
algos = ['ceasar', 'vigenere', 'substitution' ,'transposition']


def check_attribute_existance(request, attributes):
    for attribute in attributes:
        if request.get(attribute) == None:
            raise Exception(f'The "{attribute}" Attribute is missing in the Request')

def key_validation(algo:str, key):
    if algo in number_key_algos:
        if type(key) != int:
            raise Exception(f'The key is {type(key)} and it should be {int}')
    else:
        if type(key) != str:
            raise Exception(f'The key is {type(key)} and it should be {str}')
    

def validate_encrypt_request(request):
    
    # check attribute existence
    attributes = ['sender', 'algorithm', 'message', 'key', 'type']
    check_attribute_existance(request, attributes)
    is_int = lambda x : type(x) == int
    is_string = lambda x : type(x) == str
    # check types 
    attribute_checker = {
        'sender' : is_string,
        'algorithm': lambda x: is_string(x) and x in algos,
        'message': is_string,
        'key': lambda x: is_int if request['algorithm'] in number_key_algos else is_string(x)
    }

    for key in attribute_checker:
        if not attribute_checker[key](request[key]):
            raise Exception(f'Attribute {key} is incorrect')