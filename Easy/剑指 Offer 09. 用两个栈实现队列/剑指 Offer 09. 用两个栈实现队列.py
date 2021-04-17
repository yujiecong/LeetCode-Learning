class CQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def appendTail(self, value: int) -> None:
        self.stack1.append(value)
    def deleteHead(self) -> int:
        if self.stack1:
            self.stack2=self.stack1[::-1]

            pop=self.stack2.pop()
            self.stack1=self.stack2[::-1]
            #将stack2第一个弹出
            return pop
        else:
            return -1
# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()