#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_arm = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
motor_pusher = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
'''
This script controls a VEX V5 robot with a POV drive.
Two motors are attached to a brain and controlled by two joysticks.
'''

# Import the necessary libraries
from vex import *

# Brain should be defined by default
brain=Brain()

# Controller should be defined by default
controller=Controller()

# Robot configuration code
motorRight = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
motorLeft = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)

# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

# Code that runs the robot
while True:
    # clear the screen
    brain.screen.clear_screen()

    # Get the value of the left joystick
    drive = -controller.axis3.position()

    # Get the value of the right joystick
    turn = controller.axis1.position()

    # Combine drive and turn for blended motion
    left = drive + turn
    right = drive - turn

    # Set the left motor to the value of the left joystick
    motorLeft.set_velocity(left, PERCENT)
    motorLeft.spin(FORWARD)

    # Set the right motor to the value of the right joystick
    motorRight.set_velocity(right, PERCENT)
    motorRight.spin(FORWARD)

    # Print the values of the joysticks
    brain.screen.print("Right motor: " + str(right) + " Left motor: " + str(left))

    # TO DO: Add velocity above motor.spin
    # Arm control
    if controller.buttonL1.pressing():
        motor_arm.spin(REVERSE)
    elif controller.buttonL2.pressing():
        motor_arm.spin(FORWARD)
    else:
        motor_arm.set_velocity(0,PERCENT)

    # Wait for 20 milliseconds
    wait(20, MSEC)
