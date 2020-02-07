"""
22. Utwórz fukcję, która jako argument będzie przyjmować listę liczb 
zmiennoprzecinkowych, a jej wynikiem będzie mediana (skorzystaj z metody sort 
działającej na standardowych listach)
"""


lst = [] 


def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0


median([4,2.5,3,1])