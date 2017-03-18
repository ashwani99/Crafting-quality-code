def is_palindrome(s):
    """ (str) --> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    """

    # s[i] and s[j] are the next pair of characters to compare
    i = 0
    j = len(s) - 1

    # Loop until middle of the string is reached
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    # At this point all the character in the left side and the right side matched.
    return True

