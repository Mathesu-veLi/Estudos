package rounding;

public class RoundingApp1 {
    public static void main(String[] args) {
        double d = 10.5;

        long v = Math.round(d);
        System.out.println(v);

        double f = (long) Math.floor(d);
        System.out.println(f);

        double c = (long) Math.ceil(d);
        System.out.println(c);
    }
}
