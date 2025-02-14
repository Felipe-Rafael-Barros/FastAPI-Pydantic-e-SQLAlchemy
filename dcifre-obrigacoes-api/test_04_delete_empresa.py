from fastapi.testclient import TestClient
from main import app
from recreate_bank import test_recreate_table #Função que criei para recriar o banco de dados
from test_01_create_empresa import test_create_empresa #Adiciono empresa









# Instância do TestClient para testar a API
client = TestClient(app)
def test_delete_empresa():
    response = client.delete(f"/empresas/{1}") #Id da empresa que quero DELETAR

    # Verifica se a requisição foi bem-sucedida
    assert response.status_code in [200, 204]  

