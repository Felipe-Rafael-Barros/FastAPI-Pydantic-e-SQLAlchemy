from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Valores das credenciais do meu PostgreSQL
DATABASE_URL = "postgresql://postgres:adm123@localhost/empresas_obrigacoes" #adm123 é a senha, empresas_obrigacoes é o database que criei

# Criando a engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Criando a base de dados para as tabelas
Base = declarative_base()

# Criando a sessão para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
