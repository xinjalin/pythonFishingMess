# create a Color class
class NestedClassExample:

    # constructor method
    def __init__(self):
        # object attributes
        self.name = 'Green'
        self.lg = self.LightGreen()

    def show(self):
        print("Name:", self.name)

    # create Light-green class
    class LightGreen:
        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'

        def display(self):
            print("Name:", self.name)
            print("Code:", self.code)


# create Color class object
outer = NestedClassExample()

# method calling
outer.show()

# create a LightGreen
# inner class object
g = outer.lg

# inner class method calling
g.display()
