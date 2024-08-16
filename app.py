from flask import Flask, jsonify, request
from instagram_private_api import Client, ClientCompatPatch
import time
import requests
from discord_webhook import DiscordEmbed, DiscordWebhook
from g4f.client import Client
import datetime
from dateutil import parser
import random
import json

app = Flask(__name__)


API_KEY = 'IPGEOLOCATION.IO API KEY'
chave_api_cnpj = "WS RECEITA API KEY"
WEBHOOK_URL = 'LOGS DISCORD WEBHOOK'

@app.route("/")
def home():
    return '{"erro": "Use as routes /ip/:ip, /cnpj/:cnpj, /instagram/:user e /users/:id", "discord": "https://discord.gg/betterapi"}'

def get_ip_info(ip):
    route = f'/ip/{ip}'
    url = f'https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={ip}'

    try:
        response = requests.get(url)
        data = response.json()

        if 'country_flag' in data:
            del data['country_flag']

        webhook = DiscordWebhook(url=WEBHOOK_URL)
        embed = DiscordEmbed(title='Nova Requisição!', color='03b2f8')
        embed.add_embed_field(name='Route', value=f'/ip/{ip}')
        embed.add_embed_field(name='Response', value=f'```{data}```')
        webhook.add_embed(embed)
        webhook.execute()

        return jsonify(data)
    except requests.RequestException:
        return jsonify({'error': 'Erro ao consultar a API de geolocalização.'}), 500

@app.route('/ip/<ip>', methods=['GET'])
def ip_info(ip):
    return get_ip_info(ip)

@app.route('/instagram/<username>')
def get_instagram_data(username):
    
    username = username

    # Construir a URL da solicitação
    url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}'

    # Definir os cabeçalhos da solicitação
    headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'pt-BR,pt;q=0.9',
    'cookie': 'INSERT YOUR COOKIE HERE!',
    'dpr': '1',
    'referer': 'https://www.instagram.com/cristiano/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="99.0.0.0", "Google Chrome";v="109.0.5414.168", "Chromium";v="109.0.5414.168"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"0.3.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'viewport-width': '689',
    'x-asbd-id': '129477',
    'x-csrftoken': 'bmLR4yeJXx7Bc7i9oxkRmg',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-requested-with': 'XMLHttpRequest'
}

    
    proxies = [
    '192.252.214.20:15864',
    '31.170.22.127:1080',
    '192.111.139.163:19404',
    '184.170.248.5:4145',
    '72.37.216.68:4145',
    '45.144.30.254:443',
    '72.195.114.169:4145',
    '138.2.73.157:1080',
    '72.195.34.42:4145',
    '51.15.139.59:16379',
    '72.210.252.134:46164',
    '207.180.198.241:37443',
    '62.171.131.101:37447',
    '142.54.232.6:4145',
    '82.223.121.72:60325',
    '199.102.104.70:4145',
    '67.201.59.70:4145',
    '98.188.47.150:4145',
    '148.66.130.187:5630',
    '72.195.101.99:4145',
    '185.82.87.30:1080',
    '192.252.208.70:14282',
    '184.178.172.11:4145',
    '98.162.25.7:31653',
    '163.172.149.133:16379',
    '104.248.151.220:52106',
    '72.217.216.239:4145',
    '98.170.57.249:4145',
    '92.204.135.37:23918',
    '75.119.145.169:61553',
    '188.164.196.30:62564',
    '31.42.184.144:57752',
    '203.161.32.218:52903',
    '146.59.70.29:33076',
    '72.49.49.11:31034',
    '92.205.110.118:18374',
    '194.4.50.60:12334',
    '72.206.181.97:64943',
    '37.18.73.60:5566',
    '192.252.220.89:4145',
    '161.97.147.193:29901',
    '207.180.198.241:35119',
    '72.195.34.60:27391',
    '139.162.238.184:11227',
    '166.62.35.102:45775',
    '72.210.208.101:4145',
    '75.119.145.154:31074',
    '95.111.227.164:39888',
    '92.204.134.38:34261',
    '162.241.79.22:32371',
    '103.174.178.249:2004',
    '174.77.111.196:4145',
    '148.72.212.212:58474',
]


    selected_proxy = random.choice(proxies)

# Dividir o endereço IP e a porta
    host, port = selected_proxy.split(':')

# Construir proxies dictionary com o endereço IP e a porta
    proxies = {'socks5': (host, int(port))}

