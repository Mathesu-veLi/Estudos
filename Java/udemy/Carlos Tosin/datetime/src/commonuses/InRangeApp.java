package commonuses;

import java.time.LocalDate;
import java.time.LocalTime;
import java.time.OffsetDateTime;
import java.time.ZoneOffset;

public class InRangeApp {
    public static void main(String[] args) {
        var start = LocalDate.of(2020, 1, 1).atStartOfDay().atOffset(ZoneOffset.UTC);
        System.out.println(start);

        var end = LocalDate.of(2030, 12, 31).atTime(LocalTime.MAX).atOffset(ZoneOffset.UTC);
        System.out.println(end);

        var now = OffsetDateTime.now();
        System.out.println(inRange(now, start, end));
    }

    private static boolean inRange(OffsetDateTime odt, OffsetDateTime start, OffsetDateTime end) {
        return odt.isEqual(start) || odt.isEqual(end) || odt.isAfter(start) && odt.isBefore(end);
    }
}
