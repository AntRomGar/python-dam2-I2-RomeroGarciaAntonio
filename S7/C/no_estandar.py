# pip install requests
import requests
import webbrowser

salir = False

while not salir:
    try:
        pokemon = input("Ingrese el nombre o ID del Pokémon: ").lower()
        url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/"
        url2 = f"https://pokeapi.co/api/v2/pokemon/{pokemon}/"
        sprite_response = requests.get(url2)
        sprite_data = sprite_response.json()
        response = requests.get(url)
        data = response.json()
        
        # Abrir el enlace del sprite en el navegador
        webbrowser.open(sprite_data['sprites']['front_default'])
        
        # Mostrar información sobre el Pokémon
        print(data['name'].capitalize())
        flavor_text = None
        flavor_text_en = None

        for entry in data["flavor_text_entries"]:
            if entry["language"]["name"] == "es" and flavor_text is None:
                flavor_text = entry["flavor_text"]
            elif entry["language"]["name"] == "en" and flavor_text_en is None:
                flavor_text_en = entry["flavor_text"]
            if flavor_text and flavor_text_en:
                break
        if flavor_text:
            print(flavor_text.replace('\n', ' ').replace('\f', ' '))
        elif flavor_text_en:
            print(flavor_text_en.replace('\n', ' ').replace('\f', ' '))
        else:
            print("No se encontró ninguna descripción disponible.")
       
        # Preguntar si quiere buscar otro Pokémon
        print("¿Quieres buscar otro Pokémon? (s/n): ", end="")
        respuesta = input().lower()
        if respuesta != "s":
            salir = True
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")