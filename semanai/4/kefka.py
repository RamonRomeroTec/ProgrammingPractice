from collections import defaultdict

def solve(cats, edges, n, m):
    connected = defaultdict(set)
    for a, b in edges:
        connected[a].add(b)
        connected[b].add(a)

    def connected_to(v, visited):
        return connected[v] - visited

    cats = {i: cat for i, cat in enumerate(cats, 1)}

    states = {(1, cats[1])}
    visited = {1}
    count = 0
    while states:
        next_states = set()
        for s, cat_count in states:
            children = connected_to(s, visited)
            visited |= children
            if not children:
                count += 1
            for x in children:
                if cats[x]:
                    next_cat_count = cat_count + cats[x]
                else:
                    next_cat_count = 0

                if next_cat_count <= m:
                    newstate = x, next_cat_count
                    next_states.add(newstate)

        states = next_states
    return count

if __name__ == '__main__':

    [n, m] = [int(i) for i in input().strip().split()]
    cats = [int(i) for i in input().strip().split()]
    assert len(cats) == n
    edges = [tuple(int(i) for i in input().strip().split()) for _ in range(n-1)]
    result = solve(cats, edges, n, m)
    print(result)
