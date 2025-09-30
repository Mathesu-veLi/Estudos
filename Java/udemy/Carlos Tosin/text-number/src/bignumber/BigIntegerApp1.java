package bignumber;

import java.math.BigInteger;

public class BigIntegerApp1 {
    public static void main(String[] args) {
        BigInteger big = new BigInteger("56789073148134914134081348134871134123124352135677975731");
        big = big.add(BigInteger.TEN);
        System.out.println(big);

        BigInteger big2 = BigInteger.valueOf(100);
        System.out.println(big2);
        System.out.println(big2.intValue());
    }
}