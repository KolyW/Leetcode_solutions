class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums_all = sorted(nums1 + nums2)
        return nums_all[int(len(nums_all)/2)] if len(nums_all) % 2 == 1 else (nums_all[int((len(nums_all)/2)-1)]+nums_all[int(len(nums_all)/2)])/2
    
def main():
    nums1 = []
    nums2 = [2,3]
    solution = Solution().findMedianSortedArrays(nums1=nums1, nums2=nums2)
    print(solution)
    
if __name__ == "__main__":
    main()
