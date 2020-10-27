# python program to illustrate functions
# treated as objects
def shout(text):
    return text.upper()

print(shout('Hi my name is Maddie'))

#assigning function to a variable
yell = shout

print(yell('Hi my name is Maddie'))
