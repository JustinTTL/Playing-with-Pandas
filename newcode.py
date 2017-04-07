# We Need More Lemon Pledge!
countries_filter = pd.read_csv("data/countries.csv",usecols=['English Name'])
countries_filter = countries_filter['English Name'].unique()
df = df[df['country'].apply(lambda x: x in countries_filter)]
df.info()