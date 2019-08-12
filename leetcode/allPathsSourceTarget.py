class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        stack = [ (0,graph[0], [0] )]
        goal = len(graph)-1
        l=[]
        
        
        
        while stack: 
            x = stack.pop()
            node_id, connections, path = x[0], x[1], x[2]
            #print('>', node_id, connections, path, '<')
           
            #print('c>',connections, path)
            if node_id == goal:
                l.append(path)
            if connections:
                for i in connections:
                    aux=path[:]
                    aux.append(i)
                    stack.append((i,graph[i],  aux))
        return l
                
        