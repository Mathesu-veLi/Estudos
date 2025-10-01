package rounding;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class RoudingApp2 {
    public static void main(String[] args) {
        BigDecimal d = BigDecimal.valueOf(10.43);
        d = d.setScale(1, RoundingMode.DOWN);

        System.out.println(d);
    }
}
