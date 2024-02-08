/**
 * This class represents a gym app that provides instructions for different exercises.
 * @author Your name
 * @version 1.0
 * @since 2024-02-07
 */
public class GymApp {

    /**
     * The main method of the class that runs the app.
     * @param args The command-line arguments (not used).
     */
    public static void main(String[] args) {
        // Create an array of exercises
        String[] exercises = {"push ups", "pull ups", "bench press", "jumping jack", "crunches"};

        // Create a variable for the number of reps
        int reps = 10;

        // Create a variable for the number of sets
        int sets = 4;

        // Loop through the exercises and print the instructions
        for (String exercise : exercises) {
            System.out.println("Do " + reps + " " + exercise + " for " + sets + " sets.");
        }
    }
}
