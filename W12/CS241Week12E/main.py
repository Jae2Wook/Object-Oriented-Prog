import pandas
import matplotlib.pyplot as plt

# Read movies data into a dataframe
data = pandas.read_csv("movies.csv")

# Print out columns
print(data.columns)
print("Movie Length mean: {}" .format(data.length.mean()))
print("Voter Rating median: {}" .format(data.rating.median()))
print()

# Get the Year of the First PG Movie
data.mpaa = data.mpaa.apply(lambda x : x.strip())
print(data[data.mpaa == "PG"].sort_values(by = "year"))
print(data[data.mpaa == "PG"].year.min())
# Plot graph of all movies by MPAA ratings
data_mpaa_count = data[data.mpaa != ""].mpaa.value_counts().sort_index()
print(data_mapp_count)
data_mpaa_count.plot(kind = "bar", title = "Movies by mpaa rating", rot = 0)
plt.show()
#plt.savefig("graph1.png")
print()

# Find the average budget Action Movies
subset = data[["budget", "Action"]]
subset_action = subset[subset.Action == 1]
abg = subset_action.budget.mean()
print(subset_action)
print(avg)
print()

# Find the non-short movie with the highest cost per minute
data["CostPerMinite"] = data.budget / data.length
result = data[data.Short == 0].sort_values(by = "CostPerMinute", ascending = False)
print(result)
print(result.iloc[0])

# Find trends in movie ratings
#pg_per_year = data[data.mpaa == "PG"].year.value_counts()
pg_per_year = data[data.mpaa == "PG"].groupby("year").size()
print(pg_per_year)

rating_per_year = {}
for rating in ["PG", "PG-13", "R", "NC-17"]:
rating_per_year[rating] = data[data.mpaa == rating].year.value_counts()
print(rating_per_year)

df = pandas.DataFrame(rating_per_year)
df = df.fillna(0)
print(df)

df[df.index > 1980].plot(kind = "line", title = "Ratings per year")
plt.show()



