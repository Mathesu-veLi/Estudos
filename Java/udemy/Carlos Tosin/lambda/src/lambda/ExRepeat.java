package lambda;

public class ExRepeat {
    public static void main(String[] args) {
        repeat(5, i -> System.out.println("Number:  " + i));
    }

    private static void repeat(int n, RepeatCode code) {
        for(int i = 0; i < n; i++) {
            code.repeat(i);
        }
    }

    @FunctionalInterface
    interface RepeatCode {
        void repeat(int index);
    }
}
