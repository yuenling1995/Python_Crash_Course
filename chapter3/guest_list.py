names = ['Helen', 'Hannah', 'dicky']
print(names)
print("Number of guests is " + str(len(names)) + ".")

#msg to Helen
message = "Hi " + names[0] + "! Can you come to my dinner tonight?"
print(message)
#msg to Hannah
message = "Hi " + names[1] + "! Will you be free to join my dinner tonight?"
print(message)
#msg to Dicky
message = "Good morning " + names[-1].title() + "! Wanna have dinner tonight?"
print(message)

#person who cannot make the dinner
print(names[-1].title() + " can't make the dinner tonight.")
#new person
names[-1] = 'Trinae'
print(names)
#print new invite
message = "Hi " + names[-1] + "! Come to dinner with me tonight!"
print(message)

#message to inform ppl that I found a bigger table
message = "Hey people! so we have a bigger tinner table!"
print(message)
#add new ppl to different positions now
names.insert(0, 'Alex')
print(names)
names.insert(2, 'Mike')
print(names)
names.append('Nicole')
print(names)
#I'm not gonna print the new set of invite messages here.


#plan changes - only 2 ppl for the dinner table now
print("\nHey sorry guys, only 2 people are allowed to have dinner with me tonight.")
#remove guests with pop()
name_1 = names.pop(0)
print("Sorry " + name_1 + " I can't invite you to dinner tonight.")
name_2 = names.pop(3)
print("Sorry " + name_2 + " I can't have dinner with you tonight.")
name_3 = names.pop()
print("Sorry " + name_3 + " we can't have dinner tonight")
name_4 = names.pop(1)
print("Sorry " + name_4 + " let's skip dinner.")
print(name_4)


#now tell the 2 ppl left on the list - they're still invited
message = "Hi " + names[0] + "! You're still invited!"
print(message)
message = "Hi " + names[1] + "! You're still invited!"
print(message)


#use del statement to remove the last 2 ppl from the list (1 by 1)
print(names)
del names[0]
print(names)
del names[0]
print(names)





















