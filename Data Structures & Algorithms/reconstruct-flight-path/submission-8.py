from collections import defaultdict, deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        res = [] 
        for u, v in tickets:
            adjList[u].append(v)
        for dest in adjList.values():
            dest.sort(reverse=True)
        
        def visit(airport):
            while adjList[airport]:
                destination = adjList[airport].pop()
                visit(destination)
            res.append(airport)
        visit("JFK")
        
        return res[::-1]