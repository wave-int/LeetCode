class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = set()
        length = len(s)
        variants = []
        var = [0,0,0,0]

        for pos0 in range(1,4):
            var[0] = pos0
            for pos1 in range(1,4):
                var[1] = pos1
                for pos2 in range(1,4):
                    var[2] = pos2
                    for pos3 in range(1,4):
                        var[3] = pos3
                        if sum(var) == length:
                            variants.append(var[::]) 

        for var in variants:
            part0 = s[0 : var[0]]
            part1 = s[var[0] : var[0] + var[1]]
            part2 = s[var[0] + var[1] : var[0] + var[1] + var[2]]
            part3 = s[var[0] + var[1] + var[2] : var[0] + var[1] + var[2] + var[3]]
            parts = [part0, part1, part2, part3]
            
            for part in parts:
                if len(part) != 1:
                    if part[0] == '0':
                        break
                if int(part) > 255:
                    break
            else:
                result.add(part0 + '.' + part1 + '.' + part2 + '.' + part3)

        return list(result)
