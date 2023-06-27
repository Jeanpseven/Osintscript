import requests

def search_social_media_profiles(name):
    social_media_sites = [
        "https://www.facebook.com/{}",
        "https://www.instagram.com/{}",
        "https://www.twitter.com/{}",
        "https://www.linkedin.com/in/{}",
        "https://www.reddit.com/user/{}",
        "https://www.pinterest.com/{}",
        "https://www.telegram.me/{}",
        "https://www.tiktok.com/@{}",
        "https://www.youtube.com/{}"
    ]

    found_profiles = []

    for site in social_media_sites:
        url = site.format(name)
        response = requests.get(url)
        
        if response.status_code == 200:
            found_profiles.append(url)

    return found_profiles

# Exemplo de uso:
name = input("Digite o nome para pesquisa: ")
profiles = search_social_media_profiles(name)

if profiles:
    print("Perfis encontrados nas redes sociais:")
    for profile in profiles:
        print(profile)
else:
    print("Nenhum perfil encontrado nas redes sociais.")
