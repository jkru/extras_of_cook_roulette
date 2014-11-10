f = open('trunc_100_unindexedrecipes.txt','r')
g = open('shortformattedforclusters.txt','w')
g.write("index ")
all_foods = []
l = 0
for item in f:
    item = item.split()
    for afood in item:
        if afood not in all_foods:
            all_foods.append(afood)
        
f.close()


for food in all_foods:
    g.write(str(food)+str(" "))
g.write("\n")


f = open('trunc_100_unindexedrecipes.txt','r')
for j, items in enumerate(f):
    g.write(str(j)+" ")
    items = items.split()
    items = list(items)
    temp_list = []
    for k in range(len(all_foods)):
        temp_list.append(0)
    for k, nextfood in enumerate(items):
        pos = all_foods.index(nextfood)
        temp_list[pos] = 1
    for entry in temp_list:
        g.write(str(entry)+" ")
    g.write("\n")

print all_foods
