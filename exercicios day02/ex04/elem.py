#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    r_count = 0

    class ValidationError(Exception):
        def __init__(self):
            super().__init__("incorrect behaviour.")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.content = content
        self.tag_type = tag_type

        if content is None:
            self.content = []
        elif not Elem.check_type(content):
            raise Elem.ValidationError
        else:
            if hasattr(content, '__iter__'):
                self.content = content
            else:
                self.content = [content]

        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """

        result = ""

        if self.tag_type == 'double':
            result += "<" + self.tag + self.__make_attr() + ">" + self.__make_content() + "</" + self.tag + ">"
        elif self.tag_type == 'simple':
            result += "<" + self.tag + self.__make_attr() + " />"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if self.content == None or len(self.content) == 0:
            return ''

        result = ''

        Elem.r_count += 1
        for elem in self.content:
            if len(str(elem)) != 0:
                result += '\n' + Elem.r_count * '  ' + str(elem)
        if len(str(elem)) != 0:
            result += '\n' + (Elem.r_count - 1) * '  '
        Elem.r_count -= 1
        return result


    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))
def test_Elem():
    _html = Elem("html")
    _head = Elem("head")
    _title = Elem("title", content=[Text("Hello ground!")])
    _body = Elem("body")
    _h1 = Elem("h1", content=[Text("Oh no, not again!")])
    _img = Elem("img", attr={"src" : "http://i.imgur.com/pfp3T.jpg"}, tag_type='simple')

    try:
        _head.add_content(_title)
        _html.add_content(_head)
        _body.add_content(_h1)
        _body.add_content(_img)
        _html.add_content(_body)
        print(_html)
    except Exception as exception:
        print(exception.args[0])

if __name__ == '__main__':
    test_Elem()