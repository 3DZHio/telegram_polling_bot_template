![Static Badge](https://img.shields.io/badge/Python-008000?style=for-the-badge&logo=python&logoColor=white&link=https://www.python.org/downloads/)
![Static Badge](https://img.shields.io/badge/ReDiS-d92b09?style=for-the-badge&logo=redis&logoColor=white&link=https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/)
![Static Badge](https://img.shields.io/badge/PostgreSQL-3a6790?style=for-the-badge&logo=postgresql&logoColor=white&link=https://www.postgresql.org/download/linux/)

## 🔗 REPOSITORY

```shell
git clone "https://github.com/3DZHio/telegram_polling_bot_template.git"
```

---

## ⚙️ DEPENDENCIES

### [Install Docker](https://www.docker.com/)

> [!IMPORTANT]
> Perform Actions in Project Folder
> ```shell
> cd <PROJECT_FOLDER>
> ```

### ReName `.env.example` to `.env`

```shell
mv .env.example .env
```

### Configure `.env`

```shell
vi .env || nano .env
```

### PreRequisites

```shell
chmod +x prerequisites.sh
./prerequisites.sh
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