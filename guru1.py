#import necessary modules
import csv
import matplotlib.pyplot as plt
reader = csv.DictReader(open("C:\core-python-samples\sample1\Emissions.csv"))
list_dist = list(reader)

input_nation = input("Select a Country to  draw graph (1997 to 2010): ")
index_of_year  = None

for dist in list_dist:
    if dist.get('CO2 per capita') == input_nation:
        print (dist.items())
        selected_item = dist.items()
        break

# Passed that index value to matplotlib plot function. As x value we passed years and as y value we passed emission value
f = True
en_year = []
en_value = []

for i in selected_item:
    if f:
        f = False
        plt.title("Year vs Emissions in Capita")
        plt.xlabel("Year")
        plt.ylabel("Emissions in " + input_nation )
    else:
        en_year.append(i[0])
        en_value.append(float( i[1]))

plt.plot(en_year,en_value)
plt.show()
print()
