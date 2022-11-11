#*********************************************#
#=======> appliction Gestion Note d Formation 
#********************************************#

#-- obj 
Nom_Eleve=[]
Nom_Formations=[]
Notes=[]
Note_Moyenne=[]

# metheod tri note 
def tri_Note_Moyenne(tab):

   for i in range(len(tab)):

      # Trouver le note max
       max = i

       for j in range(i+1, len(tab)):
           if tab[max] < tab[j]:
               max = j
                
       tmp = tab[i]
       tab[i] = tab[max]
       tab[max] = tmp

   return tab

# message pour  NBR  eleves  est Formations
Nbr_elev=int(input("Donner Nbr votre eleve : "))
Nbr_Forma=int(input("Donner Nbr votre Formations : "))


# message pour demande le nom de eleve
for NbrNom in range(Nbr_elev):
    Nom=input("Nom de eleve " + str(NbrNom+1) + ": " )
    Nom_Eleve.append(Nom)

# message pour demande le nom de Formations
for NbrFor in range(Nbr_Forma):
    forma=input("Nom de Formation  " + str(NbrFor+1) + ": " )
    Nom_Formations.append(forma)
print ("---------------------------------------------------")
# demande le note de eleve
for i in range(Nbr_elev):
    NoteFormation=[]
    #  boucle in Nom_Eleve:
    print(f"===> les Note de eleve  "+ str(i+1) + " :")

    for j in range(len(Nom_Formations)):
        Note_Formation=float(input("Note de Foramation " + Nom_Formations[j] + " : "))
        NoteFormation.append(Note_Formation)
        
    Notes.append(NoteFormation)

    
#  note de chaque eleve 
print ("---------------------------------------------------")
for nnt in Notes:
    note_moyenne=sum(nnt)/len(Nom_Formations)
    Note_Moyenne.append(note_moyenne)
i = 0
for jj in Nom_Eleve:
    print(f"===> Note  de eleve  {jj} :  {Note_Moyenne[i]}")
    i=i+1
    
## declaer funtion tri  Note_Moyenne
tri_Note_Moyenne(Note_Moyenne)
ii=0
print ("---------------------------------------------------")

print ("Le Note_Moyenne  des eleve trié par decoicent")
print(f"*** Eleve|Note|Note *****")
iii=0
NbrEtudiantNonAdmis=0
NbrEtudiantAdmis=0
for jj in Nom_Eleve:
    if(Note_Moyenne[iii] < 10):
        etudiantNonAdmis = "nom admin"
        NbrEtudiantNonAdmis=NbrEtudiantNonAdmis+1
        print(f"===> Eleve  {jj} : | {Note_Moyenne[iii]} | {etudiantNonAdmis} ")
    else:
        etudiantAdmis ="admin"
        print(f"{jj}|{Note_Moyenne[iii]}|{etudiantAdmis}")
        NbrEtudiantAdmis=NbrEtudiantAdmis+1
    iii=iii+1

# affiche nbr eleve admin et non admin
print ("---------------------------------------------------")
print ("nbr des eleve Admin et Non Admin")
print(f"NBr des eleve admin : {NbrEtudiantAdmis}/{iii}")
print(f"NBr des eleve Non admin : {NbrEtudiantNonAdmis}/{iii}")