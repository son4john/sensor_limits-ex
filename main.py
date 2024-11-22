my_dict = {
    1:{"label": "gyro U", "limit": 100},
    2:{"label": "accel U", "limit": 50}
}


test_list = [1, 2]

for i in test_list:
    value1 = my_dict[i]["label"]
    value2 = my_dict[i]["limit"]
    print(f"For {i} the label is: {value1}\n the limit is {value2}")
    
# 1) Get Git setup create a project for this specific thing.
# 2) The old code opens and reads through the data use that
# 3) First check if the label matches the value in that cell
# 4) The test if the value is below the limit.
# 5) If the value fails then write all the information into file
