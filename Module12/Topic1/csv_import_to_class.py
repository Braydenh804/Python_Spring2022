import csv
from Module12.Topic1.county_info import CountyInfo

with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    county = {}
    for row in csv_reader:
        # skip the first line in the file because it is the header
        if line_count == 0:
            line_count += 1
            continue
        if row[0] == "":
            line_count += 1
            continue
        # create an item in dictionary county with a key of the county name and a value of the object
        county[str(row[1])] = CountyInfo(row[2], row[3], row[4], row[5], row[6])


def average_pop_per_household(county_name):
    average = int(county[county_name].population.replace(",", "")) / int(
        county[county_name].household_num.replace(",", ""))
    rounded_average = round(average, 2)
    return 'The Average Population Per Household in ' + county_name + ' County Is: ' + str(rounded_average) + ' People'


def iowa_total_pop():
    pop_sum = 0
    for key in county:
        pop_sum += int(county[key].population.replace(',', ''))
    return "Iowas Current Total Population Is " + str(pop_sum) + " People"


if __name__ == '__main__':
    print(average_pop_per_household('Dallas'))
    print(iowa_total_pop())
