class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append(';')
            res.append(s)
        print(''.join(res))
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        temp = ''

        while start < len(s):
            end = start
            while s[end] != ';':
                end += 1
            length = int(s[start:end])
            start = end + 1
            temp = s[start:start+length]
            res.append(temp)
            if start+length > len(s):
                return res
            start = start + length

        return res
        


            
