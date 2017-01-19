
def getFirst(a):
    return a[0]

def get_critical_points(buildings):
    result = []
    for b in buildings:
        x,y,h = b[0], b[1], b[2]
        result.append((x,h))
        result.append((y,0))
    return result

result = []
def merge(cps, l, m, r):
    h1 = 0
    h2 = 0
    i = l 
    j = m+1
    while i < m and j < r:
        if cps[i][0] < cps[j][0]:
            x1 = cps[i][0]
            h1 = cps[i][1]
            h = max(h1, h2)
            result.append((x1, h))
            i += 1
        else:
            x1 = cps[j][0]
            h2 = cps[j][1]
            h = max(h1, h2)
            result.append((x1, h))
            j += 1
    while i<= m:
        result.append(cps[i])            
    while j<= r:
        result.append(cps[j])


def getSkyline(cps):
    l = len(cps)
    mergeSort(cps, 0, l)

def mergeSort(cps, l, r):
    if l<r:
        m = (l+r)/2
        mergeSort(cps, l, m)
        mergeSort(cps, m+1, r)
        merge(cps, l, m, r)



buildings = [ (1,11,5) ]
cps = get_critical_points(buildings)
cps = sorted(cps, key=getFirst)
print cps
getSkyline(cps)