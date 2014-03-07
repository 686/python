class test_inner():
    def __init__(self, inner):
        self.inner = inner

class test_outter():
    def __init__(self):
        self.inner_list = []

    def create_inner(self, inner):
        t_inner = test_inner(inner)
        self.inner_list.append(t_inner.inner)
        return t_inner

    def print_inner(self):
        for t_inner in self.inner_list:
            print t_inner


t_outter = test_outter()
inner_1 = t_outter.create_inner(1)
inner_2 = t_outter.create_inner(2)
inner_3 = t_outter.create_inner(3)
inner_4 = t_outter.create_inner(4)
inner_4.inner = 1

t_outter.print_inner()