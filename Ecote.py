import re

input = "input.cpp"
output = "output.txt"

## LISTS:

vartypes = ["char", "int", "float", "double", "short", "long", "unsigned ", "string", "bool"]  ## list for allowed types of variables
types = [] ## for variables types
variables = [] ## for variables without types
varcounter = [] ## for counting how many times variable was used
linescounter = [] ## for counting lines
samenames = [] ## same names variables
samenameslines = [] ## same names variables lines 
samenamestypes = [] ## same names variables types


def unused_variables(input_txt, output_txt):  ## first and main function, oparating on input code and creating output txt
    with open(input_txt) as datafile:
        in_comment=0     # flag for checking if line is commented
        counter=1           # counter for lines
        for line in datafile:
            line = line.strip()
            in_comment = skip1(line, in_comment, counter)
            counter+=1
    with open(input_txt) as datafile:  ## opening 2nd time, because now programm has to search for matching names, input was not modified
        for line in datafile:
            line = line.strip()
            in_comment = skip2(line, in_comment)

    same_name_counter=0   ## counter for same name variables, it is not allowed by assumption  

    same_names(line, same_name_counter)

    print("List of types of variables:")
    print(types)
    print("\nList of variables:")
    print(variables)
    print("\nCounter for each variable:")
    print(varcounter)
    print("\nCounter for lines, line of declaration of each variable:")
    print(linescounter)
    print("\nWARNING")
    print("\nVariables declared more than once:")
    print (samenames)
    print("\nLines of variables declared more than once:")
    print (samenameslines)
    print("\nTypes of variables declared more than once:")
    print (samenamestypes)


    with open(output, 'w') as file:
        for x in range(types.__len__()):
            if varcounter[x]==1:
                file.write("Variable {var} declared in Line: {line} is never used.\n".format(line=linescounter[x],var=variables[x]))


def skip1(line,in_comment,counter):   ## function for detecting if declaration is in "" or in comments 
    if '"' in line:
        tmp = line[line.index('"')+1:len(line)]
        tmp = tmp[tmp.index('"')+1:len(tmp)]
        line = line [0:line.index('"')] + tmp
    if "//" in line:
        line = line[0:line.index("//")]
        search_var(line,counter)
    elif "/*" in line:
        if "*/" not in line:
            in_comment = 1
        line = line[0:line.index("/*")]
        search_var(line,counter)
    elif "*/" in line:
        in_comment = 0
        line = line[line.index("*/")+2:len(line)]
        search_var(line,counter)
    elif in_comment == 0:
        search_var(line,counter)
    return in_comment

def skip2(line,in_comment): ## mostly the same function as skip1 but this time only for names of detected variables
    if '"' in line:
        tmp = line[line.index('"')+1:len(line)]
        tmp = tmp[tmp.index('"')+1:len(tmp)]
        line = line [0:line.index('"')] + tmp
    if "//" in line:
        line = line[0:line.index("//")]
        if_unused(line)
    elif "/*" in line:
        if "*/" not in line:
            in_comment = 1
        line = line[0:line.index("/*")]
        if_unused(line)
    elif "*/" in line:
        in_comment = 0
        line = line[line.index("*/")+2:len(line)]
        if_unused(line)
    elif in_comment == 0:
        if_unused(line)
    return in_comment



def search_var(line,counter): ## function searching for variables, looking for declared types like int, float etc
    for x in range(vartypes.__len__()):
        regex = r"({var})\s+([a-zA-Z0-9,]+)\s*([,;)]+)".format(var=vartypes[x])
        matches = re.finditer(regex, line, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            types.append(match.group(1))
            variables.append(match.group(2))
            varcounter.append(0)
            linescounter.append(counter)

        regex = r"({var})\s+([a-zA-Z0-9,]+)\s*([=]+)\s*([a-zA-Z0-9 \"']*)([;]+)".format(var=vartypes[x]) ## regex for variables declared with assignings like: int a = 10
        matches = re.finditer(regex, line, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            types.append(match.group(1))
            variables.append(match.group(2))
            varcounter.append(0)
            linescounter.append(counter)

def if_unused(line):  ## function which checks if variable was used (has been detected more than only with declaration)
    for x in range(variables.__len__()):
        regex = r"[\W]({varname})[\W]".format(varname=variables[x])       ## case when variable is not the first from the left  
        matches = re.finditer(regex, line, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            varcounter[x]+=1

        regex = r"^[\W]*({varname})[\W]".format(varname=variables[x])     ## case when variable is the first from the left   
        matches = re.finditer(regex, line, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            varcounter[x]+=1

def same_names(line, same_name_counter): ## function checking if names of variables are repeating and giving information where exatcly are same named variables
    for x in range(variables.__len__()):
        for y in range(variables.__len__()):
            if variables[x] == variables[y]:
                    same_name_counter += 1
        if same_name_counter > 1:
            line=linescounter[x]
            samenames.append(variables[x])
            samenameslines.append(line)
            samenamestypes.append(types[x])
        same_name_counter = 0


if __name__ == "__main__":
    unused_variables(input, output)
