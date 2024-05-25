import heapq
from typing import List, Tuple
import sys

class Edge:
    def __init__(self, end, weight):
        self.end = end
        self.weight = weight

def dijkstra(graph: List, r: int) -> List[Tuple[int, int]]:
    """
    グラフと始点を受け取って，各ノードの番号と，最短経路上の変の重みの総和を返す
    """
    INF = 10**9

    # 初期位置以外のノードへのコストをINFで初期化
    min_length = [INF for _ in range(len(graph))]
    min_length[r] = 0 

    # 確定していないノードたち（全てのノードへの最短経路が確定するまで）
    done = [False for _ in range(len(graph))]

    # これまでにわかった最短経路を取り出すためのヒープ
    heap = []
    for i in range(len(graph)):
        # 初期化時は(0, r)が先頭になる
        heapq.heappush(heap, (min_length[i], i))

    # 直前に確定したノードとして初期位置を選択
    while len(heap) > 0:
        # 初めは確定しているノードが取り出される
        d, v = heapq.heappop(heap)
        # ノードへの最短経路が確定しているかどうか
        if done[v] == True:
            continue
        # 確定していないかつ，最短経路
        for edge in graph[v]:
            # 現在のノードへの最短経路長＋次のノードへのコスト＝次のノードの値
            if d + edge.weight < min_length[edge.end]:
                min_length[edge.end] = d + edge.weight
                heapq.heappush(heap, (d + edge.weight, edge.end))
        done[v] = True
    return min_length

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append(Edge(b-1, c))
    graph[b-1].append(Edge(a-1, c))

min_via_length = dijkstra(graph, 0)
min_length_dest = dijkstra(graph, N-1)
print(min_length_dest)
print(min_via_length)
for i in range(N):
  print(min_via_length[i] + min_length_dest[i])