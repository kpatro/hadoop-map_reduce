#!/usr/bin/env bash

hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-file all_acc_mapper.py -mapper all_acc_mapper.py \
-file all_acc_reducer.py -reducer all_acc_reducer.py \
-input input/data.csv -output output/all_accidents

hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-file my_count_mapper.py.py -mapper my_count_mapper.py \
-file my_count_reducer.py -reducer my_count_reducer.py \
-input output/all_accidents -output output/make_year_count