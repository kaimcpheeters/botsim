
public class Bots {

    public static class Cheater extends Bot {
        public String decide(){
            return "cheat";
        }
    }

    public static class Cooperator extends Bot {
        public String decide(){
            return "cooperate";
        }
    }

    public static class Copycat extends Bot {
        public String decide(){
            return this.memory;
        }
    }

}
