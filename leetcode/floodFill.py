class Solution(object):
    def floodFill(self, image, r, c, newColor):
        from collections import deque           
        stack = deque([(r, c)])
        color = image[stack[0][0]][stack[0][1]]
        visited=set()
        while stack:
            pair = stack.popleft()
            if pair:
                if pair not in visited:
                    visited.add(pair)
                    if pair[0]-1 >= 0 and image[pair[0]-1][pair[1]] == color and (pair[0]-1, pair[1]) not in visited :
                        stack.append((pair[0]-1, pair[1]))
                    if pair[0]+1 < len(image) and image[pair[0]+1][pair[1]] == color and (pair[0]+1, pair[1]) not in visited :
                        stack.append((pair[0]+1, pair[1]))
                    if pair[1]-1 >= 0 and  image[pair[0]][pair[1]-1] == color and (pair[0], pair[1]-1) not in visited :
                        stack.append((pair[0], pair[1]-1))
                    if pair[1]+1 < len(image[0]) and image[pair[0]][pair[1]+1] == color and (pair[0], pair[1]+1) not in visited :
                        stack.append((pair[0], pair[1]+1))
        for p in visited:
            image[p[0]][p[1]]=newColor
        return image     
            

print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))         
            
            