#*********************************************#
#=======> appliction Gestion Note d Formation 
#********************************************#

#-- obj 
Nom_Eleve=[]
Formations=["php","js","html","python"]
Notes=[]
Note_Moyenne=[]
# message pour  NBR  eleves 

Nbr=int(input("Donner Nbr votre eleve : "))


# message pour demande le nom de eleve
for NbrNom in range(Nbr):
    Nom=input("Nom de eleve " + str(NbrNom+1) + ": " )
    Nom_Eleve.append(Nom)

# demande le note de eleve
for i in range(Nbr):
    NoteFormation=[]
    #  boucle in Nom_Eleve:
    print(f"===> les Note de eleve  "+ str(i+1) + " :")

    for j in range(len(Formations)):
        Note_Formation=float(input("Note de Foramation " + Formations[j] + " : "))
        NoteFormation.append(Note_Formation)
        
    Notes.append(NoteFormation)

    
#  note de chaque eleve 

for nnt in Notes:
    note_moyenne=sum(nnt)/len(Formations)
    Note_Moyenne.append(note_moyenne)

i = 0
for jj in Nom_Eleve:
    print(f"===> Note  de eleve  {jj} :  {Note_Moyenne[i]}")
    i=i+1
