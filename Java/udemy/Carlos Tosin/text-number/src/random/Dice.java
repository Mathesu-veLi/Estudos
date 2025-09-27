package random;

import java.util.Random;

public class Dice {
    private final Random random = new Random();

    public Numbers roll() {
        return new Numbers(randomInt(), randomInt());
    }

    private int randomInt() {
        return random.nextInt(1, 7);
    }
}
