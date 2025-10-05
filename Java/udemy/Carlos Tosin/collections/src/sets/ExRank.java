package sets;

public class ExRank {
    public static void main(String[] args) {
        Rank rank = new Rank();


        rank.addPlayer("player1", 100);
        rank.addPlayer("player2", 200);
        rank.addPlayer("player3", 300);

        rank.printRanking();
    }
}
