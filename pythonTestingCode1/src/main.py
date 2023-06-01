# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       kevinorjalo                                                  #
# 	Created:      23/05/2023, 17:48:49                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Robot configuration code
brain = Brain()
Remote = Controller(PRIMARY)
x = int()

rightFrontMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
rightBackMotor = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
leftFrontMotor = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
leftBackMotor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)

Punchermotor_1 = Motor(Ports.PORT5, GearSetting.RATIO_36_1, False)
rollerMotor_1 = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
rollerMotor_2 = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)

limit_switch_a = Limit(brain.three_wire_port.a)


def remoteControl(Remote, rightFrontMotor, rightBackMotor, leftFrontMotor, leftBackMotor):
  while True:
   
   #init
   fwd = Remote.axis3.position()
   sideways = Remote.axis1.position()
   leftTrain = fwd + sideways
   rightTrain = fwd - sideways

   #drivetrain
   rightFrontMotor.set_velocity(rightTrain, PERCENT)
   rightBackMotor.set_velocity(rightTrain, PERCENT)
   leftFrontMotor.set_velocity(leftTrain, PERCENT)
   leftBackMotor.set_velocity(leftTrain, PERCENT)
   rightFrontMotor.spin(FORWARD)
   rightBackMotor.spin(FORWARD)
   leftFrontMotor.spin(FORWARD)
   leftBackMotor.spin(FORWARD)

   # Punchermotor control
   if Remote.buttonR2.pressing():
      Punchermotor_1.set_velocity(50, PERCENT)
      while limit_switch_a.pressing != True:
         Punchermotor_1.spin(FORWARD)
      sleep(10, MSEC)
   else:
      Punchermotor_1.stop()
   if Remote.buttonR2.pressing() and limit_switch_a.pressing == True:
      Punchermotor_1.set_velocity(50, PERCENT)
      while limit_switch_a == True:
         Punchermotor_1.spin(FORWARD)
      sleep(10, MSEC)
   else:
      Punchermotor_1.stop()

   #roller intake control
   if Remote.buttonL2.pressing():
      rollerMotor_1.set_velocity(50, PERCENT)
      rollerMotor_2.set_velocity(50, PERCENT)
      rollerMotor_1.spin(FORWARD)
      rollerMotor_2.spin(FORWARD)
   elif Remote.buttonL1.pressing():
      rollerMotor_1.set_velocity(-50, PERCENT)
      rollerMotor_2.set_velocity(-50, PERCENT)
      rollerMotor_1.spin(FORWARD)
      rollerMotor_2.spin(FORWARD)
   else:
      rollerMotor_1.stop()
      rollerMotor_2.stop()


remoteControl(Remote, rightFrontMotor, rightBackMotor, leftFrontMotor, leftBackMotor)



def autonCode():
  #init
  global x

#turning from start point to angle toward goal, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 400, DEGREES, wait=False) 
  rightBackMotor.spin_for(FORWARD, 400, DEGREES, wait=True)
  print("Turning COMPLETE")
  wait(500, MSEC)
#to move closer to goal and punch alliance triball, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, 500, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, 500, DEGREES, wait=True)
  rollerMotor_1.spin_for(FORWARD, -400, DEGREES, wait=False)
  rollerMotor_2.spin_for(FORWARD, 400, DEGREES, wait=True)
  print("Moving closer to goal and firing COMPLETE")
  wait(500, MSEC)
#to rotate toward the diagonal boundary, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, -360, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, -360, DEGREES, wait=True)
  print("Rotating toward diagonal boundary COMPLETE")
  wait(500, MSEC)
#to move toward the diagonal boundary, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 300, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 300, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, 300, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, 300, DEGREES, wait=True)
  print("Moving toward diagonal boundary COMPLETE")
  wait(500, MSEC)
#engage rolleer to pick up new triball, TO CHANGE VALUE
  rollerMotor_1.spin_for(FORWARD, 400, DEGREES, wait=False)
  rollerMotor_2.spin_for(FORWARD, -400, DEGREES, wait=True)
#move back, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, -300, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, -300, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, -300, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, -300, DEGREES, wait=True)
  print("Moving back COMPLETE")
  wait(500, MSEC)
#rotate back, TO CHANGE VALUES
  rightFrontMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 360, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, -360, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, -360, DEGREES, wait=True)
  print("rotate back COMPLETE")
  wait(500, MSEC)
  
#endgame code to be inserted. else, code for contact to elevation bar
  rightFrontMotor.spin_for(FORWARD, 300, DEGREES, wait=False)
  rightBackMotor.spin_for(FORWARD, 300, DEGREES, wait=False)
  leftFrontMotor.spin_for(FORWARD, 300, DEGREES, wait=False)
  leftBackMotor.spin_for(FORWARD, 300, DEGREES, wait=True)
  print("Moving toward elevation bar COMPLETE")
  wait(500, MSEC)
  #to insert further code. (rotate &  contact with elevation bar TBD)
   
  x += 1


if x == 1:
   print("code COMPLETE")