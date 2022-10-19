class MyQueue {
public:
    stack<int> pus_stack;
    stack<int> pul_stack;
    MyQueue() {
        
    }
    
    void push(int x) {
        pus_stack.push(x);
        
    }
    
    int pop() {
        if(pul_stack.empty())
        {
            while(!pus_stack.empty())
            {
            pul_stack.push(pus_stack.top());
            pus_stack.pop();
            }
            
        }
        int x = pul_stack.top();
        pul_stack.pop();
        return x;
        
            
        
        
        
    }
    
    int peek() {
        if(pul_stack.empty())
        {
            while(!pus_stack.empty())
            {
            pul_stack.push(pus_stack.top());
            pus_stack.pop();
            }
            
        }
        return pul_stack.top();
        
    }
    
    bool empty() {
       if(pul_stack.empty() && pus_stack.empty())
           return true;
        else
            return false;
        
        
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
