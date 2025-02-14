from database import  engine
import models


def test_recreate_table():
    # Deleta as minhas tables do banco de dados
    models.Base.metadata.drop_all(bind=engine)
    # Recria as tabelas no banco de dados
    models.Base.metadata.create_all(bind=engine)
