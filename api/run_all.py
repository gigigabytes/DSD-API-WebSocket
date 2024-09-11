import subprocess
import os

# Caminho para os scripts das APIs
api_scripts = {
    'api': 'api.py',
    'books': 'books.py',
    'users': 'users.py',
    'shelf': 'shelf.py'
}

# Função para rodar um script em um novo subprocesso
def run_script(script_name):
    return subprocess.Popen(['python', script_name], cwd=os.getcwd())

# Inicia todos os subprocessos
if __name__ == "__main__":
    processes = []
    try:
        for name, script in api_scripts.items():
            print(f"Starting {name}...")
            process = run_script(script)
            processes.append(process)

        print("All APIs are running. Press Ctrl+C to stop.")
        
        # Mantém os processos rodando
        for process in processes:
            process.wait()
    
    except KeyboardInterrupt:
        print("Shutting down all APIs...")
        for process in processes:
            process.terminate()
        print("All APIs have been stopped.")
