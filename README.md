# devops-testing 🧪

Pipeline CI/CD com testes automatizados, linting e build Docker.

## Pipeline

A cada `git push` o pipeline executa automaticamente:

1. **Testes unitários** com pytest (5 testes)
2. **Verificação de qualidade** com flake8
3. **Coverage report** gerado e salvo como artefato
4. **Build e push** da imagem Docker (só se testes passarem)

## Testes

```bash
pip install -r requirements.txt
python3 -m pytest tests/ -v
```

## Stack

- GitHub Actions
- pytest + pytest-cov
- flake8
- Docker

## Autor

**Henrique Sattolo** — github.com/henriquesattolo
