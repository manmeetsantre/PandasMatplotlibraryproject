import pandas as pd
import matplotlib.pyplot as pl

data = {
    'Name': ['Rohan', 'Mohit', 'Aryan', 'Adi', 'Madhav'],
    'Div': [4, 7, 6, 5, 3],
    'Points': [54, 77, 45, 90, 89]
}

df = pd.DataFrame(data)

print("Dataframe:")
print(df)

avg = df['Points'].mean()
print("\nAvg Points:", avg)

dataf = df[df['Points'] > avg]

print("\nStudents with Points above avg:")
print(dataf)

pl.figure(figsize=(8, 6))
pl.scatter(df['Div'], df['Points'], color='red', label='Cadets')
pl.title('Div vs Points')
pl.xlabel('Div')
pl.ylabel('Points')
pl.grid(True)
pl.legend()
pl.show()