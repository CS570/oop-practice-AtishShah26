[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/bWrxVXn-)
# Object Oriented Programming Example

In this example, we will create a class called `Robot`. A robot is going to be
made of a few different parts. It will have a name, a color, and a left motor and a right motor.
The robot will be able to drive forward and backward, and it will be able to turn.

You will create a class called `Robot` that has the following properties:

* `name` - a string
* `color` - a string
* `left_motor` - a Motor (to be imported from motors.py)
* `right_motor` - a Motor (to be imported from motors.py)

The `Robot` class in a file called `robot.py` that will have the following methods:

* `__init__` - a constructor that takes a name, a color. It will also create a left motor and a right motor.
* `drive_forward` - a method that takes a speed and drives the robot forward at that speed, by setting the right and left motors to the same speed.
* `reverse` - a method that reverses the direction of both motors.
* `turn_left` - a method that turns the robot left by setting the left motor to a speed of 0 and the right motor to a speed of 1.
* `turn_right` - a method that turns the robot right by setting the right motor to a speed of 0 and the left motor to a speed of 1.


