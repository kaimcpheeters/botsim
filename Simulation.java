
public class Simulation {
    public static void main(String[] args){
        Bots.Cheater cheater  = new Bots.Cheater();
        Bots.Cooperator cooperator  = new Bots.Cooperator();
        Bots.Copycat copycat  = new Bots.Copycat();

        Simulator.run_game(cooperator,copycat,10);
        Simulator.run_game(cooperator,cheater,10);
        Simulator.run_game(cheater,copycat,10);

    }
}
