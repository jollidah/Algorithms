class Solution {
  public String fractionToDecimal(int numerator, int denominator) {
    StringBuilder result = new StringBuilder();
    if ((numerator > 0 && denominator < 0) || (numerator < 0 && denominator > 0)) {
      result.append("-");
    }
    long numeratorLong = Math.abs((long) numerator);
    long denominatorLong = Math.abs((long) denominator);
    result.append(numeratorLong / denominatorLong);
    long remainder = numeratorLong % denominatorLong;
    if (remainder == 0) {
      return result.toString();
    }
    result.append(".");
    Map<Long, Integer> map = new HashMap<>();
    while (remainder != 0) {
      if (!map.containsKey(remainder)) {
        map.put(remainder, result.length());
      } else {
        result.insert(map.get(remainder), "(");
        result.append(")");
        return result.toString();
      }
      remainder *= 10;
      result.append(remainder / denominatorLong);
      remainder %= denominatorLong;
    }
    return result.toString();
  }
}

// https://leetcode.com/problems/fraction-to-recurring-decimal/description/
