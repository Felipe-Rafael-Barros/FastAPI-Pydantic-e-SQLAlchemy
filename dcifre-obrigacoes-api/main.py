#Felipe Rafael Barros da Silva

# 1) De start no terminal: uvicorn main:app --reload
# 2) Para realizar o test, vá ao diretório principal("Projeto Dcifre") e execute "pytest -v"
# 3) Para consultas manuais: http://localhost:8000/docs#/

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import SessionLocal, engine
import models
from schemas import EmpresaCreate, Empresa, ObrigacaoCreate, Obrigacao


# Gera as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas para Empresas
@app.post("/empresas/", response_model=Empresa)
def criar_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = models.Empresa(**empresa.model_dump())
    try:
        db.add(db_empresa)
        db.commit()
        db.refresh(db_empresa)
        return db_empresa
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="CNPJ já cadastrado")

@app.get("/empresas/{empresa_id}", response_model=Empresa)
def ler_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@app.put("/empresas/{empresa_id}", response_model=Empresa)
def atualizar_empresa(empresa_id: int, empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    
    for key, value in empresa.model_dump().items():
        setattr(db_empresa, key, value)
    
    try:
        db.commit()
        db.refresh(db_empresa)
        return db_empresa
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="CNPJ já cadastrado")

@app.delete("/empresas/{empresa_id}", response_model=dict)
def excluir_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    
    db.delete(db_empresa)
    db.commit()
    return {"message": "Empresa excluída com sucesso"}

# Rotas para Obrigações
@app.post("/obrigacoes/", response_model=Obrigacao)
def criar_obrigacao(obrigacao: ObrigacaoCreate, db: Session = Depends(get_db)):
    db_obrigacao = models.Obrigacao(**obrigacao.model_dump())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.get("/obrigacoes/{obrigacao_id}", response_model=Obrigacao)
def ler_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = db.query(models.Obrigacao).filter(models.Obrigacao.id == obrigacao_id).first()
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    return db_obrigacao

@app.put("/obrigacoes/{obrigacao_id}", response_model=Obrigacao)
def atualizar_obrigacao(obrigacao_id: int, obrigacao: ObrigacaoCreate, db: Session = Depends(get_db)):
    db_obrigacao = db.query(models.Obrigacao).filter(models.Obrigacao.id == obrigacao_id).first()
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    
    for key, value in obrigacao.model_dump().items():
        setattr(db_obrigacao, key, value)
    
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.delete("/obrigacoes/{obrigacao_id}", response_model=dict)
def excluir_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = db.query(models.Obrigacao).filter(models.Obrigacao.id == obrigacao_id).first()
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    
    db.delete(db_obrigacao)
    db.commit()
    return {"message": "Obrigação excluída com sucesso"}
