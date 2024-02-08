// main.h
// A header file for a gym app

#ifndef MAIN_H
#define MAIN_H

#include <iostream>
#include <string>
#include <vector>
#include "user.h"
#include "workout.h"
#include "diet.h"

// A class that represents the gym app
class GymApp {
  public:
    // Constructor that takes the user's name and age
    GymApp(const std::string& name, int age);

    // Destructor
    ~GymApp();

    // A method that displays the main menu of the app
    void showMenu();

    // A method that allows the user to create a profile
    void createProfile();

    // A method that allows the user to view their profile
    void viewProfile();

    // A method that allows the user to edit their profile
    void editProfile();

    // A method that allows the user to choose a workout plan
    void chooseWorkout();

    // A method that allows the user to view their workout progress
    void viewWorkout();

    // A method that allows the user to choose a diet plan
    void chooseDiet();

    // A method that allows the user to view their diet progress
    void viewDiet();

    // A method that allows the user to log out of the app
    void logOut();

  private:
    // A pointer to the user object
    User* user;

    // A pointer to the workout object
    Workout* workout;

    // A pointer to the diet object
    Diet* diet;
};

#endif
