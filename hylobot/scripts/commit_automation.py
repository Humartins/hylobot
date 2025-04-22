import subprocess

# Caminho fixo do script PS1
COMMIT_PS1_PATH = "C:/Users/Humberto Martins/Desktop/Hylo/hylobot/scripts/commit.ps1"

def obter_mensagem_commit():
    mensagem = input("Digite a mensagem de commit (deixe em branco para usar a mensagem padrão): ")
    return mensagem if mensagem else "Commit geral com as últimas alterações"

def atualizar_mensagem_commit(mensagem):
    with open(COMMIT_PS1_PATH, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if "git commit -m" in line:
            lines[i] = f'git commit -m "{mensagem}"\n'
            break

    with open(COMMIT_PS1_PATH, "w") as file:
        file.writelines(lines)

def rodar_commit():
    result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", COMMIT_PS1_PATH], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("[❌] Algo deu errado no commit ou push:")
        print(result.stderr)

        # Tenta resolver automaticamente se for erro de push
        if "Updates were rejected" in result.stderr:
            print("[🔁] Corrigindo: fazendo pull com rebase e tentando push novamente...")
            try:
                subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True)
                subprocess.run(["git", "push", "origin", "main"], check=True)
                print("[✅] Push realizado com sucesso após rebase.")
            except subprocess.CalledProcessError as e:
                print("[❌] Falha ao fazer rebase/push. Verifique conflitos e resolva manualmente.")

def main():
    mensagem_commit = obter_mensagem_commit()
    atualizar_mensagem_commit(mensagem_commit)
    rodar_commit()

if __name__ == "__main__":
    main()
