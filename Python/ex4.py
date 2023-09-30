# 26/09/2023
# While, break, continue

print("========= Uso del break nel ciclo while =========")
counter_break = 0
while counter_break < 6:
  counter_break += 1
  if counter_break == 3:
    break
  print(counter_break)
print("====================================================")

#eq = "="
#print(49*eq)

print("")

print("========= Uso del continue nel ciclo while =========")
counter_continue = 0
while counter_continue < 6:
  counter_continue += 1
  if counter_continue == 3:
    continue
  print(counter_continue)
print("====================================================")