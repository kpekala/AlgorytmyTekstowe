
##
# direction = 1: na góre
# direction = -1: w lewo
# direction = 2: na ukos
def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    d = [[0 ] *( n +1) for _ in range( m +1)]
    path = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(0, m+ 1):
        d[i][0] = i
    for j in range(0, n + 1):
        d[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            tmp = d[i - 1][j] + 1
            direction = 1
            if d[i][j - 1] + 1 < tmp:
                tmp = d[i][j - 1] + 1
                direction = -1
            if d[i - 1][j - 1] + cost < tmp:
                tmp = d[i - 1][j - 1] + cost
                direction = 2
            d[i][j] = tmp
            path[i][j] = direction

    return path, d[m][n], d



def print_path(path, s1, s2, d):
    m = len(s1)
    n = len(s2)
    mp = {1: "usuwanie", -1: "wstawianie", 2: "zamiana"}
    my = {1: -1, -1: 0, 2: -1}
    mx = {1: 0, -1: -1, 2: -1}
    i = m
    j = n
    while i > 0 and j > 0:
        val = path[i][j]
        if not (val == 2 and s1[i-1] == s2[j-1]):
            #print(i,j)
            if val == -1:
                print(mp[path[i][j]], s2[j-1])
            else:
                print(mp[path[i][j]], s1[i-1])
            if path[i][j] == 2:
                print("z ",s2[j-1])
                #val = -1
        print(path[i][j], i, j)
        i += my[val]
        j += mx[val]
    if d[i][j] > 0:
        if i == 0:
            print("wstawianie", s2[0])
        else:
            print("usuwanie", s1[0])



def test_edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    path, res, d = edit_distance(s1,s2)
    print("res:",res)
    print_path(path,s1,s2, d)


test_edit_distance("kwintesencja", "quintessence")
