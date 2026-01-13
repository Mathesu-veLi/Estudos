package staticnested;

public class ExMemory {
    public static void main(String[] args) {
        Memory m = new Memory();
        Memory.Stats stats = m.stats();
        System.out.println(stats);
    }
}
