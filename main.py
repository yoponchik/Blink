#https://www.youtube.com/watch?v=VWUgkcX_KoY
import cv2
import numpy as np
import dlib
from math import hypot
import pyglet
import time
import win32api
from time import sleep

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()

font = cv2.FONT_HERSHEY_PLAIN


picture1 = 'playtest1.jpg'
picture2 = 'playtest2.jpg'
picture3 = 'playtest3.jpg'


sound = pyglet.media.load("knock.mp3")


savedpos = win32api.GetCursorPos()
count = 0


def moveWindow(winname, img, x, y):
    cv2.namedWindow(winname)        # Create a named window
    cv2.moveWindow(winname, x, y)   # Move it to (x,y)
    cv2.imshow(winname,img)

def resize(scale_percent, img):

    #scale_percent = 60  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized


def get_blink_ratio(eyepoints, facial_landmarks):
    left_point = (facial_landmarks.part(eyepoints[0]).x, facial_landmarks.part(eyepoints[0]).y)
    right_point = (facial_landmarks.part(eyepoints[3]).x, facial_landmarks.part(eyepoints[3]).y)
    center_top = midpoint(facial_landmarks.part(eyepoints[1]), facial_landmarks.part(eyepoints[2]))
    center_bottom = midpoint(facial_landmarks.part(eyepoints[5]), facial_landmarks.part(eyepoints[4]))

    #hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)  # line from one end of eye to another
    #ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)  # vertical center line

    hor_line_length = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_length / ver_line_length

    return ratio

def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y +p2.y)/2)       #function finds midpoint, then connect those points with a line; to get a line from top end of eye to bottom
                                                                #finds the vertical center line


def get_gaze_ratio(eye_points, facial_landmarks):
    # gaze detection
    left_eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y),
                                (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y),
                                (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y),
                                (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y),
                                (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y),
                                (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)], np.int32)

    # cv2.polylines(frame, [left_eye_region], True, (0, 0, 255), 2)   #image, points, close polygon?, color, thickness

    height, width, _ = frame.shape
    mask = np.zeros((height, width), np.uint8)  # make black screen
    cv2.polylines(mask, [left_eye_region], True, (0, 0, 255), 2)
    cv2.fillPoly(mask, [left_eye_region], 255)

    eye = cv2.bitwise_and(gray_face, gray_face, mask=mask)

    min_x = np.min(left_eye_region[:, 0])  # using slice assignment; take first value of array; the x
    max_x = np.max(left_eye_region[:, 0])
    min_y = np.min(left_eye_region[:, 1])  # take second value of array; the y value
    max_y = np.max(left_eye_region[:, 1])

    # eye = frame[min_y: max_y, min_x: max_x]
    # gray_eye = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)

    gray_eye = eye[min_y: max_y, min_x: max_x]  # src already a gray image
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255,
                                     cv2.THRESH_BINARY_INV)  # threshold colors in source to 70 to 255
    height, width = threshold_eye.shape

    left_side_threshold = threshold_eye[0: height, 0: int(width / 2)]  # pixels are always integers
    left_side_white = cv2.countNonZero(left_side_threshold)

    right_side_threshold = threshold_eye[0: height, int(width / 2): width]
    right_side_white = cv2.countNonZero(right_side_threshold)


    if left_side_white == 0:
        gaze_ratio = 1
    elif right_side_white ==0:
        gaze_ratio = 5
    else:
        gaze_ratio = left_side_white / right_side_white

    return gaze_ratio

while True:
    _, frame = cap.read()

    gray_face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    predictor = dlib.shape_predictor("face_landmarks.dat")



    faces = detector(gray_face)
    for face in faces:

        landmarks = predictor(gray_face, face)


        #detect blinking
        left_eye_ratio = get_blink_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blink_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blink_ratio = (left_eye_ratio + right_eye_ratio) /2   #average


        #if blink_ratio > 5.7:
            #cv2.putText(frame, "BLINKING", (50, 150), font, 3, (255, 0, 0)) #windowname, display text, text position, font, font size, color

        #print(blink_ratio)

        #Gaze Detection
        gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
        gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)
        gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye)/2

        #Showing Direction


        if count  < 4:
            while 0.7 < gaze_ratio < 1.9:
                cv2.putText(frame, "CENTER", (50, 150), font, 2, (0, 0, 255), 3)
                img = cv2.imread(picture1)
                img = resize(60, img)
                moveWindow("DON'T BLINK", img, 250, 150)

                print("lights off")
                print(count)
                break
            else:
                cv2.putText(frame, "OFFSCREEN", (50, 150), font, 2, (0, 0, 255), 3)
                print("add 1")
                count +=1
                print(count)
            if blink_ratio > 5.7:
                print("add 1")
                count += 1
                print(count)
        elif count < 8:
            while 0.7 < gaze_ratio < 1.9:
                cv2.putText(frame, "CENTER", (50, 150), font, 2, (0, 0, 255), 3)
                img = cv2.imread(picture2)
                img = resize(60, img)
                moveWindow("DON'T BLINK", img, 250, 150)
                print("lights on")
                print(count)
                break
            else:
                cv2.putText(frame, "OFFSCREEN", (50, 150), font, 2, (0, 0, 255), 3)
                print("add1")
                print(count)
                count += 1
            if blink_ratio > 5.7:
                print("add 1")
                count += 1
                print(count)
        elif count < 15:
            while 0.7 < gaze_ratio < 1.9:
                cv2.putText(frame, "CENTER", (50, 150), font, 2, (0, 0, 255), 3)
                img = cv2.imread(picture3)
                img = resize(60, img)
                moveWindow("DON'T BLINK", img, 250, 150)
                print("lights on")
                print(count)
                break
            else:
                cv2.putText(frame, "OFFSCREEN", (50, 150), font, 2, (0, 0, 255), 3)
                print("add1")
                print(count)
                count += 1
            if blink_ratio > 5.7:
                print("add 1")
                count += 1
                print(count)

            else:
                break






        '''
        curpos = win32api.GetCursorPos()
        if savedpos != curpos:
            time.sleep(5)
            sound.play()
            count = count + 1
            savedpos = curpos
            print("Mouse Movement # ", count)
        '''

    cv2.imshow("face", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


