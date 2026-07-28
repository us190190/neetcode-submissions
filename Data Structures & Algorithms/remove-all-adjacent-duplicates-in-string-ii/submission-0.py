class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        # deeedbbcccbdaa
        # ddbbbdaa


        result = ""
        length = len(s)
        i=0

        while i<length:

            if (i+k)<length and s[i:i+k]=="".join(s[i]*k):
                i += k
            else:
                len_result = len(result)
                if len_result>=(k-1) and result[len_result-(k-1):]=="".join(s[i]*(k-1)):
                    result = result[:len_result-k+1]
                else:
                    result += s[i]
                i += 1
        
        return result


        