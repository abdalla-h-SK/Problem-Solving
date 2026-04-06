# 3123
# AI solution ->

from collections import defaultdict
import heapq

class Solution(object):
    def findAnswer(self, n, edges):
        graph = defaultdict(list)

        # Step 1: Build adjacency list
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))  # Since it's undirected

        # Step 2: Implement Dijkstra's Algorithm
        def dijkstra(start):
            dist = {i: float('inf') for i in range(n)}
            dist[start] = 0
            pq = [(0, start)]  # Min-heap (distance, node)

            while pq:
                curr_dist, node = heapq.heappop(pq)
                
                if curr_dist > dist[node]:  # Ignore outdated distances
                    continue

                for neighbor, weight in graph[node]:
                    new_dist = curr_dist + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))

            return dist

        # Step 3: Run Dijkstra from 0 and from n-1
        distFromStart = dijkstra(0)
        distFromEnd = dijkstra(n - 1)

        # If there's no path from 0 to n-1, return all False
        if distFromStart[n - 1] == float('inf'):
            return [False] * len(edges)

        shortestPathLength = distFromStart[n - 1]  # The shortest path distance

        # Step 4: Identify valid shortest path edges
        ans = []
        for u, v, w in edges:
            if (distFromStart[u] + w + distFromEnd[v] == shortestPathLength) or \
               (distFromStart[v] + w + distFromEnd[u] == shortestPathLength):
                ans.append(True)
            else:
                ans.append(False)

        return ans