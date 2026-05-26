class Solution:

    def encode(self, strs: List[str]) -> str:
        str1=""
        for i in strs:
            str1=str1+str(len(i))+"#"+i
        return str1

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            # Step 1: Find the separator '#'
            j = i
            while s[j] != '#':
                j += 1

            # Step 2: Extract length
            length = int(s[i:j])

            # Step 3: Move pointer after '#'
            j += 1

            # Step 4: Extract the string of given length
            word = s[j:j + length]

            # Step 5: Store result
            result.append(word)

            # Step 6: Move pointer to next encoded string
            i = j + length

        return result
