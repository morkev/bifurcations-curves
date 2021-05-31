package logisticmap;

class LogisticMap {

    static double logistic(double y, double r) {
        return 4.0 * r * y * (1.0 - y);
    }

    // Plot the logistic map using standard draw
    public static void main(String[] args) {
        int N = 800;
        StdDraw.setXscale(0.7, 1.0);
        StdDraw.setYscale(0.0, 1.0);
        StdDraw.enableDoubleBuffering();

        for (double r = 0.7; r <= 1.0; r += 0.3/N) {

            // choose random initial value
            double y = Math.random();

            // ignore first 1000 iterates
            for (int i = 0; i < 1000; i++)
                y = logistic(y, r);

            // plot next 1000 iterates
            for (int i = 0; i < 100; i++) {
                y = logistic(y, r);
                StdDraw.point(r, y);
            }
            StdDraw.show();
            // change to 10 from 1
            StdDraw.pause(2);
        }
    }
}