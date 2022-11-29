#!/usr/bin/env python3

import pygame

import rospy
from sensor_msgs.msg import Joy

axes = [0.0]*6
buttons = [0]*17
joy_msg = Joy()
joy_msg.axes = axes
joy_msg.buttons = buttons


class Controller:

    def __init__(self, joyNum=0):
        pygame.joystick.Joystick(joyNum).init()

        # Get the name of the joystick and print it

        print("DS5 Bluetooth Connection Success !")

        # JoyName = pygame.joystick.Joystick(0).get_name()
        # print("Name of the joystick : ", end='')
        # print(JoyName)
        # print('----------')

        # # Get the number of axes
        # JoyAx = pygame.joystick.Joystick(0).get_numaxes()
        # print("Number of Axis : ", end='')
        # print(JoyAx)
        # print('----------')

        # # Get the number of buttons
        # JoyBt = pygame.joystick.Joystick(0).get_numbuttons()
        # print("Number of Buttons : ", end='')
        # print(JoyAx)
        # print('----------')

        # # Get the number of balls
        # JoyBl = pygame.joystick.Joystick(0).get_numballs()
        # print("Number of Balls : ", end='')
        # print(JoyBl)
        # print('----------')

        # # Get the number of hats
        # JoyHt = pygame.joystick.Joystick(0).get_numhats()
        # print("Number of Hats : ", end='')
        # print(JoyHt)
        # print('----------')

        self._joysticks = pygame.joystick.Joystick(joyNum)

    def get_Cross(self):
        pygame.event.pump()
        return self._joysticks.get_button(0)

    def get_Circle(self):
        pygame.event.pump()
        return self._joysticks.get_button(1)

    def get_Triangle(self):
        pygame.event.pump()
        return self._joysticks.get_button(2)

    def get_Square(self):
        pygame.event.pump()
        return self._joysticks.get_button(3)

    def get_L1(self):
        pygame.event.pump()
        return self._joysticks.get_button(4)

    def get_R1(self):
        pygame.event.pump()
        return self._joysticks.get_button(5)

    def get_L2(self):
        pygame.event.pump()
        return self._joysticks.get_button(6)

    def get_R2(self):
        pygame.event.pump()
        return self._joysticks.get_button(7)

    def get_Create(self):
        pygame.event.pump()
        return self._joysticks.get_button(8)

    def get_Option(self):
        pygame.event.pump()
        return self._joysticks.get_button(9)

    def get_PS(self):
        pygame.event.pump()
        return self._joysticks.get_button(10)

    def get_L3(self):
        pygame.event.pump()
        return self._joysticks.get_button(11)

    def get_R3(self):
        pygame.event.pump()
        return self._joysticks.get_button(12)

    def get_DPad(self):
        pygame.event.pump()
        return self._joysticks.get_hat(0)

    def get_leftX(self):
        pygame.event.pump()
        return -self._joysticks.get_axis(0)

    def get_leftY(self):
        pygame.event.pump()
        return -self._joysticks.get_axis(1)

    def get_rightX(self):
        pygame.event.pump()
        return -self._joysticks.get_axis(3)

    def get_rightY(self):
        pygame.event.pump()
        return -self._joysticks.get_axis(4)

    def get_LT(self):
        pygame.event.pump()
        return self._joysticks.get_axis(2)/2 + 0.5

    def get_RT(self):
        pygame.event.pump()
        return self._joysticks.get_axis(5)/2 + 0.5


def eventButton(state, button):
    if state:
        joy_msg.buttons[button] = 1
    else:
        joy_msg.buttons[button] = 0


def eventAxis(state, axis):
    if state > 0.02 or state < -0.02:
        joy_msg.axes[axis] = state
    else:
        joy_msg.axes[axis] = 0


def eventHat(state):
    if state[0] == 1:
        joy_msg.buttons[15] = 0
        joy_msg.buttons[16] = 1
    elif state[0] == -1:
        joy_msg.buttons[15] = 1
        joy_msg.buttons[16] = 0
    else:
        joy_msg.buttons[15] = 0
        joy_msg.buttons[16] = 0

    if state[1] == 1:
        joy_msg.buttons[13] = 1
        joy_msg.buttons[14] = 0
    elif state[1] == -1:
        joy_msg.buttons[13] = 0
        joy_msg.buttons[14] = 1
    else:
        joy_msg.buttons[13] = 0
        joy_msg.buttons[14] = 0


def checkEvent(ds5):

    eventButton(ds5.get_Cross(), 0)
    eventButton(ds5.get_Circle(), 1)
    eventButton(ds5.get_Triangle(), 2)
    eventButton(ds5.get_Square(), 3)
    eventButton(ds5.get_L1(), 4)
    eventButton(ds5.get_R1(), 5)
    eventButton(ds5.get_L2(), 6)
    eventButton(ds5.get_R2(), 7)
    eventButton(ds5.get_L3(), 8)
    eventButton(ds5.get_R3(), 9)
    eventButton(ds5.get_PS(), 10)
    eventButton(ds5.get_Create(), 11)
    eventButton(ds5.get_Option(), 12)
    eventHat(ds5.get_DPad())
    eventAxis(ds5.get_leftX(), 0)
    eventAxis(ds5.get_leftY(), 1)
    eventAxis(ds5.get_rightX(), 2)
    eventAxis(ds5.get_rightY(), 3)
    eventAxis(ds5.get_LT(), 4)
    eventAxis(ds5.get_RT(), 5)


def ds5_bluetooth_node():

    rospy.init_node("ds5_bluetooth_node")
    _ds5JoyPublisher = rospy.Publisher('ds5_joy', Joy, queue_size=100)
    rate = rospy.Rate(100)

    pygame.display.init()
    pygame.joystick.init()

    global axes
    global buttons
    global joy_msg

    ds5 = Controller()

    # Publish the values of the joystick
    while not rospy.is_shutdown():
        checkEvent(ds5)
        _ds5JoyPublisher.publish(joy_msg)
        rate.sleep()


if __name__ == "__main__":
    ds5_bluetooth_node()
