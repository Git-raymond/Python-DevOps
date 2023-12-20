import subprocess

def execute_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        print("Résultat de l'exécution de la commande :")
        print(result)
    except subprocess.CalledProcessError as e:
        print("Erreur lors de l'exécution de la commande :")
        print(e.output)

if __name__ == "__main__":
    command_to_execute = input("Entrez la commande à exécuter : ")
    execute_command(command_to_execute)
