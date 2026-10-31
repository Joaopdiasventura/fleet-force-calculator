# Fleet Force Calculator

Calculadora de custos operacionais de frota desenvolvida em **Python**, como entrega da **Sprint 1 — Fundamentos da Calculadora de Frota** do Challenge Sem Parar Empresas.

## Objetivo

Receber dados de uma frota, consolidar despesas operacionais e apresentar indicadores de custo no terminal. Esta versão utiliza entrada manual, sem banco de dados, API ou dependências externas.

## Requisitos

- Python **3.10 ou superior**.
- Terminal (PowerShell, Prompt de Comando, bash etc.).
- Não é necessário instalar bibliotecas.

## Execução

No diretório `fleet-force-calculator`:

```bash
python main.py
```

Em ambientes que utilizam `python3`:

```bash
python3 main.py
```

Preencha os campos solicitados. O programa exibirá o relatório e oferecerá a opção de calcular outra frota/período.

**Formato de números:** informe `1234.50` ou `1234,50`, **sem separadores de milhar**. Não informe símbolo de moeda.

## Informações solicitadas

- Período de referência (texto, por exemplo `10/2026`)
- Quantidade de veículos (inteiro positivo)
- Distância total percorrida (km)
- Litros de combustível consumidos
- Gastos em reais com combustível, manutenção, pedágios, multas, impostos e outros custos

Os valores monetários, a distância e o consumo devem ser maiores ou iguais a zero. Um período não pode ficar vazio.

## Indicadores

1. **Custo total:** soma das seis categorias de despesa.
2. **Custo médio por veículo:** custo total ÷ quantidade de veículos.
3. **Custo por km:** custo total ÷ distância total.
4. **Participação de cada categoria:** gasto da categoria ÷ custo total × 100.
5. **Maior despesa:** categoria com o maior valor informado.
6. **Consumo médio (adicional):** distância ÷ litros consumidos (km/L).
7. **Custo de combustível por km (adicional):** despesa com combustível ÷ distância.

## Exemplo de entrada

| Campo | Valor |
| --- | ---: |
| Período | 10/2026 |
| Veículos | 40 |
| Distância | 85000 km |
| Combustível consumido | 9500 L |
| Combustível | R$ 54000 |
| Manutenção | R$ 18000 |
| Pedágios | R$ 12000 |
| Multas | R$ 3000 |
| Impostos | R$ 8000 |
| Outros | R$ 2000 |

Resultados principais: **custo total R$ 97.000,00**, **R$ 2.425,00 por veículo**, **R$ 1,14/km**, e **combustível como maior despesa (55,67%)**.

## Estrutura

```text
fleet-force-calculator/
├── src/
│   ├── __init__.py
│   ├── calculations.py  # Funções matemáticas
│   ├── input.py         # Coleta/validação das entradas
│   └── report.py        # Formatação e apresentação
├── tests/
│   └── test_calculations.py
├── main.py              # Menu e fluxo principal
└── README.md
```

## Testes

```bash
python -m unittest discover -s tests -v
```

## Fundamentos de Python empregados

Variáveis, tipos (`int`, `float`, `str`), operadores, `input` e `print`, estruturas `if`, `while`, `for`, dicionários, funções, tratamento de exceções e organização em módulos.

## Roadmap do Challenge

- **Sprint 1 (esta entrega):** entradas manuais, cálculos e relatório no terminal.
- **Sprint 2 (futura):** persistência e histórico para análise dos custos.
- **Sprint 3 (futura):** diagnóstico, benchmark e recomendações.
- **Sprint 4 (futura):** integração do produto e relatório executivo.

Esta versão **não** implementa persistência, diagnósticos automatizados, benchmarks externos nem IA. A categoria com maior despesa é apenas uma indicação inicial, não um diagnóstico de ineficiência.
