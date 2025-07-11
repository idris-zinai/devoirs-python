grades_data = """Alice,85,90,78
Bob,72,68,80
Charlie,95,100,92
Diana,50,60,55
Evan,88,79,84"""

with open("grades.csv", "w") as f:
    f.write(grades_data)

with open("grades.csv", "r") as f:
    lines = f.readlines()

print("=== Contenu du fichier grades.csv ===")
for line in lines:
    print(line.strip())
    
results = []

for line in lines:
    line = line.strip()
    data = line.split(',')
    name = data[0]
    scores = list(map(float, data[1:]))
    average = sum(scores) / len(scores)
    status = "Pass" if average >= 50 else "Fail"
    results.append([name, round(average, 2), status])
    
with open("averages.csv", "w") as f:
    f.write("StudentName,Average,Pass\n")
    for result in results:
        f.write(f"{result[0]},{result[1]},{result[2]}\n")

print("\n=== Résultats calculés ===")
print("Nom\t\tMoyenne\t\tStatut")
print("-" * 35)
for result in results:
    print(f"{result[0]}\t\t{result[1]}\t\t{result[2]}")
