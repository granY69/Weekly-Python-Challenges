"""
In this exercise you will have to:

Take a list of names.
Add "Hello" to every name.
Make one big string with all greetings.
The solution should be one string with a comma in between every "Hello (Name)".
"""

def greetingPeopleList(people : list) -> str:
    temp = ""
    for i in range(len(people)):
        if temp != "":
            temp += ", "
        temp += "Hello " + people[i]
    return temp

print(greetingPeopleList(['Seemab Yamin', "Joe Biden", "Nocon Man", "De Culprist"]))