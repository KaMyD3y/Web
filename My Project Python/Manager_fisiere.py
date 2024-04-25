# Planificare și Design
# Definirea funcționalităților cheie: căutare, sortare, organizare.
# Stabilirea structurii de directoare și tipurilor de date necesare pentru gestionarea fișierelor.
# Setarea Mediului de Lucru
# Crearea unui mediu virtual folosind venv.
# Instalarea bibliotecilor necesare, cum ar fi os și shutil, care sunt incluse în standard library și nu necesită instalări adiționale.
# Dezvoltarea Logică
# Implementarea funcțiilor pentru căutarea fișierelor bazată pe diferite criterii.
# Scrierea algoritmilor de sortare și de organizare a fișierelor în directoare.
# Testarea și debugging-ul codului pentru a asigura funcționalitatea corectă.

# file_manager.py: Modulul care conține logica pentru gestionarea fișierelor, inclusiv căutarea, sortarea și organizarea.
# config_manager.py: Modulul pentru salvarea și încărcarea configurațiilor sau structurilor de dosare folosind json.

a=int(input())
s=int(input())
d=int(input())
for i in range(a+1):
    for j in range(s+1):
        for k in range(d+1):
            m=i,j,k
            print(m)
            