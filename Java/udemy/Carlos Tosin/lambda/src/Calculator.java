public class Calculator {
    private int mult;

    int calculate(int x, int y) {
        mult = 1;
        Operation operation = (n1, n2) -> (n1 + n2) * mult;
        mult = 2;
        return operation.calculate(x, y);
    }
}
