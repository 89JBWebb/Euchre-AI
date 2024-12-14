class Node:
    d = None
    yes = None
    no = None

    def eval(self, input):
        if self.d(input):
            if type(self.yes) == type(self):
                return self.yes.eval()
            return self.yes
        if type(self.no) == type(self):
            return self.no.eval()
        return self.no

