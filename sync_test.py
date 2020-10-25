import os 
import pandas as pd
import shutil

wd = "/home/pi/Desktop/MetaBase-CSV-Bash-Test/"

lst = os.listdir(wd)

# left_acc = None
# left_gyro = None
# left_mag = None
right_acc = None
right_gyro = None
right_mag = None

for l in lst:
	# if "Left" in l and "Accelerometer" in l:
	# 	left_acc_name = l
	# 	left_acc = pd.read_csv(wd+l, usecols = ["epoc (ms)","x-axis (g)","y-axis (g)","z-axis (g)"])
	# elif "Left" in l and "Gyroscope" in l:
	# 	left_gyro_name = l
	# 	left_gyro = pd.read_csv(wd+l, usecols = ["epoc (ms)","x-axis (deg/s)","y-axis (deg/s)","z-axis (deg/s)"])
	# elif "Left" in l and "Magnetometer" in l:
	# 	left_mag_name = l
	# 	left_mag = pd.read_csv(wd+l, usecols = ["epoc (ms)","x-axis (T)","y-axis (T)","z-axis (T)"])
	if "Right" in l and "Accelerometer" in l:
		right_acc_name = l
		try:
			right_acc = pd.read_csv(wd+l, usecols = ["epoc (ms)","x-axis (g)","y-axis (g)","z-axis (g)"])
		except:
			right_acc = pd.read_csv(wd+l, usecols = ["epoch (ms)","x-axis (g)","y-axis (g)","z-axis (g)"])
	elif "Right" in l and "Gyroscope" in l:
		right_gyro_name = l
		try:
			right_gyro = pd.read_csv(wd+l, usecols = ["epoc (ms)","x-axis (deg/s)","y-axis (deg/s)","z-axis (deg/s)"])
		except:
			right_gyro = pd.read_csv(wd+l, usecols = ["epoch (ms)","x-axis (deg/s)","y-axis (deg/s)","z-axis (deg/s)"])
	elif "Right" in l and "Magnetometer" in l:
		right_mag_name = l
		try:
			right_mag = pd.read_csv(wd+l, usecols = ["epoc (ms)","x-axis (T)","y-axis (T)","z-axis (T)"])
		except:
			right_mag = pd.read_csv(wd+l, usecols = ["epoch (ms)","x-axis (T)","y-axis (T)","z-axis (T)"])

#if left_acc is None or left_gyro is None or right_acc is None or right_gyro is None:
if right_acc is None or right_gyro is None:
	print("Error with download")
	exit(10)
else:
	print("Success")
	#filenames = [left_mag_name,left_gyro_name,left_acc_name,right_mag_name,right_gyro_name,right_acc_name]
	filenames = [right_mag_name,right_gyro_name,right_acc_name]
	#Left Leg
	try:
		df_right_1 = pd.merge_asof(right_acc.sort_values('epoch (ms)'), right_gyro, 'epoch (ms)')
		df_right = pd.merge_asof(df_right_1, right_mag, 'epoch (ms)')
	except:
		df_right_1 = pd.merge_asof(right_acc.sort_values('epoc (ms)'), right_gyro, 'epoc (ms)')
		df_right = pd.merge_asof(df_right_1, right_mag, 'epoc (ms)')

	#Both Legs
	# if len(df_left) < len(df_right):
	# 	df_right_new = df_right[:len(df_left)]
	# 	df_right_new = df_right_new.rename(columns = {"x-axis (g)":"r_x-axis (g)",
	# 		"y-axis (g)":"r_y-axis (g)",
	# 		"z-axis (g)":"r_z-axis (g)",
	# 		"x-axis (deg/s)":"r_x-axis (deg/s)",
	# 		"y-axis (deg/s)":"r_y-axis (deg/s)",
	# 		"z-axis (deg/s)":"r_z-axis (deg/s)",
	# 		"x-axis (T)":"r_x-axis (T)",
	# 		"y-axis (T)":"r_y-axis (T)",
	# 		"z-axis (T)":"r_z-axis (T)"})
	# 	df_legs = pd.concat([df_left, df_right_new.drop(columns = ["epoc (ms)"])], axis=1)
	# 	df_left.to_csv(wd+"Test/Left.txt",sep = ',',index=False)
	# 	df_right_new.to_csv(wd+"Test/Right.txt",sep = ',',index=False)
	# 	df_legs.to_csv(wd+"Test/Both.txt",sep = ',',index=False)
	# 	df_left.to_csv(wd+"Test/Left.csv",sep = ',',index=False)
	# 	df_right_new.to_csv(wd+"Test/Right.csv",sep = ',',index=False)
	# 	df_legs.to_csv(wd+"Test/Both.csv",sep = ',',index=False)
	# else:
	# 	df_left_new = df_left[:len(df_right)]
	# 	df_right = df_right.rename(columns = {"x-axis (g)":"r_x-axis (g)",
	# 		"y-axis (g)":"r_y-axis (g)",
	# 		"z-axis (g)":"r_z-axis (g)",
	# 		"x-axis (deg/s)":"r_x-axis (deg/s)",
	# 		"y-axis (deg/s)":"r_y-axis (deg/s)",
	# 		"z-axis (deg/s)":"r_z-axis (deg/s)",
	# 		"x-axis (T)":"r_x-axis (T)",
	# 		"y-axis (T)":"r_y-axis (T)",
	# 		"z-axis (T)":"r_z-axis (T)"})
	# 	df_legs = pd.concat([df_left_new, df_right.drop(columns = ["epoc (ms)"])], axis=1)
		# df_left_new.to_csv("~/Desktop/Test/Left.txt",sep = ',',index=False)
		# df_right.to_csv("~/Desktop/Test/Right.txt",sep = ',',index=False)
		# df_legs.to_csv("~/Desktop/Test/Both.txt",sep = ',',index=False)
		# df_left.to_csv("~/Desktop/Test/Left.csv",sep = ',',index=False)
		# df_right_new.to_csv("~/Desktop/Test/Right.csv",sep = ',',index=False)
		# df_legs.to_csv("~/Desktop/Test/Both.csv",sep = ',',index=False)

	df_right.to_csv(wd+"data.csv",sep = ',', index=False)
	for f in filenames:
		shutil.move(wd+f,wd+'Old/'+f)




	



