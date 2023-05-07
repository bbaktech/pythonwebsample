import matplotlib.pyplot as plt


print("A Simple Data Analysis Program")
print()

emission_dict = {}

with open('Emissions.csv', 'r') as file:
    for data in file.read().split('\n'):
        emission_dict.update({data.split(',')[0]: data.split(',')[1:]})

print("All data from Emissions.csv has been read into a dictionary.", end="\n\n")

#print (emission_dict.keys())

input_year = input("Select a year to find statistics (1997 to 2010): ")

index_of = int()
lines = []

for item in emission_dict.values():
    if input_year in item:
        index_of = (item.index(input_year))
        break

print(index_of)

total = 0
i = 0
emissions_in_year = []

for value in emission_dict.values():
    if i != 0:
        total += float(value[index_of])
        emissions_in_year.append(list(emission_dict.values())[i][index_of])
    i += 1

mxval = max(float(str_value) for str_value in emissions_in_year)
minval= min(float(str_value) for str_value in emissions_in_year)

print(mxval)
print(minval)

max_country_index = int(emissions_in_year.index(str(mxval)))
min_country_index = int(emissions_in_year.index(str(minval)))
average_emissions = total / 195

max_emission = list(emission_dict.keys())[max_country_index + 1]
min_emission = list(emission_dict.keys())[min_country_index + 1]

print(f'In {input_year}, countries with minimum and maximum CO2 emission levels were: [{min_emission}] '
      f'and [{max_emission}] respectively.')

print(f'Average CO2 emissions in {input_year} were {"%.6f" % round(average_emissions, 6)}')
print()

"""
Step 1: Take the input from user to visualize data
"""
visualize_country = input("Select the country to visualize: ")

"""
Step 2: Getting the index of Country and passing it to plot function, Setting the Title and Label of Plot
"""
# From user entered value we extracted the Index value of country
number = list(emission_dict.keys()).index(visualize_country)
# Passed that index value to matplotlib plot function. As x value we passed years and as y value we passed emission value

#list(emission_dict.values())[0] has list of yers
#emission_dict.values())[number] has the list of valuse for corresponding year

plt.plot(list(map(float, list(emission_dict.values())[0])),
         list(map(float, list(emission_dict.values())[number])))
# Given the Title and Lable to Plot
plt.title("Year vs Emissions in Capita")
plt.xlabel("Year")
plt.ylabel("Emissions in " + visualize_country.title())
plt.show()
print()
