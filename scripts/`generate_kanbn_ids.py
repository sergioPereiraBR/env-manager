import re
import os

# Caminho para o arquivo principal do Kanbn
KANBN_FILE = ".kanbn/index.md"

def get_next_task_id():
    """Gera o próximo ID de tarefa (ex: TASK-001)."""
    task_ids = []
    if os.path.exists(KANBN_FILE):
        with open(KANBN_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            # Encontra todos os IDs de tarefas existentes
            matches = re.findall(r"- ID: TASK-(\d+)", content)
            if matches:
                task_ids = [int(match) for match in matches]
    next_id = max(task_ids) + 1 if task_ids else 1
    return f"TASK-{next_id:03d}"

def get_next_subtask_id(parent_task_id):
    """Gera o próximo ID de subtarefa para uma tarefa pai (ex: TASK-001-ST01)."""
    with open(KANBN_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        # Encontra todas as subtarefas da tarefa pai
        pattern = rf"{parent_task_id}-ST(\d+)"
        matches = re.findall(pattern, content)
        if matches:
            subtask_numbers = [int(match) for match in matches]
            next_num = max(subtask_numbers) + 1
        else:
            next_num = 1
    return f"{parent_task_id}-ST{next_num:02d}"

def add_task(title, description=""):
    """Adiciona uma nova tarefa com ID único."""
    task_id = get_next_task_id()
    new_task = f"- {title}\n  - ID: {task_id}\n  - Description: {description}\n"
    with open(KANBN_FILE, "a", encoding="utf-8") as f:
        f.write(new_task + "\n")
    print(f"Tarefa criada: {task_id}")

def add_subtask(parent_task_id, title, description=""):
    """Adiciona uma subtarefa com ID único e tag vinculada à tarefa pai."""
    subtask_id = get_next_subtask_id(parent_task_id)
    new_subtask = f"  - {title}\n    - ID: {subtask_id}\n    - Description: {description}\n    - Tag: relation:{parent_task_id}\n"
    with open(KANBN_FILE, "r+", encoding="utf-8") as f:
        content = f.read()
        # Localiza a tarefa pai e insere a subtarefa
        pattern = rf"({parent_task_id}.*?)(\n\n|\Z)"
        updated_content = re.sub(
            pattern,
            lambda m: m.group(1) + "\n" + new_subtask + "\n",
            content,
            flags=re.DOTALL
        )
        f.seek(0)
        f.write(updated_content)
        f.truncate()
    print(f"Subtarefa criada: {subtask_id}")

# Exemplo de uso
if __name__ == "__main__":
    # Adicionar uma nova tarefa
    add_task("Implementar login", "Criar tela de autenticação")
    
    # Adicionar subtarefas para a tarefa recém-criada
    add_subtask("TASK-001", "Validar campos", "Verificar email e senha")
    add_subtask("TASK-001", "Conectar ao banco", "Integrar com PostgreSQL")