students = [
    ["Ploy", [80, 75, 90]],
    ["Bank", [40, 50, 60]],
    ["Mind", [95, 88, 92]],
    ["Ton", [30, 45, 20]],
]

log_flag = False
pass_count = 0
highest_avg = 0
highest_name = ""

for student in students:
    name = student[0]
    scores = student[1]
    total = 0
    for s in scores:
        total = total + s
    avg = total / len(scores)

    if avg >= 50:                 # fix 1: was > 50
        pass_count = pass_count + 1

    if avg > highest_avg:
        highest_avg = avg
        highest_name = name       # fix 2: was student

record = []
for i in range(len(students)):
    record.append(students[i][0])  # fix 3: was record[i] = ...

print("Students passed:", pass_count)
print("Top student:", highest_name, "with average", highest_avg)
print("All students:", record)
