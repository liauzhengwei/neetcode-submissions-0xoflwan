class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat array like linked list
        # each index points to another index

        # Find the intersection where they meet inside the cycle
        # Find the cycle entrance

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

