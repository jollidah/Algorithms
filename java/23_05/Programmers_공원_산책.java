import java.util.*;

class Solution {
    public int[] solution(String[] park, String[] routes) {
        boolean isWall [][] = new boolean [park.length + 2][park[0].length() + 2];
        int [] dy = new int [] {-1, 0, 1, 0};
        int [] dx = new int [] {0, 1, 0, -1};
        int sy, sx, p, tmpY, tmpX;
        sy = 0;
        sx = 0;
        tmpY = 0;
        tmpX = 0;
        StringTokenizer st;
        for (int y : new int [] {0, park.length + 1}){
            for (int x = 0; x < park[0].length() + 2; x++){
                isWall[y][x] = true;
            }   
        }
        for (int x : new int [] {0, park[0].length() + 1}){
            for (int y = 0; y < park.length + 2; y++){
                isWall[y][x] = true;
            }   
        }
        
        for (int i = 0; i < park.length; i++){
            for (int j = 0; j < park[0].length(); j++){
                if (park[i].charAt(j) == 'X'){
                    isWall[i + 1][j + 1] = true;
                } else {
                    isWall[i + 1][j + 1] = false;
                    if (park[i].charAt(j) == 'S'){
                        sy = i + 1;
                        sx = j + 1;
                    }
                }
            }   
        }
        for (String m : routes){
            st = new StringTokenizer(m);
            p = switch (st.nextToken()){
                case "N" -> 0;
                case "E" -> 1;
                case "S" -> 2;
                default -> 3;
            };
            tmpY = sy;
            tmpX = sx;
            int n = Integer.parseInt(st.nextToken());
            boolean meetWall = false;
            for (int i = 0; i < n; i++){
                tmpY += dy[p];
                tmpX += dx[p];
                if (isWall[tmpY][tmpX]){
                    meetWall = true;
                    break;
                }
            }
            if (!meetWall){
                sy = tmpY;
                sx = tmpX;
            }
        }
        return new int [] {sy - 1, sx - 1};
    }
}r
