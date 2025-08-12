````markdown
# Architecture Governance Kit

Kit reutilizável de **quality gates**, **segurança** e **aderência arquitetural** para toda a organização.

---

## Como usar em outro repositório

Crie `.github/workflows/quality-gate.yml` no repositório alvo:

```yaml
name: Quality Gate

on:
  pull_request:
    branches: [ "main", "develop" ]
  push:
    branches: [ "main", "develop" ]

jobs:
  call-governance-kit:
    uses: Rodrigo-Camargo-13/architecture-governance-kit/.github/workflows/quality-gate.yml@v1.0.0
    with:
      enable_dotnet: true
      enable_node: true
    permissions:
      contents: read
      security-events: write
      actions: read
      checks: write
````

Se quiser usar o **CodeQL** do kit:

```yaml
jobs:
  call-codeql:
    uses: Rodrigo-Camargo-13/architecture-governance-kit/.github/workflows/codeql.yml@v1.0.0
    with:
      languages: "javascript-typescript,csharp,python"
    permissions:
      contents: read
      security-events: write
```

---

## Conteúdo do kit

* **Composite Actions**: `setup-node`, `setup-dotnet`, `quality-gate`
* **Workflows reutilizáveis**: Quality Gate, CodeQL, Release
* **Ferramentas**: ADR Lint, Dependency-Cruiser, NetArchTest, Gitleaks, Semgrep, Trivy
* **Score agregado simples** para avaliação final de qualidade

---

## Versionamento

Use **tags SemVer** (ex.: `v1.0.0`).
Os repositórios consumidores fixam a versão por tag e atualizam quando desejarem.

---

## Licença

Escolha a licença conforme política interna (MIT/Apache-2.0).
Exemplo MIT:

```text
MIT License
Copyright (c) 2025 Rodrigo...
[texto padrão MIT]
```

---

## Publicar a primeira versão

Após o push do `main`, crie a tag:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Agora, em qualquer repositório consumidor, basta referenciar:

```yaml
uses: Rodrigo-Camargo-13/architecture-governance-kit/.github/workflows/quality-gate.yml@v1.0.0
```