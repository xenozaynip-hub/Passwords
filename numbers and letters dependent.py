password = "44aaa4" #can be changed to test different passwords
score = 0

#Gives points based on length of password
length = len(password)
if length <= 5:
    score = 0
elif 5 < length < 15:
    score += 10
else:
    score += 20 

#points for having digets and letters
char = {}
for char in password:
    char = sum(1 for char in password if char.isdigit() or char.isupper() or char.islower())

#Subtracts points for repeated characters
repeated_char_counts = {}
for char in password:
    if char.isdigit() or char.isupper() or char.islower():
        repeated_char_counts[char] = repeated_char_counts.get(char, 0) + 1
for count in repeated_char_counts.values():
    if count > 1:
        score -= count

#print strength of password
if score < 10:
    strength = "Weak"
    print("You really need a new password",
          "Twinkle twinkle little star how i wonder why youre so bad at making passwords")
elif 10 <= score <= 15:
    strength = "Mid"
    print("Not bad but could be better",
          "Youre getting there but still not good enough")
else:
    strength = "Amazing"
    print("Youre good at making passwords ^^",
          "Microwave popcorn is better than stove popcorn")

print(f"{password} is your password and your score is {score}, its in the {strength} category")