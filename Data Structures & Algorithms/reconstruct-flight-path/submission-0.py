from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list) # {:[],:[]}

        tickets.sort(reverse = True) # descending

        for source,destination in tickets:
            graph[source].append(destination)
        
        result = []

        def dfs(node):
            while graph[node]:
                next_flight = graph[node].pop()
                dfs(next_flight)
            result.append(node)
        dfs("JFK")

        return result[::-1]


        

        