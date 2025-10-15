package arrayEx;

/**
 * Calculator class
 * Provides fundamental and advanced operation:
 * sum, diff, mult, div, square, cube, log, root
 */

public class Calculator {

    private float[] values;

    public Calculator(){
        this.values = new float[10];
        this.values[0] = 0;
    }

    public float[] getValues() {
        return values;
    }

    public void setValues(float... values) {
        this.values = values;
    }
}
