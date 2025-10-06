package commonuses;

import java.time.YearMonth;
import java.time.format.DateTimeFormatter;

public class YearMonthApp {
    public static void main(String[] args) {
        YearMonth ym1 = YearMonth.of(2000, 12);
        System.out.println(ym1);

        YearMonth ym2 = ym1.withYear(2010);
        System.out.println(ym2);

        ym2.format(DateTimeFormatter.ofPattern("MM/yyyy"));
        System.out.println(ym2);
    }
}
