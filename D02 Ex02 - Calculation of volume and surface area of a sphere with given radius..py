pie = 3.14
radius = input("Input the radius of a sphere (in cm):")
Volume = (4/3) * pie * (int(radius)**3)
''' Volume = round(Volume) '''
Surface_area = 4 * pie * (int(radius)**2)
''' Surface_area = round(Surface_area) '''
print("Volume is "+ str(Volume) + " cm cube")
print("Surface area is "+ str(Surface_area) + " cm squr")
