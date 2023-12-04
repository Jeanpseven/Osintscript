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
"https://t.me/{}",
"https://2Dimensions.com/a/{}",
"http://forum.3dnews.ru/member.php?username={}",
"https://www.7cups.com/@{}",
"https://2Dimensions.com/a/{}", "http://forum.3dnews.ru/member.php?username={}", "https://www.7cups.com/@{}", "https://8tracks.com/{}", "https://www.9gag.com/u/{}", "https://apclips.com/{}", "https://about.me/{}", "https://independent.academia.edu/{}", "https://admireme.vip/{}", "https://airlinepilot.life/u/{}", "https://airbit.com/{}", "https://www.airliners.net/user/{}", "https://www.alik.cz/u/{}", "https://www.allthingsworn.com/profile/{}", "https://allmylinks.com/{}", "https://aminoapps.com/u/{}", "https://anilist.co/user/{}", "https://developer.apple.com/forums/profile/{}", "https://discussions.apple.com/profile/{}", "https://archiveofourown.org/users/{}", "https://archive.org/details/@{}", "https://www.artstation.com/{}", "https://asciinema.org/~{}", "https://ask.fedoraproject.org/u/{}", "https://ask.fm/{}", "https://audiojungle.net/user/{}", "https://www.autofrage.net/nutzer/{}", "https://www.avizo.cz/{}", "https://blip.fm/{}", "https://{}", "https://www.bandcamp.com/{}", "https://www.bazar.cz/{}", "https://www.behance.net/{}", "https://bezuzyteczna.pl/uzytkownicy/{}", "https://www.biggerpockets.com/users/{}", "https://www.bikemap.net/en/u/{}", "https://forum.dangerousthings.com/u/{}", "https://bitbucket.org/{}", "https://bitcoinforum.com/profile/{}", "https://community.bitwarden.com/u/{}", "https://{}", "https://bodyspace.bodybuilding.com/{}", "https://pt.bongacams.com/profile/{}", "https://www.bookcrossing.com/mybookshelf/{}", "https://community.brave.com/u/{}", "https://buymeacoff.ee/{}", "https://www.buymeacoffee.com/{}", "https://buzzfeed.com/{}", "https://www.cgtrader.com/{}", "https://www.cnet.com/profiles/{}", "https://ctan.org/author/{}", "https://caddy.community/u/{}", "https://community.cartalk.com/u/{}", "https://carbonmade.com/fourohfour?domain={}", "https://{}", "https://career.habr.com/{}", "https://www.championat.com/user/{}", "https://chaos.social/@{}", "https://profil.chatujme.cz/{}", "https://chaturbate.com/{}", "https://www.chess.com/member/{}", "https://www.chess.com/callback/user/valid?username={}", "https://choice.community/u/{}", "https://clapperapp.com/{}", "https://community.cloudflare.com/u/{}", "https://www.clozemaster.com/players/{}", "https://www.clubhouse.com/@{}", "https://codesnippets.fandom.com/wiki/User:{}", "https://www.codecademy.com/profiles/{}", "https://www.codechef.com/users/{}", "https://codeforces.com/profile/{}", "https://codeforces.com/api/user.info?handles={}", "https://codepen.io/{}", "https://profile.codersrank.io/user/{}", "https://coderwall.com/{}", "https://www.codewars.com/users/{}", "https://coinvote.cc/profile/{}", "https://www.colourlovers.com/lover/{}", "https://{}", "https://www.coroflot.com/{}", "https://www.cracked.com/members/{}", "https://{}", "https://crowdin.com/profile/{}", "https://community.cryptomator.org/u/{}", "https://cults3d.com/en/users/{}", "https://dev.to/{}", "https://dmoj.ca/user/{}", "https://www.dailymotion.com/{}", "https://www.dealabs.com/profile/{}", "https://{}", "https://www.discogs.com/user/{}", "https://discuss.elastic.co/u/{}", "https://disqus.com/{}", "https://hub.docker.com/u/{}", "https://hub.docker.com/v2/users/{}", "https://dribbble.com/{}", "https://www.duolingo.com/profile/{}", "https://www.duolingo.com/2017-06-30/users?username={}", "https://community.eintracht.de/fans/{}", "https://forums.envato.com/u/{}", "https://www.erome.com/{}", "https://www.etsy.com/shop/{}", "https://euw.op.gg/summoner/userName={}", "https://{}", "https://www.eyeem.com/u/{}", "https://f3.cool/{}", "https://fameswap.com/user/{}", "https://www.fandom.com/u/{}", "https://www.finanzfrage.net/nutzer/{}", "https://www.fiverr.com/{}", "https://www.flickr.com/people/{}", "https://my.flightradar24.com/{}", "https://flipboard.com/@{}", "https://www.rusfootball.info/user/{}", "https://fortnitetracker.com/profile/all/{}", "https://www.forumophilia.com/profile.php?mode=viewprofile&u={}", "https://fosstodon.org/@{}", "https://freelance.habr.com/freelancers/{}", "https://www.freelancer.com/u/{}", "https://www.freelancer.com/api/users/0.1/users?usernames%5B%5D={}", "https://freesound.org/people/{}", "https://www.g2g.com/{}", "https://www.g2g.com/{}", "https://gitlab.gnome.org/{}", "https://gitlab.gnome.org/{}", "https://www.gaiaonline.com/profiles/{}", "https://www.gamespot.com/profile/{}", "https://auth.geeksforgeeks.org/user/{}", "https://genius.com/artists/{}", "https://genius.com/{}", "https://www.gesundheitsfrage.net/nutzer/{}", "https://www.getmyuni.com/user/{}", "https://www.giantbomb.com/profile/{}", "https://giphy.com/{}", "https://{}", "https://www.github.com/{}", "https://gitlab.com/{}", "https://gitlab.com/api/v4/users?username={}", "https://gitee.com/{}", "https://www.goodreads.com/{}", "https://play.google.com/store/apps/developer?id={}", "https://plugins.gradle.org/u/{}", "https://www.grailed.com/{}", "https://www.grailed.com/{}", "http://en.gravatar.com/{}", "https://www.gumroad.com/{}", "https://www.gutefrage.net/nutzer/{}", "https://www.hexrpg.com/userinfo/{}", "https://forum.hackthebox.eu/profile/{}", "https://hackaday.io/{}", "https://hackerearth.com/@{}", "https://news.ycombinator.com/user?id={}", "https://hackerone.com/{}", "https://hackerrank.com/{}", "https://scholar.harvard.edu/{}", "https://hashnode.com/@{}", "https://www.heavy-r.com/user/{}", "https://holopin.io/@{}", "https://houzz.com/user/{}", "https://hubpages.com/@{}", "https://hubski.com/user/{}", "https://icq.im/{}", "https://www.ifttt.com/p/{}", "https://irc-galleria.net/users/search?username={}", "https://irc-galleria.net/user/{}", "https://community.icons8.com/u/{}", "https://www.imagefap.com/profile/{}", "https://imgup.cz/{}", "https://imgur.com/user/{}", "https://api.imgur.com/account/v1/accounts/{}", "https://www.instructables.com/member/{}", "https://www.instructables.com/json-api/showAuthorExists?screenName={}", "https://app.intigriti.com/profile/{}", "https://api.intigriti.com/user/public/profile/{}", "https://forum.ionicframework.com/u/{}", "https://issuu.com/{}", "https://{}", "https://www.itemfix.com/c/{}", "https://translate.jellyfin.org/user/{}", "https://{}", "https://discourse.joplinapp.org/u/{}", "https://www.keakr.com/en/profile/{}", "https://www.kaggle.com/{}", "https://keybase.io/{}", "https://kik.me/{}", "https://ws2.kik.com/user/{}", "https://www.kongregate.com/accounts/{}", "https://www.linux.org.ru/people/{}", "https://launchpad.net/~{}", "https://leetcode.com/{}", "https://www.lesswrong.com/users/@{}", "https://letterboxd.com/{}", "https://lichess.org/@/{}", "https://linktr.ee/{}", "https://listed.to/@{}", "https://listed.to/@{}", "https://{}", "https://lobste.rs/u/{}", "https://lolchess.gg/profile/na/{}", "https://lottiefiles.com/{}", "https://www.lushstories.com/profile/{}", "https://forums.mmorpg.com/profile/{}", "https://mapify.travel/{}", "https://mapify.travel/{}", "https://medium.com/@{}", "https://medium.com/feed/@{}", "https://www.memrise.com/user/{}", "https://api.mojang.com/users/profiles/minecraft/{}", "https://www.mixcloud.com/{}", "https://api.mixcloud.com/{}", "https://www.modelhub.com/{}", "https://monkeytype.com/profile/{}", "https://api.monkeytype.com/users/{}", "https://motherless.com/m/{}", "https://www.motorradfrage.net/nutzer/{}", "https://myanimelist.net/profile/{}", "https://www.myminifactory.com/users/{}", "https://www.mydramalist.com/profile/{}", "https://myspace.com/{}", "https://community.native-instruments.com/profile/{}", "https://nationstates.net/nation={}", "https://nationstates.net/region={}", "https://blog.naver.com/{}", "https://www.needrom.com/author/{}", "https://{}", "https://help.nextcloud.com/u/{}", "https://nightbot.tv/t/{}", "https://api.nightbot.tv/1/channels/t/{}", "https://ninjakiwi.com/profile/{}", "https://ninjakiwi.com/profile/{}", "https://www.nintendolife.com/users/{}", "https://www.nitrotype.com/racer/{}", "https://notabug.org/{}", "https://notabug.org/{}", "https://nyaa.si/user/{}", "https://ogu.gg/{}", "https://www.openstreetmap.org/user/{}", "https://opensource.com/users/{}", "https://community.oracle.com/people/{}", "https://ourdjtalk.com/members?username={}", "https://forums.pcgamer.com/members/?username={}", "https://psnprofiles.com/?psnId={}", "https://psnprofiles.com/{}", "https://packagist.org/search/?q={}", "https://packagist.org/packages/{}", "https://pastebin.com/u/{}", "https://www.patreon.com/{}", "https://www.pepper.it/profile/{}", "https://www.periscope.tv/{}", "https://www.pinkbike.com/u/{}", "https://play.google.com/store/apps/developer?id={}", "https://pocketstars.com/{}", "https://pokemonshowdown.com/users/{}", "https://polarsteps.com/{}", "https://api.polarsteps.com/users/byusername/{}", "https://www.polygon.com/users/{}", "https://polymart.org/user/{}", "https://pornhub.com/users/{}", "https://www.producthunt.com/@{}", "http://promodj.com/{}", "https://pypi.org/user/{}", "https://{}", "https://rateyourmusic.com/~{}", "https://forum.rclone.org/u/{}", "https://www.redtube.com/users/{}", "https://www.redbubble.com/people/{}", "https://www.reddit.com/user/{}", "https://www.reisefrage.net/nutzer/{}", "https://replit.com/@{}", "https://www.researchgate.net/profile/{}", "https://www.reverbnation.com/{}", "https://www.roblox.com/user.aspx?username={}", "https://www.rockettube.com/{}", "https://royalcams.com/profile/{}", "https://rubygems.org/profiles/{}", "https://rumble.com/user/{}", "https://apps.runescape.com/runemetrics/app/overview/player/{}", "https://apps.runescape.com/runemetrics/profile/profile?user={}", "https://swapd.co/u/{}", "https://www.sbazar.cz/{}", "https://scratch.mit.edu/users/{}", "https://www.scribd.com/{}", "https://www.shitpostbot.com/user/{}", "https://www.shpock.com/shop/{}", "https://community.signalusers.org/u/{}", "https://sketchfab.com/{}", "https://{}", "https://www.slant.co/users/{}", "https://slashdot.org/~{}", "https://slideshare.net/{}", "https://slides.com/{}", "https://{}", "https://www.smule.com/{}", "https://www.snapchat.com/add/{}", "https://soundcloud.com/{}", "https://sourceforge.net/u/{}", "https://soylentnews.org/~{}", "https://speedrun.com/user/{}", "https://splice.com/{}", "https://splits.io/users/{}", "https://www.sporcle.com/user/{}", "https://www.sportlerfrage.net/nutzer/{}", "https://www.sports.ru/profile/{}", "https://open.spotify.com/user/{}", "https://robertsspaceindustries.com/citizens/{}", "https://steamcommunity.com/groups/{}", "https://www.strava.com/athletes/{}", "https://forum.sublimetext.com/u/{}", "https://ch.tetr.io/u/{}", "https://ch.tetr.io/api/users/{}", "https://tldrlegal.com/users/{}", "https://traktrain.com/{}", "https://t.me/{}", "https://tellonym.me/{}", "https://tenor.com/users/{}", "https://themeforest.net/user/{}", "https://tiktok.com/@{}", "https://www.tnaflix.com/profile/{}", "https://www.tradingview.com/u/{}", "https://www.trakt.tv/users/{}", "https://trashbox.ru/users/{}", "https://traewelling.de/@{}", "https://trello.com/{}", "https://trello.com/1/Members/{}", "https://tryhackme.com/p/{}", "https://tryhackme.com/api/user/exist/{}", "https://tuna.voicemod.net/user/{}", "https://tweakers.net/gallery/{}", "https://www.twitch.tv/{}", "https://m.twitch.tv/{}", "https://twitter.com/{}", "https://nitter.net/{}", "https://data.typeracer.com/pit/profile?user={}", "https://ultimate-guitar.com/u/{}", "https://unsplash.com/@{}", "https://www.quora.com/profile/{}", "https://vk.com/{}", "https://vsco.co/{}", "https://forum.velomania.ru/member.php?username={}", "https://account.venmo.com/u/{}", "https://test1.venmo.com/u/{}", "https://vero.co/{}", "https://vimeo.com/{}", "https://virgool.io/@{}", "https://www.virustotal.com/gui/user/{}", "https://www.virustotal.com/ui/users/{}", "https://discourse.wicg.io/u/{}", "https://www.warriorforum.com/members/{}", "https://www.wattpad.com/user/{}", "https://www.wattpad.com/api/v3/users/{}", "https://{}", "https://hosted.weblate.org/user/{}", "https://{}", "https://forums.whonix.org/u/{}", "http://www.wikidot.com/user:info/{}", "https://en.wikipedia.org/wiki/Special:CentralAuth/{}", "https://community.windy.com/user/{}", "https://{}", "https://community.wolfram.com/web/{}", "https://{}", "https://profiles.wordpress.org/{}", "https://www.wordnik.com/users/{}", "https://www.wykop.pl/ludzie/{}", "https://xboxgamertag.com/search/{}", "https://xvideos.com/profiles/{}", "https://music.yandex/users/{}", "https://www.younow.com/{}", "https://api.younow.com/php/api/broadcast/info/user={}", "https://youpic.com/photographer/{}", "https://youporn.com/uservids/{}", "https://www.zhihu.com/people/{}", "https://akniga.org/profile/{}", "http://www.authorstream.com/{}", "https://www.baby.ru/u/{}", "https://www.babyblog.ru/user/{}", "https://chaos.social/@{}", "https://www.couchsurfing.com/people/{}", "https://d3.ru/user/{}", "https://www.dailykos.com/user/{}", "https://www.dailykos.com/signup/check_nickname?nickname={}", "http://dating.ru/{}", "https://devrant.com/users/{}", "https://www.drive2.ru/users/{}", "https://egpu.io/forums/profile/{}", "https://ebio.gg/{}", "https://community.eintracht.de/fans/{}", "https://www.fixya.com/users/{}", "https://www.fl.ru/users/{}", "https://forum.guns.ru/forummisc/blog/{}", "https://www.freecodecamp.org/{}", "https://api.freecodecamp.org/api/users/get-public-profile?username={}", "https://www.furaffinity.net/user/{}", "https://www.geocaching.com/p/default.aspx?u={}", "https://gfycat.com/@{}", "https://habr.com/ru/users/{}", "https://www.hackster.io/{}", "https://www.hunting.ru/forum/members/?username={}", "https://imgsrc.ru/main/user.php?user={}", "http://forum.igromania.ru/member.php?username={}", "https://www.interpals.net/{}", "https://irecommend.ru/users/{}", "https://jbzd.com.pl/uzytkownik/{}", "http://www.jeuxvideo.com/profil/{}", "https://ko-fi.com/{}", "https://kwork.ru/user/{}", "https://lab.pentestit.ru/{}", "https://lab.pentestit.ru/profile/{}", "https://last.fm/user/{}", "https://forum.leasehackr.com/u/{}", "https://www.livelib.ru/reader/{}", "https://mastodon.cloud/@{}", "https://mastodon.social/@{}", "https://mastodon.technology/@{}", "https://mastodon.xyz/@{}", "https://www.mercadolivre.com.br/perfil/{}", "https://www.metacritic.com/user/{}", "https://www.minds.com/{}", "https://www.minds.com/api/v3/register/validate?username={}", "https://moikrug.ru/{}", "https://mstdn.io/@{}", "https://www.nairaland.com/{}", "https://{}", "https://note.com/{}", "https://www.npmjs.com/~{}", "https://www.opennet.ru/~{}", "https://osu.ppy.sh/users/{}", "https://php.ru/forum/members/?username={}", "https://pikabu.ru/@{}", "https://pr0gramm.com/user/{}", "https://pr0gramm.com/api/profile/info?name={}", "https://prog.hu/azonosito/info/{}", "https://prog.hu/azonosito/info/{}", "https://queer.af/@{}", "https://satsis.info/user/{}", "https://sessionize.com/{}", "https://{}", "https://social.tchncs.de/@{}", "https://spletnik.ru/user/{}", "https://www.svidbook.ru/user/{}", "https://www.toster.ru/user/{}", "http://uid.me/{}", "https://wiki.vg/User:{}", "https://www.wykop.pl/ludzie/{}", "https://xhamster.com/users/{}", "https://www.znanylekarz.pl/{}"
]

# Busca em sites específicos
for site in sites:
    search_profile_on_site(site, username)
