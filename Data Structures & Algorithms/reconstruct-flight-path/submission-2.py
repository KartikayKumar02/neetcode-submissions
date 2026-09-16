class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        if not tickets:
            return
        
        adjList = defaultdict(list)
        tickets.sort(reverse = True)
        
        for source,dest in tickets:
            adjList[source].append(dest)
        
        result = []
        # tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
        # sorted : [["JFK","BUF"],["HOU","SEA"],["BUF","HOU"]]
        def dfs(node):
            while adjList[node] != []:
                # will pick up the last element in the adjlist as pop takes out element from the last
                next_flight = adjList[node].pop()
                dfs(next_flight)
            result.append(node)


        dfs("JFK")
        return result[::-1]