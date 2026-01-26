package api;

import java.util.Optional;

public class AppOptional7 {
    public static void main(String[] args) {
        String s1 = Optional.of("A").orElse(get());
        System.out.println(s1);

        /*String s2 = Optional.of("A").orElseGet(AppOptional7::get);
        System.out.println(s2);*/
    }

    private static String get() {
        System.out.println("Calling get()...");
        try {
            Thread.sleep(3000);
        } catch(InterruptedException e) {
            throw new RuntimeException(e);
        }
        return "B";
    }
}
