import re
import json

def validate_username(username):

    if len(username) < 3:
        response ={
            'status' : False,
            'result' : 'username at least need 3 charecter'
        }
        resp = json.dumps(response)
        return resp
    
    if len(username) > 10:
        response ={
            'status' : False,
            'result' : 'username must be unedr 10 charecters'
        }
        resp = json.dumps(response)
        return resp
    
    if not username.isalnum() or '_' in username:
        response ={
            'status' : False,
            'result' : 'Username should only contain alphanumeric characters and underscores'
        }
        resp = json.dumps(response)
        return resp
    
    # Add more rules as per your requirements
    response ={
        'status' : True
    }
    resp = json.dumps(response)
    return resp

def validate_password(password):
    if len(password) < 5:
        response ={
            'status' : False,
            'result' : 'Password should contain 5 letters'
        }
        resp = json.dumps(response)
        return resp

        return False
    
    if not any(char.isupper() for char in password):
        response ={
            'status' : False,
            'result' : 'Password should contain at least one uppercase letter'
        }
        resp = json.dumps(response)
        return resp
    
    if not any(char.islower() for char in password):
        response ={
            'status' : False,
            'result' : 'Password should contain at least one lowercase letter'
        }
        resp = json.dumps(response)
        return resp
    
    if not any(char.isdigit() for char in password):
        response ={
            'status' : False,
            'result' : 'Password should contain at least one digit'
        }
        resp = json.dumps(response)
        return resp
        
    response ={
        'status' : True
    }
    resp = json.dumps(response)
    return resp



def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email):
        return True
    else:
        return False