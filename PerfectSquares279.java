public class PerfectSquares279 {
    public int numSquares(int n) {
    int max = (int) Math.sqrt(n);
    int[] minSquares = new int[n+1];
    Arrays.fill(minSquares, Integer.MAX_VALUE);
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= max; j++) {
            if(i == j * j) {
                minSquares[i] = 1;
            }
            else if(i > j * j) {
                minSquares[i] = Math.min(minSquares[i], minSquares[i-j*j] + 1);
            }
        }
    }
    return minSquares[n];
    }
}