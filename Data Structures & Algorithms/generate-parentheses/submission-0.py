class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def perm(curr, opened, closed):
            if len(curr) == n*2:
                res.append("".join(curr))
            if opened < n:
                curr.append("(")
                perm(curr, opened +1, closed)
                curr.pop()
            if opened > closed:
                curr.append(")")
                perm(curr,opened,closed+1)
                curr.pop()
        perm([],0,0)
        return res
        