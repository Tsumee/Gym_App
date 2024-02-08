// workout.h
// A header file for a workout class

public class Workout {
  // Declare the fields of the class
  private String name; // The name of the workout
  private int sets; // The number of sets
  private int reps; // The number of repetitions
  private int weight; // The weight used in kilograms
  private int duration; // The duration of the workout in minutes
  private int calories; // The calories burned during the workout

  // Define the constructor of the class
  public Workout(String name, int sets, int reps, int weight, int duration, int calories) {
    // Initialize the fields with the parameters
    this.name = name;
    this.sets = sets;
    this.reps = reps;
    this.weight = weight;
    this.duration = duration;
    this.calories = calories;
  }

  // Define the getters and setters of the class
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getSets() {
    return sets;
  }

  public void setSets(int sets) {
    this.sets = sets;
  }

  public int getReps() {
    return reps;
  }

  public void setReps(int reps) {
    this.reps = reps;
  }

  public int getWeight() {
    return weight;
  }

  public void setWeight(int weight) {
    this.weight = weight;
  }

  public int getDuration() {
    return duration;
  }

  public void setDuration(int duration) {
    this.duration = duration;
  }

  public int getCalories() {
    return calories;
  }

  public void setCalories(int calories) {
    this.calories = calories;
  }

  // Define other methods of the class
  public void start() {
    // A method that starts the workout
    System.out.println("Starting the " + name + " workout.");
  }

  public void finish() {
    // A method that finishes the workout
    System.out.println("Finishing the " + name + " workout.");
  }

  public void showDetails() {
    // A method that shows the details of the workout
    System.out.println("Name: " + name);
    System.out.println("Sets: " + sets);
    System.out.println("Reps: " + reps);
    System.out.println("Weight: " + weight + " kg");
    System.out.println("Duration: " + duration + " minutes");
    System.out.println("Calories: " + calories + " kcal");
  }
}
