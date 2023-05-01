class Solution {
    public int[] solution(String[] wallpaper) {
        int minY = 100;
        int maxY = -1;
        int minX = 100;
        int maxX = -1;
        for (int y = 0; y < wallpaper.length; y++){
            for (int x = 0; x < wallpaper[0].length(); x++){
                if (wallpaper[y].charAt(x) == '#'){
                    minY = minY > y ? y : minY;
                    maxY = maxY < y ? y : maxY;
                    minX = minX > x ? x : minX;
                    maxX = maxX < x ? x : maxX;
                }
            }
        }
        return new int [] {minY, minX, maxY + 1, maxX + 1};
    }
}
