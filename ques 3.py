def num_atoms(g , w=196.97):
    L=g/w
    f=6.022*(10**23)
    atom=L*f
    return atom

atom=num_atoms(10,1.008)
print(atom)
