print ("Ratios are defined from Power/Dollar to calculate which method of getting energy would recieve most power per dollar ")
#Anish
#GROOT

power = [83333333333, 1250000, 16666666667, 250000000]
dollar = [200000, 1000000, 1000000, 7500000]
water_ratio = power[0]/ dollar[0]
wind_ratio = power[1]/ dollar[1]
nuclear_ratio= power[2]/ dollar[2]
solar_ratio = power[3]/ dollar[3]
print ("water ratio = " + str(water_ratio))
print ("wind ratio = " + str(wind_ratio))
print ("nuclear ratio = " + str(nuclear_ratio))
print ("solar ratio = " + str(solar_ratio))

best = sorted([water_ratio, wind_ratio, nuclear_ratio, solar_ratio], reverse=True)

print("THe winners are " + str(best))