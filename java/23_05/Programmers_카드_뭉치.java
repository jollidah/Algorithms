class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        int p1 = 0;
        int p2 = 0;
        for (String s : goal){
            if (p1 < cards1.length && cards1[p1].equals(s)){
                p1++;
            } else if (p2 < cards2.length && cards2[p2].equals(s)){
                p2++;
            } else {
                return "No";
            }
        }
        return "Yes";
    }
}
