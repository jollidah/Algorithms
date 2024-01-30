from collections import deque 
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__main_queue=deque()
        self.__sub_queue=deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.__main_queue.append(x) # Push to back .
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        ret=None
        while len(self.__main_queue)>1:
            temp=self.__main_queue.popleft() # Peek/pop from front . 
            self.__sub_queue.append(temp) # Move main_queue to sub_queue
        
        if len(self.__main_queue) == 1:
            ret=self.__main_queue.popleft()
            self.__main_queue,self.__sub_queue=self.__sub_queue,self.__main_queue # Swap main_queue,sub_queue
        
        return ret
        
    

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.__main_queue[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if self.__main_queue else True