# Fazer a solicitação GET com os cabeçalhos definidos
    response = requests.get(url, headers=headers, proxies=proxies)

    # Verificar o código de status da resposta
    if response.status_code == 200:
        data = response.json()
        
        # Acessar as informações específicas que você deseja extrair
        user_data = data.get('data', {}).get('user', {})
        biography = user_data.get('biography', None)
        followed_by_count = user_data.get('edge_followed_by', {}).get('count', None)
        following_count = user_data.get('edge_follow', {}).get('count', None)
        full_name = user_data.get('full_name', None)
        is_verified = user_data.get('is_verified', None)
        profile_pic_url_hd = user_data.get('profile_pic_url_hd', None)
        
        # Criar um dicionário com os dados filtrados
        filtered_data = {
            "biography": biography,
            "followed_by_count": followed_by_count,
            "following_count": following_count,
            "full_name": full_name,
            "is_verified": is_verified,
            "profile_pic_hd": profile_pic_url_hd
        }

        webhook = DiscordWebhook(url=WEBHOOK_URL)
        embed = DiscordEmbed(title='Nova Requisição!', color='03b2f8')
        embed.add_embed_field(name='Route', value=f'/instagram/{username}')
        embed.add_embed_field(name='Response', value=f'```json \n {filtered_data}```')
        webhook.add_embed(embed)
        webhook.execute()


        # Retornar os dados filtrados como JSON
        return jsonify(filtered_data)
        
    else:
        # Se houve um erro na solicitação, retornar o código de status
        return jsonify({"error": 'Ocorreu um erro!'})

@app.route('/cnpj/<cnpj>', methods=['GET'])
def get_cnpj_info(cnpj):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}?access_token={chave_api_cnpj}'

    try:
        response = requests.get(url)
        data = response.json()
        webhook = DiscordWebhook(url=WEBHOOK_URL)
        embed = DiscordEmbed(title='Nova Requisição!', color='03b2f8')
        embed.add_embed_field(name='Route', value=f'/cnpj/{cnpj}')
        embed.add_embed_field(name='Response', value=f'```json \n {data}```')
        webhook.add_embed(embed)
        webhook.execute()
        return jsonify(data)
    except requests.RequestException:
        return jsonify({'error': 'Erro ao consultar a API de CNPJ.'}, 500)

@app.route('/minecraft/<ip>')
def get_minecraft_server(ip):
    try:
        url = f'https://api.mcsrvstat.us/2/{ip}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'hostname' in data:
            server_data = {
                'ip': data['ip'],
                'port': data['port'],
                'hostname': data['hostname'],
                'motd': data['motd']['clean'][0],
                'players_online': data['players']['online'] if 'players' in data else 0,
                'max_players': data['players']['max'] if 'players' in data else 0,
            }
            webhook = DiscordWebhook(url=WEBHOOK_URL)
            embed = DiscordEmbed(title='Nova Requisição!', color='03b2f8')
            embed.add_embed_field(name='Route', value=f'/ip/{ip}')
            embed.add_embed_field(name='Response', value=f'```{server_data}```')
            webhook.add_embed(embed)
            webhook.execute()
            return jsonify(server_data)
        else:
            return jsonify({'error': 'Não foi possível obter os dados do servidor.'}), 404
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Erro ao acessar a API: {str(e)}'}), 500
    except (KeyError, ValueError) as e:
        return jsonify({'error': 'Resposta inválida da API.'}), 500


def diff_months(start_date, final_date, round_up_fractional_months=False):
    inverse = False
    if start_date > final_date:
        start_date, final_date = final_date, start_date
        inverse = True

    years_difference = final_date.year - start_date.year
    months_difference = final_date.month - start_date.month
    days_difference = final_date.day - start_date.day

    month_correction = 0
    if round_up_fractional_months and days_difference > 0:
        month_correction = 1
    elif not round_up_fractional_months and days_difference < 0:
        month_correction = -1

    return (1 if not inverse else -1) * (years_difference * 12 + months_difference + month_correction)

def get_next_boost_date(boost_level, last_boost_date):
    if boost_level == 1:
        return last_boost_date + datetime.timedelta(days=30)
    elif boost_level == 2:
        return last_boost_date + datetime.timedelta(days=60)
    elif boost_level == 3:
        return last_boost_date + datetime.timedelta(days=90)
    elif boost_level == 4:
        return last_boost_date + datetime.timedelta(days=180)
    elif boost_level == 5:
        return last_boost_date + datetime.timedelta(days=270)
    elif boost_level == 6:
        return last_boost_date + datetime.timedelta(days=360)
    elif boost_level == 7:
        return last_boost_date + datetime.timedelta(days=450)
    elif boost_level == 8:
        return last_boost_date + datetime.timedelta(days=540)
    elif boost_level == 9:
        return "MaxLevelReached"
    else:
        return "InvalidBoostLevel"

