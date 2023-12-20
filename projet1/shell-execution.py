import subprocess
import sys

def execute_shell_script(script_path, *args):
    try:
        if args:
            command = [script_path, *args]
        else:
            command = [script_path]
            
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        print(f"Résultat de l'exécution du script '{script_path}' avec les paramètres {args} :")
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du script '{script_path}' avec les paramètres {args} :")
        print(e.output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python shell-execution.py <chemin_du_script> [<paramètre1> <paramètre2> ...]")
        sys.exit(1)

    script_path = sys.argv[1]
    arguments = sys.argv[2:]
    execute_shell_script(script_path, *arguments)






