![Static Badge](https://img.shields.io/badge/Python-008000?style=for-the-badge&logo=python&logoColor=white&link=https://www.python.org/downloads/)
![Static Badge](https://img.shields.io/badge/ReDiS-d92b09?style=for-the-badge&logo=redis&logoColor=white&link=https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/)
![Static Badge](https://img.shields.io/badge/PostgreSQL-3a6790?style=for-the-badge&logo=postgresql&logoColor=white&link=https://www.postgresql.org/download/linux/)


## 🛠️ DEPENDENCIES

> [!IMPORTANT]
> ```shell
> Windows is NOT Supported
> ```

### Install Docker

```shell
https://www.docker.com/
```


---


## 🔗 REPOSITORY

```shell
git clone "https://github.com/3DZHio/telegram_polling_bot_template.git" $HOME/Documents/telegram_polling_bot_template
cd $HOME/Documents/telegram_polling_bot_template
```


---


## ⚙️ SETUP

### Virtual Environment | Requirements

```shell
make venv_requirements
```

### Configure `.env.example`

```shell
vi .env.example || nano .env.example
```

### PreRequisites

```shell
make prerequisites
```


---


## 📦 DOCKER

### 🚀 Build and Up

```shell
make build up
```

### 🛑 Down

```shell
make down
```

> [!TIP]
> 📌 MakeFile Info
> ```shell
> cat Makefile
> ```


---


## TO INSTALL ON SERVER

```shell
cat server.sh
```


---