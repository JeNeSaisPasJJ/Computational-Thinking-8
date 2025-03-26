# Begginning: create variables
yunc_points = 0
unc_points = 0

# Middle: ask questions
answer = input( "Would you rather A) go on a nice long walk, or B) go on a nice long run?")
if answer == "A" :
    unc_points += 1
elif answer == "B" :
    yunc_points += 1


answer = input("If you JOGGED 100 yards would you be A) winded, or B) chill as hek broski?")
if answer == "A" :
    unc_points += 1
elif answer == "B" :
    yunc_points += 1


answer = input("Would you rather A) stay inside and do smth, or B) go outside and do smth like the good old days?")
if answer == "A" :
    yunc_points += 1
elif answer == "B" :
    unc_points += 1


answer = input("Would you rather play video games on A) an Atari, Nintendo or Gameboy, or B) an Xbox, Playstation or Gaming PC?")
if answer == "A" :
    unc_points += 1
elif answer == "B" :
    yunc_points += 1

answer = input("Would you rather A) scream at YN's that are on your lawn, or B) get them off the 'thuggish' way?")
if answer == "A" :
    unc_points += 1
elif answer == "B" :
    yunc_points += 1

# end of quiz: give point conclusion
if yunc_points>unc_points :
    print("You are a youthful yunc")
elif unc_points>yunc_points :
    print("You're unc ahh lmfao")