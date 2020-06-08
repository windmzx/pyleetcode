class MedianFinder {
    PriorityQueue<Integer> left,right;
    /** initialize your data structure here. */
    public MedianFinder() {
        left=new PriorityQueue<Integer>((x,y)->(y-x));
        right=new PriorityQueue<Integer>();
    
    }
    
    public void addNum(int num) {
        left.add(num);
        right.add(left.poll());
        if(right.size()>left.size())
            left.add(right.poll());

    }
    
    public double findMedian() {
        if (left.size()>right.size()){
            return left.peek();
        }else{
            return(left.peek()+right.peek())/2.0;
        }

    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */