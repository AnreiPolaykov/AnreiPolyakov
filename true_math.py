def divide(first, second):
    div = 0
    if second == 0:
        from math import inf
        return inf
    elif second !=0:
        div += first/second
    return div


