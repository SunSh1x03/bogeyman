# Bogeyman

Ferramenta simples de linha de comando para criptografar e descriptografar
arquivos utilizando chaves simétricas gerenciadas localmente. Os scripts usam o
[Fernet](https://cryptography.io/en/latest/fernet/) da biblioteca
`cryptography` para oferecer criptografia autenticada de maneira prática.

## Requisitos

- Python 3.8 ou superior
- Dependência Python: [`cryptography`](https://pypi.org/project/cryptography/)

Instale a dependência com:

```bash
pip install cryptography
```

## Uso

Os scripts operam diretamente sobre o arquivo informado, ou seja, o conteúdo é
substituído pela versão criptografada/descriptografada. Por padrão a chave é
armazenada no arquivo `bogeyman.key` no diretório atual.

### Gerar chave e criptografar

```bash
python encrypt.py caminho/para/arquivo.txt
```

- Se `bogeyman.key` não existir, uma nova chave é criada e salva.
- Use `--key` para informar um caminho diferente para o arquivo de chave.

### Descriptografar

```bash
python decyrpt.py caminho/para/arquivo.txt
```

- É necessário possuir a mesma chave usada na criptografia.
- Utilize `--key` quando a chave estiver em outro local.

## Observações

- Faça backup dos arquivos antes de executá-los, pois os scripts atuam
  in-place.
- Mantenha a chave (`.key`) em local seguro. Sem ela não será possível recuperar
  o conteúdo original.

![batutinhas](https://user-images.githubusercontent.com/6726442/130009612-d82ad817-470d-4667-8b9c-b31aa8cac5f2.gif)
