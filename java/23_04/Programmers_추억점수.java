import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        HashMap <String, Integer> hm = new HashMap<>();
        for (int i = 0; i < name.length; i ++){
            hm.put(name[i], yearning[i]);
        }
        int[] answer = new int[photo.length];
        for (int i = 0; i < photo.length; i++){
            String [] p = photo[i];
            int s = 0;
            for (String str : p){
                if (hm.containsKey(str)){
                    s += hm.get(str);
                }
            }
            answer[i] = s;
        }
        return answer;
    }
}
