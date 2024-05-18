import subprocess
import sys

def check_install_dependencies(dependencies):
    try:
        for dependency in dependencies:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dependency])
        print("Todas as dependências estão instaladas.")
    except subprocess.CalledProcessError:
        print("Algumas dependências estão faltando ou houve um erro durante a instalação.")

if __name__ == "__main__":
    dependencies = ["websockets", "psutil", "pygetwindow", "pywin32", "pynput"]
    check_install_dependencies(dependencies)
