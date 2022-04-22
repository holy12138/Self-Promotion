
def linear_search(li, val):
    for idx, v in enumerate(li):
        if v == val:
            return idx
    else:
        return None
    