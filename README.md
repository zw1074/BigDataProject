This folder is for the soruce code. The code for our project has two main part. One is Mapreduce, and the other is graph.

######################### MapReduce ###############################

You can follow the steps in the do_all.sh file. Then get the output to the local file.

######################### Graph ###################################

As you can see, there are files that have graph being their prefix. Note that to run it successfully, you must modify the input file name in the graph_file.

And another important thing here is that you have two different drvingtime (duration time) output. One is for all the user (member + customer), and one is only for member. But they have the same data structure. So you just need to modify the input file name in graph_drivingtime.py here.