import re 

def check_password_strength(password):
    length_error = len(password) < 8

    has_uppercase = bool(re.search(r'[A-Z]',password))
    has_lowercase = bool(re.search(r'[a-z]',password))
    has_digit = bool(re.search(r'[0-9]',password))
    has_special = bool(re.search(r'[!@#$%^&*();:[]{}|]',password))


    #Calculate the strength based on criteria
    strength_score = 0
    if length_error:
        return "Password is too short (minimum 8 characters)"
    else:
        strength_score += 1

    if has_uppercase:
        strength_score += 1
    if has_lowercase:
        strength_score += 1
    if has_digit:
        strength_score += 1
    if has_special:
        strength_score += 1

    #provide feedback based on the strength password
    if strength_score < 4:
        return "password is too weak"
    if strength_score == 4:
        return "password is moderate"
    else:
        return "password is strong"

#Example usage
password = input("enter your password: ")
print(check_password_strength(password))