def get_boost_info(user_id, token):
    try:
        user_response = requests.get(f"https://discord.com/api/v10/users/{user_id}", headers={"Authorization": token})
        user_data = user_response.json()

        profile_response = requests.get(f"https://discord.com/api/v10/users/{user_id}/profile", headers={"Authorization": token})
        profile_data = profile_response.json()

        # Extrai a data de início do boost
        boost_start_date_str = profile_data.get("premium_guild_since")
        if boost_start_date_str is not None:
            try:
                boost_start_date = parser.parse(boost_start_date_str).replace(tzinfo=None)
                
                # Calcula a data do próximo boost
                current_date = datetime.datetime.now().replace(tzinfo=None)
                next_boost_date = boost_start_date + datetime.timedelta(days=30)  # Adiciona 30 dias
                
                # Se a próxima data de boost for antes da data atual, adiciona mais um mês
                if next_boost_date <= current_date:
                    next_boost_date += datetime.timedelta(days=30)
                    
                next_boost_date_str = next_boost_date.isoformat()
                
                # Calcula o nível do próximo boost
                current_level = None
                for badge in profile_data["badges"]:
                    badge_id = badge.get("id")
                    if badge_id.startswith("guild_booster_lvl"):
                        current_level = int(badge_id.split("guild_booster_lvl")[1])
                        break

                if current_level is not None:
                    if current_level < 8:
                        next_boost_level = f"guild_booster_lvl{current_level + 1}"
                    else:
                        next_boost_level = "MaxLevelReached"
                else:
                    next_boost_level = "NotApplicable"
                
            except ValueError:
                next_boost_date_str = "Sem Boost."
                next_boost_level = "Sem Boost."
        else:
            next_boost_date_str = "Sem Boost."
            next_boost_level = "Sem Boost."
        
        # Monta o JSON com os dados do usuário e informações sobre o próximo boost
        user_info = {
            "user_id": user_id,
            "username": user_data["username"],
            "discriminator": user_data["discriminator"],
            "avatar_url": f"https://cdn.discordapp.com/avatars/{user_id}/{user_data['avatar']}.png",
            "next_boost": {
                "level": next_boost_level,
                "date": next_boost_date_str
            },
            "badges": profile_data["badges"],
            "profile_data": {
                "connected_accounts": profile_data["connected_accounts"],
                "guild_badges": profile_data["guild_badges"],
                "premium_guild_since": profile_data["premium_guild_since"],
                "premium_since": profile_data["premium_since"],
                "premium_type": profile_data["premium_type"],
                "profile_themes_experiment_bucket": profile_data["profile_themes_experiment_bucket"],
                "user_profile": profile_data["user_profile"],
                "user_bio": profile_data["user_profile"]["bio"],
                "boost_atual": profile_data["badges"][-1]["id"] if profile_data["badges"] else "Nenhum boost disponível"
            }
        }
        
        return user_info

    except Exception as e:
        print(f"Erro ao realizar a requisição: {e}")
        return None



@app.route('/user/<user_id>')
def boost_info(user_id):
    # Substitua 'YOUR_DISCORD_TOKEN' pelo seu token de autenticação do Discord
    boost_data = get_boost_info(user_id, 'TOKEN')
    if boost_data:
        webhook = DiscordWebhook(url=WEBHOOK_URL)
        embed = DiscordEmbed(title='Nova Requisição!', color='03b2f8')
        embed.add_embed_field(name='Route', value=f'/user/{user_id}')
        embed.add_embed_field(name='Response', value=f'```json \n {boost_data}```')
        webhook.add_embed(embed)
        webhook.execute()
        return jsonify(boost_data)
    else:
        return jsonify({"error": "Erro ao obter informações de boost"}), 500


@app.route('/gpt-4/<prompt>')
def gpt4(prompt: str):

    client = Client()
    response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": f"Você é o copilot de uma empresa chamada BetterAPI, você é encarrgado de responder perguntas de uma forma precisa e com menos de 100 linhas! Aqui está sua duvida: {prompt}"}],
    )

    webhook = DiscordWebhook(url=WEBHOOK_URL)
    embed = DiscordEmbed(title='Nova Requisição!', color='03b2f8')
    embed.add_embed_field(name='Route', value=f'/gpt-4/{prompt}')
    embed.add_embed_field(name='Response', value=f'```{response.choices[0].message.content}```')
    webhook.add_embed(embed)
    webhook.execute()

    return response.choices[0].message.content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
