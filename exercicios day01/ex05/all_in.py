import sys

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

args_lis = sys.argv

def all_in():
    if len(args_lis) != 2:
        sys.exit() 

    args = args_lis[1].split(',')

    for arg in args:
        arg = arg.strip().capitalize()

        if arg in capital_cities.values() or arg in states.keys():
            for k, v in capital_cities.items():
                if arg == v:
                    for x, y in states.items():
                        if k == y:
                            print(arg, "is the capital of", x)

            for k, v in states.items():
                if arg == k:
                    for x, y in capital_cities.items():
                        if v == x:
                            print(arg, "is a state of", y)
        else:
            print(arg, "is neither a capital city nor a state")

if __name__ == '__main__':
    all_in()

                