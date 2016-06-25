
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    candidate = {}
    for i,a in enumerate(nums):
    	b = target-a
    	if b in candidate:
    		return [i, candidate[b]]
    	candidate[a] = i

if __name__ == "__main__":
	nums = [3, 2, 4]
	target = 6
	twoSum(nums, target)