from cat_constructor import Cat

# def __init__(self, breed="", colour="", hunger_bar="full", tiredness="awake", age=0, eye_colour = 'green'

toby = Cat('toby', colour="Brown", age=7, breed="British Shorthair" )

print(toby.meow())
print(toby.sleep())

print('name:', toby.name)
print('breed:', toby.breed)

print('///////////')
print(toby.hunger_bar)


print(toby.eat())
toby.hunger_bar = "not full"
print(toby.eat())

print(toby.weight)
print(toby.yawn())
print(toby.get_age())