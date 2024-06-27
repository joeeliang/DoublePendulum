import numpy as np 
from numpy.linalg import inv
from matplotlib import pyplot as plt
from math import cos, sin, pi
import pygame
import sys
import os

def G(y,t): 
    theta1, theta2, omega1, omega2 = y
    f1 = omega1
    f2 = omega2
    f3 = (-g * (2 * m1 + m2) * sin(theta1) - m2 * g * sin(theta1 - 2 * theta2) - 2 * sin(theta1 - theta2) * m2 * (f2**2 * l2 + f1**2 * l1 * cos(theta1 - theta2))) / (l1*(2*m1 + m2 - m2 * cos(2*theta1 - 2* theta2)))
    f4 = (2 * sin(theta1-theta2) * (f1 ** 2 * l1 * (m1 + m2) + g* (m1 + m2) * cos(theta1) + f2**2 * l2 * m2 * cos(theta1- theta2))) / (l2 * (2 * m1 + m2 - m2 * cos(2*theta1 - 2* theta2)))

    return np.array([f1, f2, f3, f4])

def RK4_step(y, t, dt):
    k1 = G(y,t)
    k2 = G(y+0.5*k1*dt, t+0.5*dt)
    k3 = G(y+0.5*k2*dt, t+0.5*dt)
    k4 = G(y+k3*dt, t+dt)

    return dt * (k1 + 2*k2 + 2*k3 + k4)/6

def energy(y):
    theta1, theta2, omega1, omega2 = y
    T = 0.5* (m1 + m2) * l1**2 * omega1**2 + (m2/2) * l2**2 * omega2**2 + m2*l1*l2*omega1*omega2*cos(theta1-theta2)
    U = - (m1+m2)*l1*g*cos(theta1) - m2*l2*g*cos(theta2)
    return T + U

def update(a1, a2):
    scale = 200 * (2 / (l1 + l2))
    x1 = l1*scale * sin(a1) + offset[0]
    y1 = l1*scale * cos(a1) + offset[1]
    x2 = x1 + l2*scale * sin(a2)
    y2 = y1 + l2*scale * cos(a2)

    return (x1, y1), (x2, y2)

def render(point1, point2, prev_point, trace):
    scale = 15
    x1, y1,  = int(point1[0]), int(point1[1])
    x2, y2,  = int(point2[0]), int(point2[1])

    if prev_point:
        xp, yp = prev_point[0], prev_point[1]
        pygame.draw.line(trace, TRAILCOLOUR, (xp, yp), (x2, y2), 3)

    screen.fill(WHITE)	
    screen.blit(trace, (0,0))

    pygame.draw.line(screen, BLACK, offset, (x1,y1), 5)
    pygame.draw.line(screen, BLACK, (x1,y1), (x2,y2), 5)
    pygame.draw.circle(screen, BLACK, offset, 8)
    pygame.draw.circle(screen, COLOUR1, (x1, y1), int(m1*scale))
    pygame.draw.circle(screen, COLOUR2, (x2, y2), int(m2*scale))

    return (x2, y2)

# variables
m1, m2 = 1.0, 1.0
l1, l2 = 1.0, 1.0
g = 9.81

w, h = 850, 850
WHITE = (255,255,255)
BLACK = (0,0,0)
COLOUR1 = (13, 23, 219)
COLOUR2 = (13, 23, 219)
TRAILCOLOUR = (230,230,230)
offset = (h/2, w/2)
screen = pygame.display.set_mode((w,h))
screen.fill(WHITE)
pygame.display.update()
clock = pygame.time.Clock()
screenshotTimes = [30.00]
screenshot_directory = "Images/screenshots"
# initial state

def animate(t1, t2):
    delta_t = 0.01 # increment
    totalTime = 100
    trace = screen.copy()
    t = 0
    time = np.arange(0, totalTime, delta_t)
    prev_point = []

    initial = np.array([t1, t2, 0, 0])   # [theta1, theta2, omega1, omega2]

    pygame.font.init()
    trace.fill(WHITE)
    myfont = pygame.font.SysFont('Comic Sans MS', 38)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        point1, point2 = update(initial[0], initial[1])
        prev_point = render(point1, point2, prev_point,trace)

        t += delta_t

        initial = initial + RK4_step(initial, t, delta_t)

        clock.tick(60)
        pygame.display.update()
