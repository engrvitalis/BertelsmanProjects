def edit_distance(s, t):
    """
    This function computes the minimum number of edits needed 
    transform strings, s into t recursively.

    @param: String - s, t
    @return: Integer
    """

    
    # If s is an empty string, return length of t.
    # If t is an empty string, return length of s.
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
        # Check the equality of the last characters of s and t.
        if s[-1] != t[-1]:
            cost = 1

        d1 = edit_distance(s[:-1], t) + 1
        d2 = edit_distance(s, t[:-1]) + 1
        d3 = edit_distance(s[:-1], t[:-1]) + cost
    return min(d1, d2, d3)

def main():
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")

    try:
        print("The edit distance between {s} and {t} is {edit_distance(s, t)}")
    except Exception as e:
        print(e)
