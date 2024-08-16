import os
import subprocess
import ctypes

# Função para verificar se o script está sendo executado como administrador
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Função para bloquear sites
def bloquear_sites(sites):
    # O caminho para o arquivo hosts no Windows
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    
    # Adicionar sites à lista de bloqueio
    try:
        with open(hosts_path, 'a') as hosts_file:
            for site in sites:
                # Adiciona a entrada no arquivo hosts para bloquear o site
                hosts_file.write(f"127.0.0.1 {site}\n")
        print("Sites bloqueados com sucesso.")
    except PermissionError:
        print("Permissão negada. Execute o script como administrador.")
    except Exception as e:
        print(f"Um erro ocorreu ao bloquear sites: {e}")

# Função para limpar o cache DNS
def limpar_cache_dns():
    try:
        subprocess.run(["ipconfig", "/flushdns"], check=True)
        print("Cache DNS limpo com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Um erro ocorreu ao limpar o cache DNS: {e}")

# Lista de sites a serem bloqueados
sites_to_block = [
    "www.youtube.com", "www.facebook.com", "www.instagram.com", "www.twitter.com",
    "www.x.com", "www.max.com", "www.primevideo.com", "www.disneyplus.com",
    "www.netflix.com", "globoplay.globo.com", "tv.sbt.com.br", "youtube.com",
    "facebook.com", "instagram.com", "twitter.com", "x.com", "max.com",
    "primevideo.com", "disneyplus.com", "netflix.com", "www.torproject.org", "torproject.org"
]

# Verificar se o script está sendo executado como administrador
if is_admin():
    bloquear_sites(sites_to_block)
    limpar_cache_dns()
else:
    print("Este script precisa ser executado como administrador.")
