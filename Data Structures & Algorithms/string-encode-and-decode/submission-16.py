class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            n = len(s)
            parts.append(str(n))
            parts.append(";")
            parts.append(s)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        num = 0
        number_str = ""
        output = []
        index = 0
        while index < len(s):
            if s[index] == ";":
                num = int(number_str)
                index += 1
                output.append(s[index:index + num])
                number_str = ""
                index += num
            else:   
                number_str += s[index]
                index += 1
        return output

            

        