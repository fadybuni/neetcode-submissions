class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bfs(curr, left):
            if len(left) == 0:
                res.append(curr[:])
                
            else:
                for i in list(left):
                    curr.append(i)
                    left.remove(i)
                    bfs(curr,left)
                    curr.pop()
                    left.append(i)
        bfs([],nums[:])
        return res

