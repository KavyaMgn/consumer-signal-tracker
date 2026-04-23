from pytrends.request import TrendReq
import pandas as pd
import time

# Initialize
pytrends = TrendReq(hl='en-US', tz=360)

# Keywords that signal consumer stress around DoorDash
keywords = [
    "cancel doordash",
    "doordash too expensive",
    "doordash not worth it",
    "doordash subscription cancel",
    "doordash promo not working",
    "switch to uber eats"
]

print("Pulling Google Trends data...")

all_data = []

for keyword in keywords:
    pytrends.build_payload(
        [keyword],
        cat=0,
        timeframe='today 12-m',  # last 12 months
        geo='US'
    )
    data = pytrends.interest_over_time()
    
    if not data.empty:
        data = data.drop(columns=['isPartial'])
        data.columns = ['interest']
        data['keyword'] = keyword
        all_data.append(data)
        print(f"✓ Got data for: {keyword}")
    else:
        print(f"✗ No data for: {keyword}")
    
    time.sleep(2)  # be polite to Google's servers

# Combine all
df = pd.concat(all_data)
df.reset_index(inplace=True)
df.rename(columns={'date': 'week'}, inplace=True)

# Save
df.to_csv('data/trends_raw.csv', index=False)
print("\n✅ Done. Saved to data/trends_raw.csv")
print(df.tail(10))