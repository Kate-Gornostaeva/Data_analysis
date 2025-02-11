import pandas as pd

data = pd.read_csv('Class_ratings.csv')

df = pd.DataFrame(data)

print(df.head())

print(df.describe())

subject_columns = df.columns[2:]

average_marks = df[subject_columns].mean().round(2)

median_marks = df[subject_columns].median().round(2)

std_marks = df[subject_columns].std().round(2)


print("Средние оценки по предметам:")
print(average_marks)

print("Медианные оценки по предметам:")
print(median_marks)

print("Стандартные отклонения по предметам:")
print(std_marks)

Q1_math = df['Математика'].quantile(0.25)

Q3_math = df['Математика'].quantile(0.75)

IQR_math = Q3_math - Q1_math

print("Межквартальный размах по предмету Математика:", IQR_math)









