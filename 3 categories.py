score = 0
strength1 = "amazing"
strength2 = "mid"
strength3 = "weak"
password = "sa" #can be changed to test different passwords
lenght = len(password)

if lenght < 10:
    score = 0
elif lenght >= 10 and lenght < 20:
    score += 10
else:
    score += 30

if score < 10 :
    print("You really need a new password")
    strength = "weak"
elif score == 10 :
    print("Not bad but could be better")
    strength = "mid"
else:
    print("Youre good at making passwords")
    strength = "amazing"

if score < 10: 
     print("twinkle twinkle little star how i wonder why youre so bad at making passwords")
elif score == 10:
     print("youre getting there but still not good enough")
else:
     print("baby shark doo doo doo doo doo doo")

print(password, "is your password and your score is", score, "its in the", strength, "category")
