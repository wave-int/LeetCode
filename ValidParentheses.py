class Solution(object):
    def isValid(self, s):
        valid = "(){}[]0"
        o1 = o2 = o3 = False
        c1 = c2 = c3 = False
        l = []
        for i in range (len(s)):
            for v in range(7):
                if (s[i] == valid[v]):
                    break
            if (v == 6):
                return False
            if (s[i] == "("):
                o1 = True
                l.append("(")
            if (s[i] == "{"):
                o2 = True 
                l.append("{")
            if (s[i] == "["):
                o3 = True 
                l.append("[")
            if (s[i] == ")"):
                if (not l):
                    return False
                c1 = True   
                if (o1 != True):
                    return False
                else:
                    if (l[-1] == "("):
                        l.pop() 
                    else:
                        return False
            if (s[i] == "}"):
                if (not l):
                    return False
                c2 = True 
                if (o2 != True):
                    return False
                else:
                    if (l[-1] == "{"):
                        l.pop() 
                    else:
                        return False
            if (s[i] == "]"):
                if (not l):
                    return False
                c3 = True 
                if (o3 != True):
                    return False
                else:
                    if (l[-1] == "["):
                        l.pop() 
                    else:
                        return False
        if (not l):
            return True
        return False