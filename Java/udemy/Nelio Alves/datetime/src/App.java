import java.time.Duration;
import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;

public class App {
    public static void main(String[] args) throws Exception {
        LocalDate d04 = LocalDate.parse("2022-07-20");
        LocalDateTime d05 = LocalDateTime.parse("2022-07-20T01:30:26");
        Instant d06 = Instant.parse("2002-07-20T01:30:26Z");

        Instant pastWeekLocalDate = d06.minus(7, ChronoUnit.DAYS);
        Instant nextWeekLocalDate = d06.plus(7, ChronoUnit.DAYS);

        System.out.println("pastWeekLocalDate = " + pastWeekLocalDate);
        System.out.println("nextWeekLocalDate = " + nextWeekLocalDate);
    }
}
