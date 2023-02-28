
class Stack:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def __call__(self, value = None):
        if value:
            self.data.append(value)
        else:
            return len(self.data) > 0 and self.data.pop() or None

    def __bool__(self):
        return len(self.data) > 0
    
    def top(self):
        return len(self.data) > 0 and self.data[len(self.data)-1] or None
