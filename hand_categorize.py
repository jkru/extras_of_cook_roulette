
in_file = open('indexedingredients.lst', 'r')
out_file = open('extracategories.lst', 'w')

for line in in_file:
    line = line.split()
    print line
    food_type = raw_input()
    if food_type == 'v':
        out_file.write(line[0]+" "+line[1]+" "+line[2]+" vegetable\n")
    elif food_type == 'p':
        out_file.write(line[0]+" "+line[1]+" "+line[2]+" protein\n")
    elif food_type =='s':
        out_file.write(line[0]+" "+line[1]+" "+line[2]+" starch\n")
    elif food_type =='h':
        out_file.write(line[0]+" "+line[1]+" "+line[2]+" herbspice\n")
    elif food_type =='a':
        out_file.write(line[0]+" "+line[1]+" "+line[2]+" fat\n")
    elif food_type =='f':
        out_file.write(line[0]+" "+line[1]+" "+line[2]+" fruit\n")
    elif food_type =='l':
        out_file.write(line[0]+" "+line[1]+" "+line[2]+" liquid\n")
    elif food_type == "":
        out_file.write(line[0]+" "+line[1]+" "+line[2])
    else:
        out_file.write(line[0]+" "+line[1]+" "+line[2]+" FIXME")

