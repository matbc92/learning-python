class Logic_Gate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class Binary_Gate(Logic_Gate):

    def __init__(self, n):
        super().__init__(n)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return int(input("Enter Pin A input for gate {} -->".format(self.get_label())))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return int(input("Enter Pin B input for gate {} -->".format(self.get_label())))
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self,source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

class Unary_Gate(Logic_Gate):
    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate {} -->".format(self.get_label())))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class And_Gate(Binary_Gate):

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a==1 and b==1:
            return 1
        else:
            return 0

class Or_Gate(Binary_Gate):

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a==1 or b==1:
            return 1
        else:
            return 0

class Nand_Gate(And_Gate):

    def perform_gate_logic(self):
        if super().perform_gate_logic()==1:
            return 0
        else:
            return 1

class Nor_Gate(Or_Gate):

    def perform_gate_logic(self):
        if super().perform_gate_logic()==1:
            return 0
        else:
            return 1

class Not_Gate(Unary_Gate):

    def perform_gate_logic(self):

        a = self.get_pin()
        if a==1:
            return 0
        else:
            return 1

class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.fromgate

    def get_to(self):
        return self.togate
def main():
    g1 = And_Gate("G1")
    #print("And gate result = {}".format(g1.get_output()))
    g2 = And_Gate("G2")
    #print("And gate result = {}".format(g2.get_output()))
    g3 = Or_Gate("G3")
    #print("Or gate result = {}".format(g3.get_output()))
    g4 = Not_Gate("G4")
    #print("Not gate result = {}".format(g4.get_output()))
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())
main()
