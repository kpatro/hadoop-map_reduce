# hadoop-map_reduce
Simple Program to demonstrate Map Reduce Technique
Steps:
1. Data file is taken as an input, to identify the columns that's propagated to next step.
2. First Mapper reads the data and propagates columns of interest to reducer.
3. Reducer takes it and reduces it to identify only the repairs and accidents.
4. Then another Mapper takes the output created in above step to only filter columns needed.
5. FInally reducer counts the data as per requiremernt to identify the counut of accidents per make and year of vehicle.
