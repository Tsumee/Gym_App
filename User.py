import java.util.Scanner; // Import the Scanner class

public class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in); // Create a Scanner object
    System.out.println("Enter your name: "); // Display a message
    String name = input.nextLine(); // Read user input as a String
    System.out.println("Enter your age: "); // Display another message
    int age = input.nextInt(); // Read user input as an int
    System.out.println("Your name is: " + name); // Display the input value
    System.out.println("Your age is: " + age); // Display the input value
  }
}
