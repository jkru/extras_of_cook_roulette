
in_file = open('ingredient_categories.txt', 'r')
out_file = open('categorized.lst', 'w')

for line in in_file:
    line = line.split()
    print line
    food_type = raw_input()
    if food_type == 'v':
        out_file.write(line[0]+" vegetable")
    elif food_type == 'p':
        out_file.write(line[0]+" protein")
    elif food_type =='s':
        out_file.write(line[0]+" starch")
    else:
        out_file.write(line[0]+" FIXME")

