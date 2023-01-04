import java.util.Stack;

class Solution {

    public int doOper(int a, int b, String s)
    {
        if (s.equals("+"))
        {
            return b + a;
        }
        else if(s.equals("-"))
        {
            return b - a;
        }
        else if(s.equals("*"))
        {
            return b * a;
        }
        else
        {
            return b / a;
        }
    }
    public int evalRPN(String[] tokens) {
        if (tokens.length == 1)
        {
            return Integer.parseInt(tokens[0]);
        }
        Stack <Integer> stack = new Stack<Integer>();
        String operands = "+-*/";
        int tmp = 0;
        int ptr = -1;
        while (ptr < tokens.length - 1 & !operands.contains(tokens[++ptr]))
        {
            stack.push(Integer.parseInt(tokens[ptr]));
        }
        System.out.println(stack.peek());
        tmp = doOper(stack.pop(), stack.pop(), tokens[ptr]);
        stack.push(tmp);
        System.out.println(tmp);
        while (ptr < tokens.length - 1)
        {
            ptr++;
            if (!operands.contains(tokens[ptr]))
            {
                stack.push(Integer.parseInt(tokens[ptr]));
            }
            else
            {
                tmp = doOper(stack.pop(), stack.pop(), tokens[ptr]);
                stack.push(tmp);
            }
            System.out.println(tmp);
        }
        return tmp;
    }
}

# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
