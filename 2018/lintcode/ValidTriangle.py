#TEOREMA DEL TRIANGULO
# EL LADO RESTANTE DEBE DE SER MENOR QUE LA SUMA DE LOS " OTROS LADOS"







class Solution:
    """
    @param a: a integer represent the length of one edge
    @param b: a integer represent the length of one edge
    @param c: a integer represent the length of one edge
    @return: whether three edges can form a triangle

    """
    def isValidTriangle(self, a, b, c):
        if a+b>c and a+c>b and c+b>a:
            return True
        else:
            return False
        # write your code here
