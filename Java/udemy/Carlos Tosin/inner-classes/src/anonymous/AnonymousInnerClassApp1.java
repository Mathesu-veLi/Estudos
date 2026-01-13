package anonymous;

public class AnonymousInnerClassApp1 {
    public static void main(String[] args) {
        /*class HiMessage implements Message {
            @Override
            public String get() {
                return "Hi!";
            }
        }

        HiMessage message = new HiMessage();*/

        Message message = new Message() {
            @Override
            public String get() {
                return "Hi";
            }
        };

        Message message2 = new Message() {
            @Override
            public String get() {
                return "Bye";
            }
        };

        System.out.println(message.get());
        System.out.println(message2.get());
    }
}
