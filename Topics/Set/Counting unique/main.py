students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

different_subjects = set(Belov + Smith + Sarada)
print(len(different_subjects))
