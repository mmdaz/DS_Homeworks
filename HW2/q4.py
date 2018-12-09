from itertools import chain

from collections import defaultdict


def DFS(G, v, seen=None, path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths


V = int(input())
G = defaultdict(list)

nodes = [[0 for x in range(2)] for y in range(V - 1)]

for i in range(V - 1):
    nodes[i][0], nodes[i][1] = map(str, input().split())

for (s, t) in nodes:
    G[s].append(t)
    G[t].append(s)

# for i in range(V -1):
#     inp = input()
#     v = inp.split(" ")[0]
#     u = inp.split(" ")[1]
#     G[v].append(u)
#     G[u].append(v)

res = list()

all_paths = list(chain.from_iterable(DFS(G, n) for n in set(G)))
max_len = max(len(p) for p in all_paths)

print(max_len - 1)
