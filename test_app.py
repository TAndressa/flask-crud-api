import pytest

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_listar_tarefas(client):
    response = client.get('/tarefas')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_criar_tarefa(client):
    nova_tarefa = {'titulo': 'Tarefa de teste', 'concluida': False}
    response = client.post('/tarefas', json=nova_tarefa)
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['titulo'] =='Tarefa de teste'
    assert json_data['concluida'] == False

def test_obter_tarefa_existente(client):
    response = client.get('/tarefas/1')
    assert response.status_code == 200
    assert 'titulo' in response.get_json()

def teste_obter_tarefa_inexistente(client):
    response = client.get('/tarefas/999')
    assert response.status_code == 404

def test_atualizar_tarefa(client):
    atualizacao = {'titulo': 'Atualizada', 'concluida': True}
    response = client.put('/tarefas/1', json=atualizacao)
    assert response.status_code == 200
    assert response.get_json()['titulo'] == 'Atualizada'

def test_deletar_tarefa(client):
    response = client.delete('/tarefas/1')
    assert response.status_code == 200
    assert response.get_json()['mensagem'] =='Tarefa removida'