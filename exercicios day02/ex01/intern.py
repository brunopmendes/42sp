class Intern:

    class Coffee:
        def __init__(self):
            pass

        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def __init__(self, name = 'My name? I’m nobody, an intern, I have no name.'):
        self.name = name

    def __str__(self, name):
        self.name = name
        
    def make_coffee(self):
        coffee = self.Coffee()
        return coffee

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    
if __name__ == '__main__':
    intern_no_name = Intern()
    intern_mark = Intern('Mark')
    print(intern_no_name.name)
    print(intern_mark.name)
    print(intern_mark.make_coffee())

    try:
        intern_no_name.work()
    except Exception as e:
        print(e)
