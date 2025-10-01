package bignumber;

import java.math.BigDecimal;

public class BigDecimalApp1 {
    public static void main(String[] args) {
        BigDecimal big = new BigDecimal("341351515135.10");
        big = big.multiply(BigDecimal.TEN);

        System.out.println(big);
    }
}
