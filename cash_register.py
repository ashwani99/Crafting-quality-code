class CashRegister:
    """ A cash register. """

    def __init__(self, loonies, toonies, fives, tens, twenties):
        """ (CashRegister, int, int, int, int, int) -> NoneType
        
        A cash register with loonies, toonies, fives, tens and twenties.
        
        >>> register = CashRegister(5, 5, 5, 5, 5)
        >>> register.loonies
        5
        >>> register.toonies
        5
        >>> register.foonies
        5
        >>> register.tens
        5
        >>> register.twenties
        5
        """

        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def __str__(self):
        """ (CashRegister) -> str
        
        String representation of the CashRegister.
        
        >>> reg1 = (1, 2, 3, 4, 5)
        >>> reg1.__str__()
        CashRegister: $160 ($1x1, $2x2, $5x3, $10x4, $20x5)
        """

        return "CashRegister: ${0} ($1x{1}, $2x{2}, $5x{3}, $10x{4}, $20x{5})".format(self.get_total(),
                                                                                      self.loonies, self.toonies, self.fives, self.tens, self.twenties)

    def __eq__(self, other):
        """ (CashRegister, CashRegister) -> bool
        
        Returns True iff total value of money in both cash registers are the same.
            
        >>> reg1 = CashRegister(2, 0, 0, 0, 0)
        >>> reg2 = CashRegister(0, 2, 0, 0, 0)
        >>> reg1==reg2
        True
        """

        return self.get_total() == other.get_total()

    def get_total(self):
        """
        CashRegister -> int
        
        Return the total amount in the cash register.
        
        >>> register = CashRegister(5, 5, 5, 5, 5)
        >>> register.get_total()
        190
        """

        return self.loonies + self.toonies * 2 + self.fives * 5 + \
               self.tens * 10 + self.twenties * 20

    def add(self, count, denomination):
        """
        (CashRegister, int, str) -> NoneType
        
        Add the count of the denomination to the register. Denomination is one of the 'loonies', 'toonies', \
        fives, tens and 'twenties'.
        >>> register  = CashRegister(5, 5, 5, 5, 5)
        >>> register.add(2, 'toonies')
        >>> register.toonies
        7
        >>> register.add(1, 'tens')
        >>> register.tens
        6
        """

        if denomination == 'loonies':
            self.loonies += count
        elif denomination == 'toonies':
            self.toonies += count
        elif denomination == 'fives':
            self.toonies += count
        elif denomination == 'tens':
            self.toonies += count
        elif denomination == 'twenties':
            self.toonies += count

    def remove(self, count, denomination):
        """
        (CashRegister, int, str) -> NoneType

        Add the count of the denomination to the register. Denomination is one of the 'loonies', 'toonies', \
        fives, tens and 'twenties'.
        >>> register  = CashRegister(5, 5, 5, 5, 5)
        >>> register.remove(2, 'toonies')
        >>> register.toonies
        3
        >>> register.add(1, 'tens')
        >>> register.tens
        4
        """

        if denomination == 'loonies':
            self.loonies -= count
        elif denomination == 'toonies':
            self.toonies -= count
        elif denomination == 'fives':
            self.fives -= count
        elif denomination == 'tens':
            self.tens -= count
        elif denomination == 'twenties':
            self.twenties -= count


if __name__ == '__main__':
    cr1 = CashRegister(2, 0, 0, 0, 0)
    cr2 = CashRegister(0, 1, 0, 0, 0)
    cr3 = CashRegister(1, 1, 0, 0, 0)
    print(cr1)
    print(cr2)
    print(cr3)

    print(cr1 == cr2)
    print(cr3 == cr2)
