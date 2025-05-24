from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tarefas em memória
tarefas = [
    {'id' : 1, 'titulo': 'Estudar Flask', 'concluida': False},
    {'id' : 2, 'titulo': 'Criar API CRUD', 'consluida': False}
]

# Listar todas as tarefas
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

# Obter uma tarefa pelo ID
@app.route('/tarefas/<int:id>', methods=['GET'])
def obter_tarefa(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            return jsonify(tarefa)
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

# Criar nova tarefa
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    nova_tarefa = {
        'id' : len(tarefas) + 1,
        'titulo' : dados['titulo'],
        'concluida' : dados.get('concluida', False)
    }
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

# Atualizar tarefa
@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            dados = request.get_json()
            tarefa['titulo'] = dados.get('titulo', tarefa['titulo'])
            tarefa['concluida'] = dados.get('concluida', tarefa['concluida'])
            return jsonify(tarefa)
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

#Deletar tarefa
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefas.remove(tarefa)
            return jsonify({'mensagem': 'Tarefa removida'})
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
