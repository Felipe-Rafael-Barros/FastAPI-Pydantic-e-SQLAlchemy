from fastapi.testclient import TestClient
from main import app
from recreate_bank import test_recreate_table #Função que criei para recriar o banco de dados
from test_01_create_empresa import test_create_empresa #função para criar uma nova empresa
from test_05_create_obrigacoes import test_create_obrigacao #Adiciono obrigação

client = TestClient(app)

def test_delete_obrigacoes():
    response = client.delete(f"/obrigacoes/{1}") #Id da obrigação que quero DELETAR
    # Verifica se a requisição foi bem-sucedida
    assert response.status_code in [200, 204]  
