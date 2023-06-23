# check whether the entered credentials are possibly valid
# usernames must only have alphanumeric characters, minimum length is 3
# password minimum length is 6
pass_min_length = 6
user_min_length = 3
#this comment should effect nothing

def verify_login(username, password):
    result = True
    if not isinstance(username, str):
        result = False
    elif not isinstance(password, str):
        result = False
    elif len(username) < user_min_length:
        result = False
    elif len(password) < pass_min_length:
        result = False
    elif not username.isalnum():
        result = False
    return result

