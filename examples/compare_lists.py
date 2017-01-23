# compare two lists, to test equivalency

def lists_equal(l1,l2):
    if not l1 and not l2:
        return True
    if len(l1) != len(l2):
        return False
    for i,li in enumerate(l1):
        if not (l2[i] == li):
            return False
    return True