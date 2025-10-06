import java.time.Instant;
import java.time.OffsetDateTime;
import java.time.ZoneOffset;

public class InstantApp {
    public static void main(String[] args) {
        //Instant i1 = Instant.EPOCH;

        OffsetDateTime odt = OffsetDateTime.of(2050, 12, 31, 0, 0, 0, 0, ZoneOffset.of("+00:00"));
        Instant i1 = odt.toInstant();
        System.out.println(i1);
        System.out.println(i1.toEpochMilli());
        System.out.println(i1.getEpochSecond());

        OffsetDateTime odt2 = OffsetDateTime.ofInstant(i1, ZoneOffset.UTC);
        System.out.println(odt2);
    }
}
