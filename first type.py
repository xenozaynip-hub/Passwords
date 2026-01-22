score = 0
strength = "amazing"
stregth = "weak"
password = "sadawwsda"

if len(password) < 6:
    score = 0
else:
    score += 20
    score *= 2

if score < 6 :
    print("you really need a new password")
    strength = "weak"
else:
    print("youre good at making passwords")
    strength = "amazing"

if score <= 6: 
     print("twinkle twinkle little star how i wonder why youre so bad at making passwords")
else:
     print("baby shark doo doo doo doo doo")

print(password, "is your password and your score is", score, "its in the", strength, "category")
