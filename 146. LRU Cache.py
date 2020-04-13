class LRUCache:

    def __init__(self, capacity: int):
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.dic={}
        self.capacity=capacity
        self.head.next=self.tail
        self.tail.per=self.head


    def get(self, key: int) -> int:
        if key in self.dic.keys():
            # 更新使用 把get的节点挪动到队列尾
            movenode=self.dic.get(key)
            movenode.per.next=movenode.next
            movenode.next.per=movenode.per

            pernode=self.tail.per

            pernode.next=movenode
            movenode.per=pernode
            self.tail.per=movenode
            movenode.next=self.tail


            return movenode.value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        # 存在键直接更新
        if key in  self.dic.keys():
            movenode=self.dic[key]
            movenode.value=value

            movenode.per.next=movenode.next
            movenode.next.per=movenode.per

            pernode=self.tail.per

            pernode.next=movenode
            movenode.per=pernode
            movenode.next=self.tail
            self.tail.per=movenode
            
        # 不存在
        else:
            # 需要替换
            if len(self.dic)>=self.capacity:
                delnode=self.head.next
                self.dic.pop(delnode.key) 

                self.head.next=delnode.next
                delnode.next.per=self.head                           
            # 插到队尾 
            cur=Node(key,value)
            self.dic[key]=cur
            pernode=self.tail.per

            pernode.next=cur
            cur.per=pernode
            cur.next=self.tail
            self.tail.per=cur



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class Node:

    def __init__(self,key:int,value:int):
        self.value=value
        self.key=key
        self.per=None
        self.next=None
if __name__ == "__main__":
    x=LRUCache(2)
 
    x1=["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    x2=[[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    for i in range(len(x1)):
        print("-----{}--{}---{}--".format(i,x1[i],x2[i]))
        if x1[i]=="put":
            print(x.put(x2[i][0],x2[i][1]))
        else:
            print(x.get(x2[i][0]))
