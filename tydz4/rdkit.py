#zad rdkit
#libs
from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt

# CCCCCCC - heptan
heptan = Chem.MolFromSmiles('CCCCCCC')
heptan_img = Draw.MolToImage(heptan)

# heptan_img.show()

#C1CCC1 - cyklopropan

cyclopropane = Chem.MolFromSmiles('C1CC1')
cyclopropane_img = Draw.MolToImage(cyclopropane)

# cyclopropane_img.show()

#CC(=O)CC - kwas propanowy

propanoic_acid = Chem.MolFromSmiles('CC(=O)CC')
propanoic_acid_img = Draw.MolToImage(propanoic_acid)

# propanoic_acid_img.show()
# plt.show()

#CCCCCCCC - oktan

octan = Chem.MolFromSmiles('CCCCCCCC')
octan_img = Draw.MolToImage(octan)

octan_img.show()

#CCCC1CC1 - some_molecule

some_molecule = Chem.MolFromSmiles('CCCC1CC1')
some_molecule_img = Draw.MolToImage(some_molecule)

# some_molecule_img.show()

#LUB PROŚCIEJ

molecules = ['CCCCCCC', 'C1CC1', 'CC(=O)CC', 'CCCCCCCC', 'CCCC1CC1']

for molecule in molecules:
    molecule_in_mol = []
    molecule_to_mol = Chem.MolFromSmiles(molecule)
    molecule_in_mol.append(molecule_to_mol)
    for mol in molecule_in_mol:
        draw_molecule = Draw.MolToImage(mol)
        draw_molecule.show()


    