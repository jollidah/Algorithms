import java.util.LinkedList;

class MinStack {
    LinkedList<Integer> stack  = new LinkedList<>();

    public MinStack() {
    }

    public void push(int val) {
        if (stack.isEmpty())
        {
            stack.push(val);
        }
        else
        {
            stack.push(Math.min(stack.get(1), val));
        }
        stack.push(val);
    }

    public void pop() {
        stack.pop();
        stack.pop();
    }

    public int top() {
        return stack.get(0);
    }


    public int getMin() {
        return stack.get(1);
    }
}


/*
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */

# https://leetcode.com/problems/min-stack/submissions/871718176/
