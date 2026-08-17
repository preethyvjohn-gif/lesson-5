print("=== Smart school Day planner ===")
print("awnser 3 quick questions and I will plan your day!\n")
day       =input("what day is it?  (Monday to Sunday): ").strip().capitalize()
weather   =input("What is the weather? (sunny/rainy/cloudy): ").strip().lower()
homework  =input("is your homework done?  (yes/no: ").strip().lower()


print()
print(f"=== your Plan for {day} ===")
print("-" * 35)


if day in ("Saturday", "Sunday"):
    print("Day type     : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type    : first day of the week. Pack your weekly planner.")
elif day == "Friday":
    print("Day type    : Last school day. return libary books today.")
elif day in ("Tuesday", "Wendesday", "thursday"):
    print("Day type    : Rugular school day. Stay focused!")
else:
    print("Day type    : Day not reconginsed please check the spelling.")

if weather == "sunny" and homework == "yes":
    print("After school: Head to the park - great weather and weather and homework is done!")

if weather == "rainy" or weather == "cloudy":
    print("Weather tip : pack your Umbrella - it may get wet outside.")

if not (homework == "yes"):
    print("Homework     : Not done yet. Finish it before going out!")

if weather == "rainy" and not (homework == "yes"):
    print("Best plan    : Stay in, finnish homework, and then watch your favourite show.")
elif day in("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : perfect weekend weather - head outside and have some fun!")
else:
    print("Best plan   : Take it one step at a time - you have got this!")
print()
print("plan complete! have a wonderful day")
    


