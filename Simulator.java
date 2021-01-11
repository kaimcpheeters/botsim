
public class Simulator {
    final static int COOPERATION_REWARD = 2;
    final static int STEAL_REWARD = 3;
    final static int STEAL_PARTIAL_REWARD = 2;
    final static int STOLEN_PENALTY = -1;

    public static void run_round(Bot bot1,Bot bot2){
        //Takes 2 bots and subjects them to a match

        if (bot1.decide().equals("cooperate") && bot2.decide().equals("cooperate")){
            bot1.coins += COOPERATION_REWARD;
            bot2.coins += COOPERATION_REWARD;
            }
        else if (bot1.decide().equals("cheat") && bot2.decide().equals("cooperate")){
            if (bot2.coins >= STOLEN_PENALTY*-1){
                bot1.coins += STEAL_REWARD;
                bot2.coins += STOLEN_PENALTY;}
            else {
                bot1.coins += STEAL_PARTIAL_REWARD;
                }
            }
        else if (bot1.decide().equals("cooperate") && bot2.decide().equals("cheat")){
            if (bot1.coins >= STOLEN_PENALTY*-1){
                bot2.coins += STEAL_REWARD;
                bot1.coins += STOLEN_PENALTY;}
            else {
                bot2.coins += STEAL_PARTIAL_REWARD;
            }
        }
        else if (bot1.decide().equals("cheat") && bot2.decide().equals("cheat")){
            //no change in coins if both bots attempt to cheat
            }
        bot1.memory = bot2.decide();
        bot2.memory = bot1.decide();
        }
    public static void run_game(Bot bot1,Bot bot2,int rounds){
        //Takes 2 bots and subjects them to n rounds
        bot1.reset();
        bot2.reset();
        for (int i = 0; i <= rounds; i++){
            run_round(bot1,bot2);
        }
        bot1.bank+=bot1.coins;
        bot2.bank+=bot2.coins;
        report_game_results(bot1,bot2);
    }

    public static void report_game_results(Bot bot1, Bot bot2){
        //Reports winner of game after all rounds completed
        if (bot1.coins > bot2.coins) {
            System.out.println(bot1.toString()+ " wins the game against" + bot2.toString());
            }
        else if (bot1.coins < bot2.coins) {
            System.out.println(bot2.toString()+ " wins the game against" + bot1.toString());
        }
        if (bot1.coins == bot2.coins) {
            System.out.println("In the game between " + bot1.toString() + " and " + bot2.toString()+ " it's a tie");
        }
    }
}
