class Graph:
    # initialize the graph with the adjacent list
    def __init__(self, adj):
        self.adj = adj

    # to get neighbours, get the list at the idex of node
    def getn(self, v):
        return self.adj[v]
    
    # huristic function , having equal values at each node
    def h(self, n):
        H = {
            'A' : 1,
            'B' : 1,
            'C' : 1,
            'D' : 1
        }
        return H[n]

    # openlist = node visited, neighbours not inspected
    # closedlist = nodes visited and neighbours inspected
    def astar(self, start, stop):
        openlist = set([start])
        closedlist = set([])
        # poo dic will have dis from start to all other nodes
        poo = {}
        poo[start] = 0
        # par = adjc mapping of all nodes
        par = {}
        par[start] =start

        while len(openlist)>0:
            n = None
            # find the node with lowest value of f()
            for v in openlist:
                if n == None or poo[v]+self.h(v) < poo[n]+self.h(n):
                    n=v

            if n == None :
                print('Path does not exits!!')
                return None
            
            # if cur node is stop
            # then we start again from start
            # this is final , after the path is constructed
            if n == stop:
                reconst_path = []

                while par[n]!=n:
                    reconst_path.append(n)
                    n=par[n]

                reconst_path.append(start)
                reconst_path.reverse()

                print('path found ',reconst_path)
                return reconst_path
            
            # for all neighbours of the current node
            for (m, weight) in self.getn(n):
                # if current node is not present in both the open and closed list
                # add it to openlist and note n as its parameter
                if m not in openlist and m not in closedlist:
                    openlist.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight

                # otherwise, check if it quicker to first visit n then m
                # and if it is, update par and poo data
                    # and if the node was in the closed list , move it to open list
                else:
                    if poo[m]>poo[n]+weight:
                        poo[m] = poo[n] +weight
                        par[m] = n

                        if m in closedlist:
                            closedlist.remove(m)
                            openlist.add(m)

            #remove n from openlist and add it to the closed list
            # because all of its neighbours are inspected
            openlist.remove(n)
            closedlist.add(m)
        
        print('path does not exits')
        return  None
    
adj={
    'A': [('B',1),('C',3),('D',7)],
    'B':[('D',5)],
    'C':[('D',12)]
}
Graph1 = Graph(adj)
Graph1.astar('A','D')