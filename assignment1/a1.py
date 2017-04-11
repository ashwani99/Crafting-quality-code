import math

def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(0)
    0
    >>> num_buses(50)
    1
    >>> num_buses(51)
    2
    >>> num_buses(75)
    2
    """

    bus_size = 50

    # Returns ceiling of n divided by bus size
    return int(math.ceil(n / bus_size))


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([0.05])
    (0.05, 0)
    >>> stock_price_summary([-0.02])
    (0, -0.02)
    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """

    # Initialize two variables referring to total price gain and total price loss with value equal to 0
    sum_price_gain = 0
    sum_price_loss = 0

    # loop over the list price_changes and add the prices to calculate total gain or total loss
    for price in price_changes:
        if price >= 0:
            sum_price_gain += price
        else:
            sum_price_loss += price

    return sum_price_gain, sum_price_loss


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """

    # Initialize leftmost index and kth rightmost index in the list
    low = 0
    high = len(L) - k

    # Swap all first k elements with all last k elements
    while k:
        temp = L[low]
        L[low] = L[high]
        L[high] = temp

        # Increment left index low and right index high
        low += 1
        high += 1

        # After one swap, k is decremented by one
        k -= 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()