letter = '''Dear,<|NAME|>
Greeting from AKoN Solutions 
You are selected!
<|DATE|>
'''
name=input("Enter your name\n")
date=input("ENter the date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)