import subprocess

def configure_apache():
    # Contenu du fichier de configuration Apache
    apache_conf_content = """
# Nouvelle configuration Apache
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
"""

    # Chemin du fichier de configuration d'Apache
    apache_conf_path = "/etc/apache2/sites-available/000-default.conf"

    # Écriture du contenu dans le fichier
    with open(apache_conf_path, 'w') as apache_conf_file:
        apache_conf_file.write(apache_conf_content)

    print(f"Fichier de configuration Apache créé : {apache_conf_path}")

def restart_apache():
    subprocess.run(["sudo", "systemctl", "restart", "apache2"])

if __name__ == "__main__":
    configure_apache()
    restart_apache()

