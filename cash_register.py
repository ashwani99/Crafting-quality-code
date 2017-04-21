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
            self.toonies -= count
        elif denomination == 'tens':
            self.toonies -= count
        elif denomination == 'twenties':
            self.toonies -= count


if __name__ == '__main__':
    # A cash register for 5 loonies, 5 toonies, 5 fives, 5 tens and 5 twenties,
    # for a cash total of $190

    register = CashRegister(5, 5, 5, 5, 5)
    print(register.get_total())

    # register.add(3, 'toonies')
    # register.remove(2, 'twenties')
    #
    # print(register.get_total())
