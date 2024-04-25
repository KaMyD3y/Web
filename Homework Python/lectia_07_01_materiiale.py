if __name__ == "__main__":
    print("Bun venit la tema 07.01 - pip, venv, request")

    # # ================== PIP, VENV, REQUESTS ==================
    # import requests
    #
    # # Realizăm o cerere GET
    # response = requests.get('https://jsonplaceholder.typicode.com/posts')
    #
    # # Verificăm dacă cererea a fost reușită
    # if response.status_code == 200:
    #     # Parsăm JSON-ul într-o listă de dicționare Python
    #     posts = response.json()
    #
    #     # Afișăm primele 3 postări
    #     for post in posts[:3]:
    #         print("Title of current post is:", post['title'])
    # else:
    #     print('Eroare la preluarea postărilor')
    #
    # print("Finish executare.")
    # # ================== PIP, VENV, REQUESTS ==================
    # import requests
    #
    # # Definim URL-ul și datele pe care vrem să le trimitem
    # url = 'https://jsonplaceholder.typicode.com/posts'
    # my_post = {'title': 'Titlu nou', 'body': 'Conținutul postării', 'userId': 1}
    #
    # # Facem cererea POST
    # response = requests.post(url, json=my_post)
    #
    # # Verificăm dacă crearea a fost reușită
    # if response.status_code == 201:
    #     print('Postarea a fost creată cu succes.')
    #     created_post = response.json()
    #     print('ID Postare:', created_post['id'])
    # else:
    #     print('Eroare la crearea postării')

    # ================== PIP, VENV, REQUESTS ==================
    import requests
    from requests.exceptions import RequestException, Timeout

    try:
        response = requests.get('https://jsonplaceholder.typicode.com/poss', timeout=5)
        response.raise_for_status()  # Raises HTTPError for bad responses (4XX or 5XX)
    except RequestException as e:
        print('A apărut o eroare:', e)


    # # ================== PIP, VENV, REQUESTS ==================
    # import requests
    #
    # # Definim URL-ul și parametrii pentru cerere
    # url = 'https://jsonplaceholder.typicode.com/posts'
    # params = {'userId': 1}
    #
    # # Facem cererea GET cu parametrii specificați
    # response = requests.get(url, params=params)
    # if response.status_code == 200:
    #     # Extragem și afișăm titlurile postărilor utilizatorului 1
    #     posts = response.json()
    #     for post in posts:
    #         print(post['title'])
    #
    # else:
    #     print('Eroare la preluarea postărilor')

