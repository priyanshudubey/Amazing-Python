#Priyanshu Dubey
#Covid Report
# This will tell you all the stats of the country 
#install covid library first by "pip install covid"


from covid import Covid
covid = Covid()
cntry = input("Enter the country name: ")
cases = covid.get_status_by_country_name(cntry)
for i in cases:
    print(i, " ; ",cases[i])
