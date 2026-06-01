import cv2
import numpy as np
import random
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 960)

detector = HandDetector(detectionCon=0.5, maxHands=1)

snake_pos = [(300, 300)]
snake_length = 1
direction = None
apple_pos = (random.randint(100, 540), random.randint(100, 380))
score = 0
game_over = False

def draw_snake(img, snake_pos):
    for i, pos in enumerate(snake_pos):
        cv2.circle(img, pos, 15, (0, 255, 0), cv2.FILLED)

def check_collision_with_self(snake_pos):
    head = snake_pos[0]
    return head in snake_pos[1:]

def check_collision_with_apple(snake_pos, apple_pos):
    head = snake_pos[0]
    if abs(head[0] - apple_pos[0]) < 20 and abs(head[1] - apple_pos[1]) < 20:
        return True
    return False

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    if not game_over:
        hands, img = detector.findHands(img, flipType=False)
        if hands:
            hand = hands[0]  
            fingers = detector.fingersUp(hand)
            num_fingers = fingers.count(1)
            if num_fingers == 2:  
                direction = "UP"
            elif num_fingers == 3:  
                direction = "RIGHT"
            elif num_fingers == 4:  
                direction = "DOWN"
            elif num_fingers == 5:  
                direction = "LEFT"
            elif num_fingers == 1:  
                direction = "STOP"

        if direction:
            head_x, head_y = snake_pos[0]
            if direction == "UP":
                head_y -= 7
            elif direction == "RIGHT":
                head_x += 7
            elif direction == "DOWN":
                head_y += 7
            elif direction == "LEFT":
                head_x -= 7
            elif direction == "STOP":
                head_x -= 0

            if head_x >= 1280:
                head_x = 0
            elif head_x < 0:
                head_x = 1280
            if head_y >= 960:
                head_y = 0
            elif head_y < 0:
                head_y = 960

            snake_pos.insert(0, (head_x, head_y))

            if check_collision_with_apple(snake_pos, apple_pos):
                score += 1
                apple_pos = (random.randint(100, 500), random.randint(100, 400))
                snake_length += 5
            else:
                snake_pos = snake_pos[:snake_length]

            if check_collision_with_self(snake_pos):
                game_over = True

        draw_snake(img, snake_pos)
        cv2.circle(img, apple_pos, 20, (0, 0, 255), cv2.FILLED)
        cv2.putText(img, f"Score: {score}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(img, "Stop:0", (1000, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(img, "Up:1", (1000, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(img, "Right:2", (1000, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(img, "Down:3", (1000, 160), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(img, "Left:4", (1000, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        if direction:
            cv2.putText(img, f"Direction: {direction}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    else:
        cv2.putText(img, "Game Over! Press 'r' to Restart", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        cv2.putText(img, "Game Over! Press 'q' to Quit", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    
    key = cv2.waitKey(1)
    if key == ord('r'):
        snake_pos = [(300, 300)]
        snake_length = 1
        direction = None
        apple_pos = (random.randint(100, 500), random.randint(100, 400))
        score = 0
        game_over = False

    cv2.imshow("Snake Game", img)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
