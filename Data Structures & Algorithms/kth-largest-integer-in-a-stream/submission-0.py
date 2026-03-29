class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numArr = sorted(nums)
        self.kth = k

    def add(self, val: int) -> int:
        self.numArr.append(val)
        self.numArr.sort()
        return self.numArr[len(self.numArr) - self.kth]

        #[1,2,3,4,5]
        #kth = 2
        #5 - 2 = 3
