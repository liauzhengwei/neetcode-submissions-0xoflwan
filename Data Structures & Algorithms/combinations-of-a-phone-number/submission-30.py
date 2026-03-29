class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            '2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }

        res = []

        if not digits:
            return []

        def bt(index, current):
            if len(digits) == index:
                res.append(current[:])
                return

            digit = digits[index]
            letters = phone_map[digit]

            for letter in letters:
                bt(index + 1, current + letter)

        bt(0, "")
        return res
