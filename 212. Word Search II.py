from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tire={}
        for word in words:
            p=tire
            for char in word:
                if char in p.keys():
                    p=p[char]
                else:
                    p[char]={}
                    p=p[char]
            p['$']=word
        m=len(board)
        n=len(board[0])
        res=[]
        def search(row,col,node):
            parent=node
            char=board[row][col]
            node=node[char]
            if '$' in node.keys():
                res.append(node['$'])
            board[row][col]='#'
            for a,b in [(-1,0),(1,0),(0,1),(0,-1)]:
                newrow=row+a
                newcol=col+b
                if newrow<0 or newrow>= m or newcol<0 or newcol>=n:
                    continue
                if board[newrow][newcol] not in node.keys():
                    continue
                search(newrow,newcol,node)
            board[row][col]=char
            if not node:
                parent.pop(char)

        for i in range(m):
            for j in range(n):
                if board[i][j] in tire.keys():
                    search(i,j,tire)
        return res


if __name__ == "__main__":
    x=Solution()
    res=x.findWords([["a","a"]],
["a"])
    print(res)