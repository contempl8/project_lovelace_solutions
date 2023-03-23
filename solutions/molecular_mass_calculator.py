import os
here=os.path.abspath(os.path.dirname(__file__))
data_dir=os.path.dirname(here)+'/data/'
os.chdir(data_dir)
import csv

with open('periodic_table.csv') as csvfile:
    periodic_table_reader = csv.reader(csvfile, delimiter=',')
    p_table={}
    for item in periodic_table_reader:
        p_table[item[0]]=item[1]


def molecular_mass(chemical_formula:str):
    mass = 0
    formula_list=list(chemical_formula)
    formula_list.reverse()
    mol={}
    build_mol,next_char='',''
    def append_mol(molecule):
        alpha,num='',''
        for i in molecule:
            if i.isalpha():
                alpha+=i
            elif i.isdigit():
                num+=i
        if alpha in mol.keys():
            if num == '': num = '1'
            mol[alpha]=str(int(mol[alpha])+int(num))
        else:
            mol[alpha]=num
        return ''
    while len(formula_list):
        build_mol+=formula_list.pop()
        if len(formula_list):
            next_char=formula_list[-1]
        if not next_char.isupper():
            next_char=formula_list.pop()
            while not next_char.isupper():
                if not len(formula_list):
                    build_mol+=next_char
                    build_mol=append_mol(build_mol)
                    break
                build_mol+=next_char
                next_char=formula_list.pop()
            if not len(build_mol):
                pass
            else:
                formula_list.append(next_char)
                build_mol=append_mol(build_mol)
        elif next_char.isupper():
            build_mol=append_mol(build_mol)
    for element,num in mol.items():
        if num =='': num = '1'
        mass+=float(p_table[element])*int(num)
    return mass

print(molecular_mass('Pa'))
print(molecular_mass('OCS'))
print(molecular_mass('C4H4AsH'))
print(molecular_mass('C20H25N3O'))