class WordplayStr(str):
    """A string that can report whether it has some interesting properties."""

    def name_start_and_end(self):
        """ (WordplayStr) -> bool
        
        Return whether self starts and ends with the same letter.
        
        >>> s = WordplayStr('abracadabra')
        >>> s.name_start_and_end()
        True
        >>> s = WordplayStr('cance')
        >>> s.name_start_and_end()
        False
        """

        return self[0] == self[-1]

if __name__ ==  '__main__':
    import doctest
    doctest.testmod()
