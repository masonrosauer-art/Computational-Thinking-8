introvert_points = 0
extrovert_points = 0


answer = input("on the weekend are you A) chill at your home all day, or B) chill out side on a sunny day ")
if answer == "A":
	extrovert_points += 1
elif answer == "B":
	introvert_points += 1


answer = input("Are you A rather hangout with friends, or B and play video games? ")
if answer == "A":
	extrovert_points += 1
elif answer == "B":
	introvert_points += 1


answer = input("A, Would you rather disappear by yourself to anywhere you want, or B stay with friends but in the place you are? ")
if answer == "A":
	introvert_points += 1
elif answer == "B":
	extrovert_points += 1


answer = input("Are you A. Do you feel most energized in a social setting, or B. by yourself and one on one ")
if answer == "A":
	extrovert_points += 1
elif answer == "B":
	introvert_points += 1


answer = input(" 'A' Do you find social media important, or 'B' do you find social media not important? ")
if answer == "A":
	introvert_points += 1
elif answer == "B":
	extrovert_points += 1

if introvert_points>2:
	print("you are a introvert")
elif extrovert_points>2:
	print ("you are a extrovert")