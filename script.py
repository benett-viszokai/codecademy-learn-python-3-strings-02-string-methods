# Original string
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# Splitting by commas
highlighted_poems_list = highlighted_poems.split(',')

# Stripping the whitespaces
highlighted_poems_stripped = []
for poems in highlighted_poems_list:
  highlighted_poems_stripped.append(poems.strip())

# Splitting the list into sublists
highlighted_poems_details = []
for detail in highlighted_poems_stripped:
  highlighted_poems_details.append(detail.split(':'))

# Creating the separated lists
titles = []
poets = []
dates = []

for det in highlighted_poems_details:
  titles.append(det[0])
  poets.append(det[1])
  dates.append(det[2])

# Printing out using .format()
for i in range(len(highlighted_poems_details)):
  print("The poem {} was published by {} in {}.".format(titles[i], poets[i], dates[i]))
