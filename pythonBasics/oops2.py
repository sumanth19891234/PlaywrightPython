class calculato:

    def __init__(self):
        print("i am insode constructor")

    def __init_subclass__(cls, **kwargs):
        print("indide subnclass")

calculato()