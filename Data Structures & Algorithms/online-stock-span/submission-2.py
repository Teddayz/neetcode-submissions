# from collections import deque
class StockSpanner:

    def __init__(self):
        self.hashMap = {}
        self.deque = deque()
        self.index = 0

    def next(self, price: int) -> int:
        span = 1
        if len(self.deque) == 0:
            self.hashMap[self.index] = price
            self.deque.append(self.index)
            self.index += 1
            return span
        while self.deque and self.hashMap.get(self.deque[-1]) <= price:
            top_number_index = self.deque.pop()
        
        if self.deque:
            span = self.index - self.deque[-1]
        else:
            span += self.index
        self.hashMap[self.index] = price
        self.deque.append(self.index)
        self.index += 1
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)