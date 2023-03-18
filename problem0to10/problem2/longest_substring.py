class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        count = 1
        best_count = 1 if len(s) > 0 else 0
        while i < len(s)-1:
            '''
            2 Constraints:
            1. len(set(s[i-count+1:i+1])) == count ------> ensure that the segmented list excluding any repeating element
            2. s[i+1] not in s[i-count+1:i+1] ------> ensure that the next element is not within the previous segmented list
            '''
            count = count + 1 if (len(set(s[i-count+1:i+1])) == count) and (s[i+1] not in s[i-count+1:i+1]) else count
            best_count = count if count >= best_count else best_count
            i += 1
        return best_count
    
    
def main():
    a = 'dvdf'
    b = 'abcabcbb'
    c = "bbbbb"
    d = "pwwkew"
    keys = [a,b,c,d]
    items = [Solution().lengthOfLongestSubstring(i) for i in keys]
    
    solution_dict = dict(zip(keys, items))
    print(solution_dict)
    
if __name__ == '__main__':
    main()