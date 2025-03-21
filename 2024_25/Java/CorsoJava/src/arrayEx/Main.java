package arrayEx;

public class Main {
    public static void main(String[] args) {

        /**
         * Simple operation using array
         */
        int[] numbers = {2, -9, 0, 5, 12, -25, 22, 9, 8, 12};

        int[] ops;
        ops = new int[numbers.length+1];

        for (int i = 0; i < 11; i++){
            ops[i] = 2*i;
            System.out.println(ops[i]);
        }

        int sum = 0;
        double average;

        // access all elements using for each loop
        // add each element in sum
        for (int number : numbers) {
            sum += number;
        }

        // get the total number of elements
        int arrayLength = numbers.length;

        // calculate the average
        // convert the average from int to double
        average = ((double) sum / (double) arrayLength);

        System.out.println("Sum = " + sum);
        System.out.println("Average = " + average);


        Calculator calc = new Calculator();
        System.out.println(calc.getValues().length);
        System.out.println(calc.getValues()[0]);
    }
}
