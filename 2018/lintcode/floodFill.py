
def change(image, sr, sc, newColor, previous):
    image[sr][sc]=newColor
    #abajo
    if sr+1 < len(image) and sc < len(image[0]) and sr+1 >=0 and sc >=0 and image[sr+1][sc]==previous :
        image[sr+1][sc]=newColor
        change(image, sr+1, sc, newColor, previous)

    #arriba
    '''
    print( sr-1 < len(image))
    print(sc < len(image[0]))
    print(sr-1 >=0 )
    print(sc >=0)
    print(image[sr-1][sc]==previous)
    '''
    if sr-1 < len(image) and sc < len(image[0]) and sr-1 >=0 and sc >=0 and image[sr-1][sc]==previous:
        image[sr-1][sc]=newColor
        change(image, sr-1, sc, newColor, previous)


    #derecha
    if sr < len(image) and sc+1 < len(image[0]) and sr >=0 and sc+1 >=0 and image[sr][sc+1]==previous:
        image[sr][sc+1]=newColor
        change(image, sr, sc+1, newColor, previous)


    if sr < len(image) and sc-1 < len(image[0]) and sr >=0 and sc-1 >=0 and image[sr][sc-1]==previous:
        image[sr][sc-1]=newColor
        change(image, sr, sc-1, newColor, previous)




class Solution:
    """
    @param image: a 2-D array
    @param sr: an integer
    @param sc: an integer
    @param newColor: an integer
    @return: the modified image
    """
    def floodFill(self, image, sr, sc, newColor):
        change(image, sr, sc, newColor, image[sr][sc])
        return image

        # Write your code here
