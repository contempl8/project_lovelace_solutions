any_=["G","U","A","C"]
UC=["U","C"]
AG=["A","G"]
stop_codons=["UAA","UAG","UGA"]
C_yel = any_
U_green = any_
A_red = any_
G_blue = any_
codons = dict(G=dict(U=[any_+['Val']],
                      C=[any_+['Ala']],
                      G=[any_+['Gly']],
                      A=[UC+["Asp"],AG+["Glu"]]),
            U=dict(U=[UC+["Phe"],AG+["Leu"]],
                   C=[any_+["Ser"]],
                   A=[UC+["Tyr"]],
                   G=[UC+["Cys"],["G","Trp"]]),
            C=dict(G=[any_+["Arg"]],
                   U=[any_+["Leu"]],
                   C=[any_+['Pro']],
                   A=[UC+["His"],AG+["Gln"]]),
            A=dict(C=[any_+["Thr"]],
                   G=[AG+["Arg"],UC+["Ser"]],
                   A=[AG+["Lys"],UC+["Asn"]],
                   U=[["G","Met"],["U","A","C","Ile"]]))

def amino_acid_sequence(rna_string):
    amino_acids = []
    for i in range(0,len(rna_string),3):
        rna=rna_string[i:i+3]
        if rna in stop_codons:
            return "".join(amino_acids)
        for k,v in codons.items():
            if rna[0] == k:
                for k,v in v.items():
                    if rna[1] == k:
                        for l in v:
                            if rna[2] in l:
                                amino_acids.extend(l[-1:])

    return "".join(amino_acids)

print(amino_acid_sequence("GAAUAGGUA"))
print(amino_acid_sequence("CCU"))
print(amino_acid_sequence("AUGCCAAAGGGUUGA"))
print(amino_acid_sequence("GCAAGAGAUAAUUGU"))