from datapackage import Package

package = Package('https://datahub.io/core/global-temp/datapackage.json')

# print list of all resources:
print(package.resource_names)

# print processed tabular data (if exists any)
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        print(resource.read())
# %%
#retrieve only annual_csv and data from GCAG
annual_csv = package.get_resource('annual_csv').read()        
annual_GISTEMP = annual_csv[1::2]
print(annual_GISTEMP)

# %%
#sort data separately into year and temp lists
year = []
temp = []
for i in annual_GISTEMP:
    year.append(i[1])
    temp.append(float(i[2]))
# %%
# plot scatter chart
import numpy
import matplotlib.pyplot as plt

plt.scatter(year, temp)
plt.show()
# %%
# plot polynomial regression chart
mymodel = numpy.poly1d(numpy.polyfit(year, temp, 3))
myline = numpy.linspace(1880, 2100)
plt.scatter(year, temp)
plt.plot(myline, mymodel(myline))
plt.show()
# %%
# predict temp in year 2030
#from scipy import stats

#slope, intercept, r, p, std_err = stats.linregress(year, temp)

#def myfunc(year):
#    return slope * year + intercept

#prediction = myfunc(2050)
#print(prediction)