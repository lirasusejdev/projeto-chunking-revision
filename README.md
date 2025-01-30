# Chunking - Aprendizagem por Blocos

## Descrição do Projeto
Este projeto foi criado por LIS REGINE AMARAL - baseado no curso: “Oracle Next Education F2 T8” - Oracle ONE - Br Geral 8. O objetivo da implementação é a criação de um sistema de cálculo de revisões baseado no método **Chunking**, uma [técnica de aprendizagem](https://cursos.alura.com.br/forum/topico-conceitos-de-chunks-436017) que divide o estudo em blocos menores e utiliza revisões espaçadas para melhorar a retenção de informações.

## Funcionamento
O script em **Python** recebe uma data e hora de estudo inicial e calcula automaticamente as datas recomendadas para revisões futuras, seguindo o seguinte cronograma:

- **Revisão 1**: Algumas horas após o estudo inicial (6 horas depois).
- **Revisão 2**: 24 horas depois.
- **Revisão 3**: 1 semana depois.
- **Revisão 4**: 1 mês depois.

## Tecnologias Utilizadas
- Python 3
- Biblioteca `datetime`

## Como Executar o Projeto
### Pré-requisitos
- Ter o **Python 3** instalado na máquina.

### Passos
1. [Clone](https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository) este repositório preferencialmente com SSH:
   ```bash
   git clone git@github.com:lirasusejdev/projeto-chunking-revision.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd nome-do-repositorio
   ```
3. Execute o script se estiver usando Windows:
   ```bash
   python calculo_revisoes.py
   ```

Caso esteja utilizando **Mac/Linux**, pode ser necessário rodar:
   ```bash
   python3 calculo_revisoes.py
   ```

## Exemplo de Uso
Ao executar o script, o usuário insere uma data e hora inicial, e o programa retorna as datas sugeridas para revisão:

```
Estudo inicial: 01/02/2025 10:00
Revisão 1 (mesmo dia): 01/02/2025 16:00
Revisão 2 (24h depois): 02/02/2025 10:00
Revisão 3 (1 semana depois): 08/02/2025 10:00
Revisão 4 (1 mês depois): 01/03/2025 10:00
```

## Contribuições
Contribuições são bem-vindas! Para contribuir:
1. Faça um **fork** deste repositório.
2. Crie uma **branch** para sua funcionalidade:
   ```bash
   git checkout -b minha-nova-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m "Adiciona nova funcionalidade X"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-nova-feature
   ```
5. Abra um **Pull Request**.

## Licença
Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
Este projeto foi criado por LIS REGINE AMARAL - baseado no curso: “Oracle Next Education F2 T8” - Oracle ONE - Br Geral 8.

