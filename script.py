# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def updateDamages(thing):
  freshDamages = []
  for i in thing:
    if i == "Damages not recorded":
      freshDamages.append(i);
    else:
      if "B" in i:
        x = float(i.strip("B")) * conversion["B"];
        freshDamages.append(x);
      elif "M" in i:
        x = float(i.strip("M")) * conversion["M"];
        freshDamages.append(x);
  return freshDamages        
  

# test function by updating damages
#print(damages)
ndamages = updateDamages(damages)

# 2 
# Create a Table
def hurricaneDict():
  table = {};
  for i in range(0, 34):
    table[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": ndamages[i], "Deaths": deaths[i]}
  return table
    
# Create and view the hurricanes dictionary
ntableHurricane = hurricaneDict()
#print(ntableHurricane)
# 3
# Organizing by Year
def OrganisedByYear(thisDict):
  table = {};
  for x in thisDict.keys():
    currentYear = thisDict[x]["Year"]    
    if thisDict[x]["Year"] not in table:
      table[currentYear] = []
      table[currentYear].append(thisDict[x])
    else:      
      table[currentYear].append(thisDict[x])
    
  return table
# create a new dictionary of hurricanes with year and key
obyHuricaneTable = OrganisedByYear(ntableHurricane)
#print(obyHuricaneTable[1932])

# 4
# Counting Damaged Areas
def countDamagedArea(areas):
  table = {}
  for area in areas.keys():
    areaList=areas[area]['Areas Affected']
    for x in areaList:
      
      if x in table:
        table[x] += 1
      else:
        table[x] = 1
  return table
# create dictionary of areas to store the number of hurricanes involved in
countAreas  = countDamagedArea(ntableHurricane)
#print(countAreas)
# 5 
# Calculating Maximum Hurricane Count
def maxHurricaneCount(thisDict):
  value = 0
  area = ''
  for x in thisDict.keys():
    if thisDict[x] >= value:
      value = thisDict[x]
      area = x
  return {area : value}

# find most frequently affected area and the number of hurricanes involved in
AreaHitMax = maxHurricaneCount(countAreas)
print(AreaHitMax)
# 6
# Calculating the Deadliest Hurricane
def deadliestHurricane(thisDict):
  Hurricane = ''
  deaths = 0
  for x in thisDict.keys():
    if thisDict[x]['Deaths'] > deaths:
      deaths = thisDict[x]['Deaths']
      Hurricane = x
  return {Hurricane : deaths}
# find highest mortality hurricane and the number of deaths
highestDeaths = deadliestHurricane(ntableHurricane)
print(highestDeaths)
# 7
# Rating Hurricanes by Mortality
def mortalityRating(thisDict):
  mortality_scale = {0:0, 1:100, 2:500, 3:1000, 4:10000}
  rating = {0:[], 1:[], 2:[], 3:[], 4:[]}
  for x in thisDict.keys():
    if thisDict[x]['Deaths'] < 100:
      rating[0].append(thisDict[x])
    elif thisDict[x]['Deaths'] >= 100 and thisDict[x]['Deaths'] < 500:
      rating[1].append(thisDict[x])
    elif thisDict[x]['Deaths'] >= 500 and thisDict[x]['Deaths'] < 1000:
      rating[2].append(thisDict[x])
    elif thisDict[x]['Deaths'] >= 1000 and thisDict[x]['Deaths'] < 10000:
      rating[3].append(thisDict[x])
    elif thisDict[x]['Deaths'] >= 10000:
      rating[4].append(thisDict[x])
  return rating
  
# categorize hurricanes in new dictionary with mortality severity as key
MortSeverity = mortalityRating(ntableHurricane)
#print(MortSeverity)
# 8 Calculating Hurricane Maximum Damage
def maxDamageHurricane(thisDict):
  Hurricane = ''
  damage = 0
  for x in thisDict.keys():
    if thisDict[x]['Damage'] == "Damages not recorded":
      pass
    elif thisDict[x]['Damage'] > damage:
      damage = thisDict[x]['Damage']
      Hurricane = x
  return {Hurricane : damage}
# find highest damage inducing hurricane and its total cost
maxDamHurr = maxDamageHurricane(ntableHurricane)
print(maxDamHurr)
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def damageRating(thisDict):
  rating ={0:[], 1:[], 2:[], 3:[], 4:[]}
  for x in thisDict.keys():
    if thisDict[x]['Damage'] == "Damages not recorded" or thisDict[x]['Damage'] < 100000000:
      rating[0].append(thisDict[x])
    elif thisDict[x]['Damage'] >= 100000000 and thisDict[x]['Damage'] < 1000000000:
      rating[1].append(thisDict[x])
    elif thisDict[x]['Damage'] >= 1000000000 and thisDict[x]['Damage'] < 10000000000:
      rating[2].append(thisDict[x])
    elif thisDict[x]['Damage'] >= 10000000000 and thisDict[x]['Damage'] < 50000000000:
      rating[3].append(thisDict[x])
    elif thisDict[x]['Damage'] >= 50000000000:
      rating[4].append(thisDict[x])
  return rating
  
# categorize hurricanes in new dictionary with damage severity as key
hurricanDamagesRated = damageRating(ntableHurricane)
print(hurricanDamagesRated)
