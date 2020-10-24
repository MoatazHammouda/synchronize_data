import os 
import pandas as pd

wd = "/home/pi/Desktop/MetaBase-CSV-Bash/"

lst = os.listdir(wd)

left_acc = None
left_gyro = None
left_mag = None
right_acc = None
right_gyro = None
right_mag = None

for l in lst:
        if "Left" in l and "Accelerometer" in l:
                left_acc = pd.read_csv(wd+l, usecols = ["elapsed (s)","x-axis (g)","y-axis (g)","z-axis (g)"])
        elif "Left" in l and "Gyroscope" in l:
                left_gyro = pd.read_csv(wd+l, usecols = ["elapsed (s)","x-axis (deg/s)","y-axis (deg/s)","z-axis (deg/s)"])
        elif "Left" in l and "Magnetometer" in l:
                left_mag = pd.read_csv(wd+l, usecols = ["elapsed (s)","x-axis (T)","y-axis (T)","z-axis (T)"])
        elif "Right" in l and "Accelerometer" in l:
                right_acc = pd.read_csv(wd+l, usecols = ["elapsed (s)","x-axis (g)","y-axis (g)","z-axis (g)"])
        elif "Right" in l and "Gyroscope" in l:
                right_gyro = pd.read_csv(wd+l, usecols = ["elapsed (s)","x-axis (deg/s)","y-axis (deg/s)","z-axis (deg/s)"])
        elif "Right" in l and "Magnetometer" in l:
                right_mag = pd.read_csv(wd+l, usecols = ["elapsed (s)","x-axis (T)","y-axis (T)","z-axis (T)"])

if left_acc is None or left_gyro is None or right_acc is None or right_gyro is None:
        print("Error with download")
        exit(10)
else:
        print("Success")
        #Left Leg
        df_left_1 = pd.merge_asof(left_acc, left_gyro, 'elapsed (s)')
        df_left = pd.merge_asof(df_left_1, left_mag, 'elapsed (s)')
        #Right Leg
        df_right_1 = pd.merge_asof(right_acc, right_gyro, 'elapsed (s)')
        df_right = pd.merge_asof(df_right_1, right_mag, 'elapsed (s)')

        #Both Legs
        df_legs = pd.merge_asof(df_left, df_right, 'elapsed (s)_x')

        df_left.to_csv("Left.csv")
        df_right.to_csv("Right.csv")
        df_legs.to_csv("Both.csv")
