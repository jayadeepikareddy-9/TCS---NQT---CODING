# Solution class to remove vowels from a string
class Solution:
    # Function to remove vowels
    def removeVowels(self, s: str) -> str:
        # Define vowel set
        vowels = set("aeiouAEIOU")
        result = []

        # Traverse characters
        for ch in s:
            # Skip vowels
            if ch not in vowels:
                # Append non-vowel
                result.append(ch)

        return ''.join(result)

# Driver code
if __name__ == "__main__":
    s = "Hello World"
    sol = Solution()
    print(sol.removeVowels(s))
