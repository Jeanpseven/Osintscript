import instaloader
import requests

def obter_informacoes_perfil(username):
    loader = instaloader.Instaloader()

    try:
        perfil = instaloader.Profile.from_username(loader.context, username)
        return perfil
    except Exception as e:
        print(f"Erro ao carregar perfil: {e}")
        return None

def obter_legendas_e_locais(perfil):
    if perfil is None:
        return []

    legendas_e_locais = []

    for postagem in perfil.get_posts():
        legenda = postagem.caption
        local = postagem.location

        if legenda:
            legendas_e_locais.append({
                'legenda': legenda,
                'local': local.name if local else None
            })

    return legendas_e_locais

def pesquisar_perfis(username):
    url = f"https://www.instagram.com/web/search/topsearch/?query={username}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "users" in data and data["users"]:
            perfis = data["users"]
            
            nomes_usuarios = []
            
            for perfil in perfis:
                nome_usuario = perfil["user"]["username"]
                
                if nome_usuario not in nomes_usuarios:
                    nomes_usuarios.append(nome_usuario)
            
            return nomes_usuarios
        
    except requests.RequestException as e:
        print(f"Erro ao realizar a busca: {e}")
    
    return []

def obter_perfis_amigos_proximos(username, numero_postagens):
    loader = instaloader.Instaloader()

    perfil = instaloader.Profile.from_username(loader.context, username)

    perfis_amigos_proximos = []

    for postagem in perfil.get_posts()[:numero_postagens]:
        comentarios = postagem.get_comments()

        for comentario in comentarios:
            perfil_comentario = comentario.owner_profile

            if perfil_comentario not in perfis_amigos_proximos:
                perfis_amigos_proximos.append(perfil_comentario)

    return perfis_amigos_proximos

def gerar_descricao(perfil, legendas_e_locais, perfis_amigos_proximos):
    if perfil is None:
        return "Não foi possível obter informações do perfil."

    nome = perfil.full_name
    descricao = perfil.biography
    seguidores = perfil.followers
    seguindo = perfil.followees
    publicacoes = perfil.mediacount

    descricao_completa = f"Nome: {nome}\n"
    descricao_completa += f"Descrição: {descricao}\n"
    descricao_completa += f"Seguidores: {seguidores}\n"
    descricao_completa += f"Seguindo: {seguindo}\n"
    descricao_completa += f"Publicações: {publicacoes}\n\n"

    if legendas_e_locais:
        descricao_completa += "Legendas e Locais das Publicações:\n"
        for i, item in enumerate(legendas_e_locais, 1):
            descricao_completa += f"Postagem {i}:\n"
            descricao_completa += f"Legenda: {item['legenda']}\n"
            descricao_completa += f"Local: {item['local']}\n"
            descricao_completa += "\n"

    if perfis_amigos_proximos:
        descricao_completa += "Amigos Próximos:\n"
        for i, perfil_amigo in enumerate(perfis_amigos_proximos, 1):
            descricao_completa += f"Amigo {i}:\n"
            descricao_completa += f"Nome de Usuário: {perfil_amigo.username}\n"
            descricao_completa += f"Nome Completo: {perfil_amigo.full_name}\n"
            descricao_completa += "\n"

    return descricao_completa

def search_profile_on_site(site, username):
    url = site.format(username)
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Profile found on {site}: {url}")
    else:
        print(f"Profile not found on {site}")

# Exemplo de uso do script
username = input("Digite o nome de usuário do perfil do Instagram: ")
perfil = obter_informacoes_perfil(username)
legendas_e_locais = obter_legendas_e_locais(perfil)
perfis_amigos_proximos = obter_perfis_amigos_proximos(username, 10)
descricao = gerar_descricao(perfil, legendas_e_locais, perfis_amigos_proximos)
print(descricao)

# Lista de sites
sites = [
    "https://www.facebook.com/{}",
    "https://www.instagram.com/{}",
    "https://www.twitter.com/{}",
    "https://www.linkedin.com/in/{}",
    "https://www.reddit.com/user/{}",
    "https://www.pinterest.com/{}",
    "https://www.telegram.me/{}",
    "https://www.tiktok.com/@{}",
    "https://www.youtube.com/{}",
    "https://www.wattpad.com/user/{}",
    "https://www.netflix.com/{}",
    "https://www.github.com/{}",
"https://xvideos.com/models/{}",
"https://xvideos.com/channels/{}",
"https://pornhub.com/{}",
"https://t.me/{}"

]

# Busca em sites específicos
for site in sites:
    search_profile_on_site(site, username)
