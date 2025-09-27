#Calculate thr area of the room and how mach pric

print("Hi and wellcome to the Gotland.com")
str_length=input("Please type length:\n")
Str_width=input("please type width:\n")
length=float(str_length.replace(",","."))
width=float(Str_width.replace(",","."))
area=length*width
str_area=str(area)

str_meter=input("How much for 1 meter?\n")
meter=float(str_meter.replace(",","."))
str_meter=str(meter)

print("the total area is: " + str(area))

total=float(int(area) * float(int(meter)))
str_total=str(total)

print("give the guy: " + str (total) + " $")
