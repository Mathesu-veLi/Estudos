package sets;

import java.util.Comparator;
import java.util.Set;
import java.util.TreeSet;

public class Rank {
    private final Set<Player> players = new TreeSet<>(Comparator.comparing(Player::score).reversed());

    public void addPlayer(String name, int score) {
        players.add(new Player(name, score));
    }

    public void printRanking() {
        int pos = 1;
        for (Player p : players) {
            System.out.printf("%02d. %-10s -> %d\n", pos++, p.name(), p.score());
        }
    }
}
