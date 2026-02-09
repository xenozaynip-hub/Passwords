#change this to test different passwords
password = "adcx03ß2sasx"

def calculate_password_score(password: str) -> int:
    score = 0   

    #Gives points based on length of password
    length = len(password)
    if length <= 5:
        score = 0
    elif 5 < length < 15:
        score += 10
    else:
        score += 20 

    #points for having digits, letters and special characters
    has_digits = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)    
    has_lower = any(char.islower() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if has_digits:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_special:
        score += 2

    #Subtracts points for repeated characters
    repeated_char_counts: dict[str, int] = {}
    for char in password:
            repeated_char_counts[char] = repeated_char_counts.get(char, 0) + 1
    for count in repeated_char_counts.values():
        if count > 1:
            score -= count

    return score

#determines password strength category based on score
def calculate_password_strength(score: int) -> tuple[str, str]:
    if score <= 0:
        return "jeez-", "is that even considered as a password?"
    elif 0 < score < 10:
        return "Weak", "You really need a new password. Twinkle twinkle little star how i wonder why youre so bad at making passwords"
    elif 10 <= score <= 15:
        return "Mid", "Not bad but could be better. Youre getting there but still not good enough"
    else:
        return "Amazing", "Youre good at making passwords ^^. Microwave popcorn is better than stove popcorn"

#prints strength of password
def output_password_score(password: str, score: int, strength: str, message: str) -> None:
    print(message)
    print(f"{password} is your password and your score is {score}, its in the {strength} category")

if __name__ == "__main__":
    score = calculate_password_score(password)
    strength, message = calculate_password_strength(score)
    output_password_score(password, score, strength, message)