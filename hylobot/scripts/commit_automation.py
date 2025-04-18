import subprocess

# Função para pedir a mensagem do commit
def obter_mensagem_commit():
    mensagem = input("Digite a mensagem de commit (deixe em branco para usar a mensagem padrão): ")
    return mensagem if mensagem else "Commit geral com as últimas alterações"

# Função para atualizar o arquivo PowerShell com a nova mensagem de commit
def atualizar_mensagem_commit(mensagem):
    caminho_commit_ps1 = "C:/Users/Humberto Martins/Desktop/Hylo/hylobot/scripts/commit.ps1"  # Altere para o caminho correto, se necessário
    with open(caminho_commit_ps1, "r") as file:
        lines = file.readlines()

    # Substituindo a mensagem de commit no script .ps1
    for i, line in enumerate(lines):
        if "git commit -m" in line:
            lines[i] = f'git commit -m "{mensagem}"\n'
            break

    with open(caminho_commit_ps1, "w") as file:
        file.writelines(lines)

# Função para rodar o script PowerShell
def rodar_commit():
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "C:/Users/Humberto Martins/Desktop/Hylo/hylobot/scripts/commit.ps1"])

# Função principal
def main():
    mensagem_commit = obter_mensagem_commit()  # Pede a mensagem do commit
    atualizar_mensagem_commit(mensagem_commit)  # Atualiza o commit.ps1 com a mensagem
    rodar_commit()  # Executa o commit via PowerShell

if __name__ == "__main__":
    main()
