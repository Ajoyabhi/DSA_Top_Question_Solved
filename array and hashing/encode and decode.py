"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
"""

class Codec:
    def encode(self, strs:list[str]) -> str:
        # Encode each string as length + '#' + string
        # Example: ["neet","code"] -> "4#neet4#code"
        result =""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s:str)-> list[str]:
        result = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j += 1
            # Get the length of next string
            lenght = int(s[i:j])
            # Extract the string and add to result
            string = s[j+1: j+1+lenght]
            result.append(string)
            i = j+1+lenght
        return result

codex = Codec()
strs1 = ["neet","code","love","you"]
encoded1 = codex.encode(strs1)
print(codex.decode(encoded1))  

# Test case 2
strs2 = ["we","say",":","yes"]
encoded2 = codex.encode(strs2)
print(codex.decode(encoded2))   
