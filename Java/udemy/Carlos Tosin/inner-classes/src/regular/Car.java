package regular;

public class Car {
    private int speed;
    private Engine engine = new Engine();


    public void accelerate() {
        engine.injectFuel();
    }

    public int getSpeed() {
        return speed;
    }

    private class Engine {
        public void injectFuel() {
            speed += 10;
        }
    }
}
