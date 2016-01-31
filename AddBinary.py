class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def toInt(x):
            result = 0
            n = 0
            for i in range(len(x)-1,-1,-1):
                result += int(x[i])*pow(2,n)
                n += 1
            return result
        c = toInt(a)+toInt(b)
        
        res = ''
        while c:
            res = str(c%2)+res
            c /= 2
        if res=='': return '0'
        return res
