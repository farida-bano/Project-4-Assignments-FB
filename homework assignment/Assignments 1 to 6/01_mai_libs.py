#Mad libs Python Project
#In this Kylie Ying tutorial, you will learn how to get input from the user, work with f-strings, and see your results printed to the console.
#This is a great starter project to get comfortable doing string concatenation in Python.
# User input with validation
name = input("Enter the student name: ").title()
programming_language = input("Enter a programming language (e.g HTML, Java, TypeScript, Python): ").title()
while True:
    if programming_language.lower() in ['html', 'java', 'typescript', 'python']:
        break
    print("Note: This language might be challenging for beginners!")
    programming_language = input("Please choose from common languages: ").title()

mentor = input("Enter the mentor name: ").title()
location = input("Enter location (e.g Governor House, Tech Park): ").title()
friend_name = input("Enter a friend's name: ").title()
months = input("How many months did they study? (e.g 3, 6): ")
project_type = input("What did they build? (e.g Website, Game, App): ").title()

# Story created with enhanced flow
story = f"""
\n🚀 Here is your tech adventure story! 🚀

Once upon a time in {location}, there was a passionate student named {name}. 
{name} had always been curious about technology and decided to learn {programming_language}.

At GAIAC Academy, {name} met {mentor}, a legendary {programming_language} developer who became their mentor. 
For {months} months, {name} and {friend_name} worked tirelessly, facing bugs and errors bravely.

Their hard work paid off when they created an amazing {project_type} using {programming_language}! 
The project impressed everyone at {location} and was featured in local tech blogs.

Now {name} continues the journey, inspiring others to learn programming. 
Who knows what they'll create next... 🌟
"""

print(story)