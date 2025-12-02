templs  = {
  "t021225":{"P-S":9421, "O-S":7880, "P-M":6202, "O-M":5934, "P:V":2496},
  "t011225":{"P-S":9788, "O-S":8537, "P-M":6481, "O-M":6177, "P:V":2496},
  "t301125":{"P-S":9520, "O-S":10199, "P-M":6889, "O-M":7927, "P:V":2496},
  "t291125":{"P-S":7945, "O-S":7597, "P-M":6022, "O-M":6723, "P:V":2496},
  "t281125":{"P-S":9119, "O-S":8779, "P-M":5819, "O-M":5978, "P:V":2496},
  "t271125":{"P-S":8715, "O-S":8211, "P-M":6435, "O-M":6143, "P:V":2496},
  "t261125":{"P-S":9269, "O-S":9118, "P-M":6388, "O-M":6792, "P:V":2496}
}

directions = list(templs["t021225"].keys())

ps = 100
os = 10000
pm = 1000
om = 1000
pv = 0

new_plan_dict = {"P-S":ps, "O-S":os, 
                 "P-M":pm, "O-M":om, 
                 "P:V":pv}
templ_list = list(templs.keys())

for i in directions:
  for j in templ_list.copy():
    counter = 0
    if templs[j][i] < new_plan_dict[i]:
      templ_list.remove(j)
    
sum_dict = {}

if len(templ_list) == 0:
  print("нет подходящих шаблонов")
else:
  for i in templ_list:
    sum_of_direction = 0
    for j in directions:
      sum_of_direction += templs[i][j]
    sum_dict[i] = sum_of_direction
  min_val = min(sum_dict.values())
  result_templs = []
  
  for key in sum_dict:
    if sum_dict[key] == min_val:
      result_templs.append(key)
      
  print(result_templs)  

