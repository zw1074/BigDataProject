#!/bin/bash
echo "All mission start"
echo "Change the chmod of each .py file"
chmod 755 *.py

echo "Change the road of hadoop server"

echo "Transfer data to hadoop server"
hfs -copyFromLocal -f ./*.* /user/zw1074/

echo "Starting Mission 1: Index"
echo "Mission 1: Index" >> log.txt
hjs -D mapreduce.job.reduces=3 -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input /user/zw1074/weather-data.txt -output /user/zw1074/index.output >> log.txt
echo "Finished!"

echo "Starting Mission 2: Trips and Duration Time"
echo "\nMission 2: Trips and Duration Time" >> log.txt
hjs -D mapreduce.job.reduces=3 -files mapper_drivingtime.py,reducer_drivingtime.py -mapper mapper_drivingtime.py -reducer reducer_drivingtime.py -input /user/zw1074/201501-citibike-tripdata.csv /user/zw1074/201502-citibike-tripdata.csv /user/zw1074/201503-citibike-tripdata.csv /user/zw1074/201504-citibike-tripdata.csv 201505-citibike-tripdata.csv /user/zw1074/201506-citibike-tripdata.csv 201507-citibike-tripdata.csv /user/zw1074/201508-citibike-tripdata.csv /user/zw1074/201509-citibike-tripdata.csv /user/zw1074/201510-citibike-tripdata.csv /user/zw1074/201511-citibike-tripdata.csv /user/zw1074/201512-citibike-tripdata.csv /user/zw1074/index.output -output /user/zw1074/drivingtime.output >> log.txt
echo "Finished!"

echo "Starting Mission 3: Member"
echo "\nMission 3: Duration time" >> log.txt
hjs -D mapreduce.job.reduces=3 -files mapper_member.py,reducer_drivingtime.py -mapper mapper_member.py -reducer reducer_drivingtime.py -input /user/zw1074/201501-citibike-tripdata.csv /user/zw1074/201502-citibike-tripdata.csv /user/zw1074/201503-citibike-tripdata.csv /user/zw1074/201504-citibike-tripdata.csv 201505-citibike-tripdata.csv /user/zw1074/201506-citibike-tripdata.csv 201507-citibike-tripdata.csv /user/zw1074/201508-citibike-tripdata.csv /user/zw1074/201509-citibike-tripdata.csv /user/zw1074/201510-citibike-tripdata.csv /user/zw1074/201511-citibike-tripdata.csv /user/zw1074/201512-citibike-tripdata.csv /user/zw1074/index.output -output /user/zw1074/member.output >> log.txt
echo "Finished!"

echo "Starting Mission 4: Gender"
echo "\nMission 4: Gender" >> log.txt
hjs -D mapreduce.job.reduces=3 -files mapper_gender.py,reducer_gender.py -mapper mapper_gender.py -reducer reducer_gender.py -input /user/zw1074/201501-citibike-tripdata.csv /user/zw1074/201502-citibike-tripdata.csv /user/zw1074/201503-citibike-tripdata.csv /user/zw1074/201504-citibike-tripdata.csv 201505-citibike-tripdata.csv /user/zw1074/201506-citibike-tripdata.csv 201507-citibike-tripdata.csv /user/zw1074/201508-citibike-tripdata.csv /user/zw1074/201509-citibike-tripdata.csv /user/zw1074/201510-citibike-tripdata.csv /user/zw1074/201511-citibike-tripdata.csv /user/zw1074/201512-citibike-tripdata.csv /user/zw1074/index.output -output /user/zw1074/gender.output >> log.txt
echo "Finished!"

echo "Starting Mission 5: Gender all year"
echo "\nMission 5: Gender all year" >> log.txt
hjs -D mapreduce.job.reduces=1 -files mapper_gender.py,reducer_all_gender.py -mapper mapper_gender.py -reducer reducer_all_gender.py -input /user/zw1074/201501-citibike-tripdata.csv /user/zw1074/201502-citibike-tripdata.csv /user/zw1074/201503-citibike-tripdata.csv /user/zw1074/201504-citibike-tripdata.csv 201505-citibike-tripdata.csv /user/zw1074/201506-citibike-tripdata.csv 201507-citibike-tripdata.csv /user/zw1074/201508-citibike-tripdata.csv /user/zw1074/201509-citibike-tripdata.csv /user/zw1074/201510-citibike-tripdata.csv /user/zw1074/201511-citibike-tripdata.csv /user/zw1074/201512-citibike-tripdata.csv /user/zw1074/index.output -output /user/zw1074/all_gender.output >> log.txt
echo "Finished!"

echo "Starting Mission 6: Age"
echo "\nMission 6: Age" >> log.txt
hjs -D mapreduce.job.reduces=3 -files mapper_age.py,reducer_age.py -mapper mapper_age.py -reducer reducer_age.py -input /user/zw1074/201501-citibike-tripdata.csv /user/zw1074/201502-citibike-tripdata.csv /user/zw1074/201503-citibike-tripdata.csv /user/zw1074/201504-citibike-tripdata.csv 201505-citibike-tripdata.csv /user/zw1074/201506-citibike-tripdata.csv 201507-citibike-tripdata.csv /user/zw1074/201508-citibike-tripdata.csv /user/zw1074/201509-citibike-tripdata.csv /user/zw1074/201510-citibike-tripdata.csv /user/zw1074/201511-citibike-tripdata.csv /user/zw1074/201512-citibike-tripdata.csv /user/zw1074/index.output -output /user/zw1074/age.output >> log.txt
echo "Finished!"

echo "Starting Mission 7: Age all year"
echo "\nMission 7: Age all year" >> log.txt
hjs -D mapreduce.job.reduces=1 -files mapper_age.py,reducer_all_age.py -mapper mapper_age.py -reducer reducer_all_age.py -input /user/zw1074/201501-citibike-tripdata.csv /user/zw1074/201502-citibike-tripdata.csv /user/zw1074/201503-citibike-tripdata.csv /user/zw1074/201504-citibike-tripdata.csv 201505-citibike-tripdata.csv /user/zw1074/201506-citibike-tripdata.csv 201507-citibike-tripdata.csv /user/zw1074/201508-citibike-tripdata.csv /user/zw1074/201509-citibike-tripdata.csv /user/zw1074/201510-citibike-tripdata.csv /user/zw1074/201511-citibike-tripdata.csv /user/zw1074/201512-citibike-tripdata.csv /user/zw1074/index.output -output /user/zw1074/all_age.output >> log.txt
echo "Finished!"

echo "Starting Mission 8: Temperature"
echo "\nMission 8: Temperature" >> log.txt
hjs -D mapreduce.job.reduces=3 -files mapper_speed_1.py,reducer_speed_1.py -mapper mapper_speed_1.py -reducer reducer_speed_1.py -input /user/zw1074/weather-data.txt -output /user/zw1074/temperature.output >> log.txt
echo "Finished!"

echo "Starting Mission 9: Trip vs. Temperature"
echo "\nMission 9: Trip vs. Temperature" >> log.txt
hjs -D mapreduce.job.reduces=1 -files mapper_speed_2.py,reducer_speed_2.py -mapper mapper_speed_2.py -reducer reducer_speed_2.py -input /user/zw1074/201501-citibike-tripdata.csv /user/zw1074/201502-citibike-tripdata.csv /user/zw1074/201503-citibike-tripdata.csv /user/zw1074/201504-citibike-tripdata.csv 201505-citibike-tripdata.csv /user/zw1074/201506-citibike-tripdata.csv 201507-citibike-tripdata.csv /user/zw1074/201508-citibike-tripdata.csv /user/zw1074/201509-citibike-tripdata.csv /user/zw1074/201510-citibike-tripdata.csv /user/zw1074/201511-citibike-tripdata.csv /user/zw1074/201512-citibike-tripdata.csv /user/zw1074/temperature.output -output /user/zw1074/trip-temperature.output >> log.txt
echo "Finished!"

echo "Starting Mission 10: Trips_all"
echo "\nMission 10: Trips_all" >> log.txt
hjs -D mapreduce.job.reduces=1 -files mapper_trips_all.py,reducer_trips_all.py -mapper mapper_trips_all.py -reducer reducer_trips_all.py -input /user/zw1074/201501-citibike-tripdata.csv /user/zw1074/201502-citibike-tripdata.csv /user/zw1074/201503-citibike-tripdata.csv /user/zw1074/201504-citibike-tripdata.csv 201505-citibike-tripdata.csv /user/zw1074/201506-citibike-tripdata.csv 201507-citibike-tripdata.csv /user/zw1074/201508-citibike-tripdata.csv /user/zw1074/201509-citibike-tripdata.csv /user/zw1074/201510-citibike-tripdata.csv /user/zw1074/201511-citibike-tripdata.csv /user/zw1074/201512-citibike-tripdata.csv /user/zw1074/temperature.output -output /user/zw1074/trips-all.output >> log.txt
echo "Finished!"
echo "All mission finished, now get the output"

hjs -D mapreduce.job.reduces=3 -files mapper_snow_1.py,reducer_snow_1.py -mapper mapper_snow_1.py -reducer reducer_snow_1.py -input /user/zw1074/weather-data.txt -output /user/zw1074/snow.output

hjs -D mapreduce.job.reduces=1 -files mapper_snow_2.py,reducer_snow_2.py -mapper mapper_snow_2.py -reducer reducer_snow_2.py -input /user/zw1074/201501-citibike-tripdata.csv /user/zw1074/201502-citibike-tripdata.csv /user/zw1074/201503-citibike-tripdata.csv /user/zw1074/201504-citibike-tripdata.csv 201505-citibike-tripdata.csv /user/zw1074/201506-citibike-tripdata.csv 201507-citibike-tripdata.csv /user/zw1074/201508-citibike-tripdata.csv /user/zw1074/201509-citibike-tripdata.csv /user/zw1074/201510-citibike-tripdata.csv /user/zw1074/201511-citibike-tripdata.csv /user/zw1074/201512-citibike-tripdata.csv /user/zw1074/snow.output -output /user/zw1074/snow_2.output

hjs -D mapreduce.job.reduces=3 -files mapper_week.py,reducer_week.py -mapper mapper_week.py -reducer reducer_week.py -input /user/zw1074/201501-citibike-tripdata.csv /user/zw1074/201502-citibike-tripdata.csv /user/zw1074/201503-citibike-tripdata.csv /user/zw1074/201504-citibike-tripdata.csv 201505-citibike-tripdata.csv /user/zw1074/201506-citibike-tripdata.csv 201507-citibike-tripdata.csv /user/zw1074/201508-citibike-tripdata.csv /user/zw1074/201509-citibike-tripdata.csv /user/zw1074/201510-citibike-tripdata.csv /user/zw1074/201511-citibike-tripdata.csv /user/zw1074/201512-citibike-tripdata.csv /user/zw1074/index.output -output /user/zw1074/heatmapbigger.output

hfs -get /user/zw1074/*.output ./output/
echo "Now you can find the output/ folder in current directory."
