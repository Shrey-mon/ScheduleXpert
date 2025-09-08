class Slot_Stack:
    stack=[]
    top=-1

    def push(self, item):
        self.top+=1
        self.stack.append(item)

    def pop(self):
        if self.top==0:
            return []
        item=self.stack[self.top]
        self.stack.remove(item)
        self.top-=1
        return item

    def empty(self):
        self.stack.clear()
        self.top=-1

    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
