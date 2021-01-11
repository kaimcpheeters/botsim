
public class Bot {
    int round;
    int coins;
    int bank;
    String memory;

    public Bot() {
        round = 0;
        coins = 0;
        bank = 0;
        memory = "cooperate";}

    public String toString() {
        return getClass().getName() + String.format("(%d)",this.bank);}

    public void reset(){
        this.round = 0;
        this.coins = 0;
        this.memory = "cooperate";
        secondary_reset();}

    public void secondary_reset() {
    }

    public String decide() {
        return "cooperate";
    }
}
