import sys

arg_list = sys.argv
arg = arg_list[1]


states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}

capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

def return_capitals():
    if len(arg_list) != 2:
        sys.exit()
    elif arg in states:
        print(capital_cities[states[arg]])
    else:
        print("Unknown state")

if __name__ == '__main__':
    return_capitals()