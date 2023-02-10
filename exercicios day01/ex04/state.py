import sys

arg_list = sys.argv

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

def teste():

    if len(arg_list) != 2:
        sys.exit()
    elif arg_list[1] in capital_cities.values():            
        for k, v in capital_cities.items():
            if arg_list[1] == v:
                for x, y in states.items():
                    if k == y:
                        print(x)
                        break 
    else:
        print('Unknown state') 

if __name__ == '__main__':
    teste()