import json

if __name__ == "__main__":
    print("Bun venit la tema 07.01 - pip, venv, request")

    # # ================== PIP, VENV, REQUESTS ==================
    # # ------------------ Exercițiul 0 ------------------
    # """
    # Exercițiul: Afișarea Informațiilor despre Rasele de Câini
    # Descrierea Exercițiului:
    # - Scopul acestui exercițiu este de a crea un script Python care interoghează Dog API pentru a afișa o listă de rase
    # de câini și, opțional, de a afișa o imagine aleatorie pentru o rasă specificată de utilizator.
    #
    # Instrucțiuni:
    # - Utilizează biblioteca requests pentru a face o cerere GET la endpoint-ul API-ului care oferă lista completă a
    # raselor de câini.
    # - Afișează lista de rase de câini în consolă.
    # - Solicită utilizatorului să introducă o rasă de câine și efectuează o nouă cerere GET pentru a obține o imagine
    # aleatorie a acelei rase.
    # - Afișează URL-ul imaginii în consolă sau, dacă preferi, deschide imaginea într-un browser web.
    # """
    # # =================== Partea I ===================
    # import requests
    # url = 'https://dog.ceo/api/breeds/list/all'
    # response = requests.get(url)
    #
    # if response.status_code == 200:
    #     rase = response.json()['message']
    #     print("Rase disponibile: ")
    #     for rasa in rase:
    #         print(rasa)
    #
    # # =================== Partea II ===================
    # rasa = input("Introduceti rasa de caine pentru a vedea o imagine").lower()
    # url = f'https://dog.ceo/api/breed/{rasa}/images/random'
    # response = requests.get(url)
    #
    # if response.status_code == 200:
    #     image_url = response.json()['message']
    #     print(f"Imaginea pentru rasa {rasa}: {image_url}")
    #
    # else:
    #     print("Nu s-a putut obtine o imagine pentru rasa specificata.")


    # # ------------------ Exercițiul 1 ------------------
    # """
    # Exercițiul 1: Verificator de Vreme cu OpenWeather
    # Descrierea Exercițiului:
    # Creează un script Python care folosește API-ul OpenWeather pentru a afișa vremea actuală în Chișinău. Scriptul ar
    # trebui să extragă și să afișeze temperatura actuală, descrierea vremii și viteza vântului.
    #
    # Pași Preliminari:
    #
    # - Înainte de a începe, va trebui să creezi un cont pe OpenWeather și să obții o cheie API (API key). După
    # înregistrare, navighează la secțiunea "API keys" din contul tău pentru a crea o nouă cheie.
    # - Odată ce ai cheia API, înlocuiește your_api_key din script cu cheia ta personală.
    # - Atentia: Poate dura cateva ore pana cand cheia ta va fi valida!
    #
    # Hint-uri pentru Implementare:
    #
    # - Utilizează pachetul requests pentru a efectua o cerere GET la endpoint-ul OpenWeather pentru date meteo.
    # - Construiește URL-ul cererii astfel: http://api.openweathermap.org/data/2.5/weather?q=Chisinau,MD&appid=your_api_key&units=metric, unde your_api_key trebuie înlocuit cu cheia ta personală.
    # - Răspunsul API va fi în format JSON și va include detalii precum temperatura (main['temp']), descrierea vremii
    # (weather[0]['description']) și viteza vântului (wind['speed']).
    # - Verifică răspunsul API pentru a te asigura că cererea a fost succesful (codul de status HTTP 200) înainte de a
    # încerca să extragi datele.
    # - Afișează datele extrase într-un format prietenos, de exemplu: "Temperatura în Chișinău: 20°C, cer senin,
    # vânt: 5m/s".
    # """
    # # Solutia
    # from config1 import WEATHER_API_KEY
    # import requests
    #
    # api_key = WEATHER_API_KEY
    # oras = "Chisinau,MD"
    #
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={oras}&appid={api_key}&units=metric"
    # response = requests.get(url)
    #
    # if response.status_code == 200:
    #     data = response.json()
    #     temperatura = data['main']['temp']
    #     descriere = data['weather'][0]['description']
    #     viteza_vantului = data['wind']['speed']
    #
    #     print(f"Temperatura in Chisinau este de {temperatura}°C, {descriere}, vant : {viteza_vantului} m/s")
    #
    # else:
    #     print("A avut loc o eroare in extragerea datelor meteo.")


    # ------------------ Exercițiul 2 ------------------
    """
    Exercițiul: Conversie Valutară folosind Exchange Rates API
    Descrierea Exercițiului:
    Dezvoltă un script Python care interoghează API-ul Exchange Rates pentru a converti o sumă specificată de
    utilizator dintr-o monedă aleasă în EUR. Acest exercițiu necesită obținerea unei chei API de la Exchange Rates API.

    Pași Preliminari:
    - Înregistrează-te pe Exchange Rates API și obține o cheie API.
    - Stochează cheia API într-un fișier numit config.py sub forma unei variabile EXCHANGERATES_API_KEY.
    - Alternativ, poți folosi variabile de mediu pentru a stoca cheia API, dar în acest exemplu vom importa cheia
    dintr-un fișier de configurare.

    Instrucțiuni:
    - Importă cheia API din fișierul de configurare folosind from config import EXCHANGERATES_API_KEY.
    - Solicită utilizatorului să introducă codul monedei din care dorește să convertească și suma respectivă.
    - Construiește URL-ul cererii pentru a efectua conversia folosind cheia API și datele introduse de utilizator.
    - Efectuează cererea GET la API folosind modulul requests și tratează răspunsul.
    - Afișează rezultatul conversiei sau un mesaj de eroare dacă cererea nu este reușită.
    """
    from config1 import EXCHANGERATES_API_KEY
    import requests

    api_key = EXCHANGERATES_API_KEY
    moneda_sursa = input("Introduceti codul monedei sursa: ")
    moneda_dest = input("Introduceti codul monedei dest: ")
    suma = input(f"Introduceti suma pe care doriti sa o convertiti din {moneda_sursa} in {moneda_dest}: ")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={moneda_dest}&from={moneda_sursa}&amount={suma}"
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        converted_amount = data['result']
        print(f"{suma}{moneda_sursa} este echivalentul a {converted_amount} EUR")
    else:
        print("A avut loc o eroare la conversie")



    # # ------------------ Exercițiul 3 ------------------
    # """
    # Exercițiul: Salvarea Citatului Zilei într-un Fișier JSON
    # Descrierea Exercițiului:
    # - Scopul acestui exercițiu este de a interoga un API pentru citate, pentru a obține citatul zilei din categoria management, și apoi de a salva acest citat într-un fișier JSON local. Acest exercițiu îți va dezvolta abilitățile de lucrul cu API-uri web, preluarea datelor în format JSON și lucrul cu fișiere în Python.
    #
    # Pași Preliminari:
    # - Pentru a efectua cererea la API, este necesară o cheie API. Această cheie trebuie obținută prin înregistrarea la serviciul They Said So Quotes API.
    # - După ce ai obținut cheia API, stocheaz-o într-un fișier config.py sub numele QUOTES_KEY sau în variabile de mediu, pentru a păstra securitatea datelor.
    #
    # Instrucțiuni:
    # - Folosește biblioteca requests pentru a efectua o cerere GET la endpoint-ul API-ului pentru citatul zilei, specificând categoria de interes (management).
    # - Adaugă cheia API în antetul cererii pentru a te autentifica la serviciul API.
    # - Extrage citatul din răspunsul JSON primit.
    # - Salvează citatul într-un fișier JSON local, formatând conținutul pentru lizibilitate.
    # - Gestionează posibilele erori și asigură un mesaj corespunzător în cazul unei cereri nereușite.
    # """

    # ------------------ Exercițiul 4 ------------------
    """
    Exercițiul: Afișarea Evenimentelor Astronomice Curente
    Descrierea Exercițiului:
    Obiectivul acestui exercițiu este de a crea un script Python care interoghează The Astronomy Picture of the Day (APOD) API de la NASA pentru a afișa informații despre evenimentul astronomic al zilei, inclusiv o scurtă descriere și un link către imaginea asociată. Deși APOD API poate fi folosit cu o cheie API pentru a accesa funcționalități suplimentare, pentru scopul acestui exercițiu, vom utiliza versiunea publică care nu necesită autentificare.

    Instrucțiuni:

    Folosește biblioteca requests pentru a efectua o cerere GET la endpoint-ul APOD API care oferă informații despre evenimentul astronomic al zilei.
    Extrage din răspunsul JSON titlul evenimentului, descrierea (explicația) și URL-ul imaginii.
    Afișează aceste informații în consolă, încurajând utilizatorul să viziteze linkul pentru a vedea imaginea astronomică.
    
    - titlul -> data['title']
    - explicatie -> data['explanation']
    - imaginea -> data['url']
    
    - url to use -> 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
    """

