import pandas as pd

data = pd.read_csv('dz.csv')
df = pd.DataFrame(data)

#print(df.info())

print(df)
#Выводим среднее значение зарплаты по городу
group = df.groupby('City')['Salary'].mean()

#Заполняем пропущенные значения средним по городу
#df['Salary'] = df['Salary'].fillna(df.groupby('City')['Salary'].transform('mean'))

df['Salary'] = df['Salary'].fillna(group)

#Удаляем строки, с пропущенным значением города, чтобы они не учитывались в подсчетах
df.dropna(inplace = True)

print(df)
print(group)
