# To find the number of minutes in 20 day
print(20 * 24 * 60)
# To add a descriptive analysis to the above so that other project members can understand

# print("20 days are " + str(28800) + " minutes")
# print(f"20 days are {28800} minutes")
# print(f"20 days are {20*24*60} minutes")
# print(f"20 days are {20*24*60*60} seconds")


# #We can use variables to represent those numbers that are constant above to avoid repetition
# calculation_to_unit = 24 * 60 * 60
# name_of_unit = "seconds"
# print(f"20 days are {20 * calculation_to_unit} {name_of_unit}")
# print(f"35 days are {35 * calculation_to_unit} {name_of_unit}")
# print(f"35 days are {50 * calculation_to_unit} {name_of_unit}")
# print(f"35 days are {110 * calculation_to_unit} {name_of_unit}")

# #########################################
# # With the variables indicated we can then make changes at the variable level, e.g change from seconds to hours
# calculation_to_unit = 24
# name_of_unit = "hours"
# print(f"20 days are {20 * calculation_to_unit} {name_of_unit}")
# print(f"35 days are {35 * calculation_to_unit} {name_of_unit}")
# print(f"35 days are {50 * calculation_to_unit} {name_of_unit}")
# print(f"35 days are {110 * calculation_to_unit} {name_of_unit}")

#########################################################################################
# FUNCTIONS
# How to introduce functions to make our code cleaner by removing further repetition in the code
# function is defined using "def" key word
# print(f"35 days are {35 * calculation_to_units} {name_of_unit}")---- this can be re-written as

# # These variables are defined outside the function
# calculation_to_units = 24
# name_of_unit = "hours"
#
#
#def days_to_units(num_of_days):
    #print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    # Alternatively
    #print(f"There are {num_of_days * calculation_to_units} {name_of_unit} in {num_of_days} days")
#
# # Enter the required numbers of days in the units below
#days_to_units(20)
# days_to_units(35)
# days_to_units(50)
# days_to_units(110)
