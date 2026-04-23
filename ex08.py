#Constants
W = 75
G = 112
#User Input
OW = int(input("Enter the Number of Widgets Ordered: "))
OG = int(input("Enter the Number of Gizmos Ordered: "))
#Calculations
Total_WeightW = OW * W
Total_WeightG = OG * G
Total_Weight = Total_WeightW + Total_WeightG
#Output
print (f"\nTotal weight of Widgets: {Total_WeightW} grams")
print (f"Total weight of Gizmos: {Total_WeightG} grams")  
print (f"Total weight of the order: {Total_Weight} grams")