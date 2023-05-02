class Solution {
    public int[] solution(int[] sequence, int k) {
        int left = 0;
        int right = 1000000;
        int lp = 0;
        int rp = 0;
        int s = sequence[0];
        while (rp < sequence.length){
            if (s == k){
                if (right - left > rp - lp){
                    right = rp;
                    left = lp;
                }
                s -= sequence[lp++];
            } else if (s < k){
                if (++rp < sequence.length){
                    s += sequence[rp];
                }
            } else {
                s -= sequence[lp++];
            }
        }
        return new int [] {left, right};
    }
}

# https://school.programmers.co.kr/learn/courses/30/lessons/178870
