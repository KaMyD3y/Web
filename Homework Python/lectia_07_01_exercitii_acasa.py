import json

if __name__ == "__main__":
    print("Bun venit la tema 07.01 - pip, venv, request")

    # ================== PIP, VENV, REQUESTS ==================
    # ------------------ Exercițiul 1 ------------------
    """
    Exercițiul 1: Afișarea Știrilor Principale de la Hacker News
    Descrierea Exercițiului:
    Scopul acestui exercițiu este de a crea un script Python care interoghează Hacker News API pentru a afișa titlurile
     și linkurile către primele 5 știri principale. 
    
    Instrucțiuni:
    - Utilizează biblioteca requests pentru a face o cerere GET la endpoint-ul API care oferă identificatorii (ID-uri) 
    pentru top știri (Top Stories).
    - Extrage primele 5 ID-uri din răspunsul JSON primit.
    - Pentru fiecare ID, efectuează o cerere GET suplimentară pentru a obține detalii despre știre, inclusiv titlul și 
    URL-ul.
    - Afișează titlurile și URL-urile în consolă, permițând utilizatorilor să acceseze direct știrile.
    
    Hint-uri pentru Lucrul cu Răspunsul API:
    
    - Răspunsul inițial pentru top știri va fi o listă de ID-uri în format JSON. Aceste ID-uri reprezintă știrile 
    individuale.
    - Pentru a accesa detalii despre o știre specifică, va trebui să faci o cerere GET folosind ID-ul respectiv la 
    endpoint-ul de item, de exemplu: https://hacker-news.firebaseio.com/v0/item/{id}.json.
    - Răspunsul pentru o știre individuală va include diverse câmpuri, dintre care title (titlul știrii) și url 
    (link-ul către știre) sunt de interes pentru acest exercițiu.
    """


