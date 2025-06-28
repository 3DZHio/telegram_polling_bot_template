### VARIABLE ###
## MAIN ##
S=sudo
E=@echo

## DOCKER ##
D=docker

## DOCKER COMPOSE ##
DC=docker compose



### ACTION ###
## MAIN ##
prerequisites:
	chmod +x prerequisites.sh
	./prerequisites.sh


## PYTHON ## 
venv_requirements:
	python3 -m venv venv
	bash -c "source venv/bin/activate && pip install -r requirements.txt"


## DOCKER ##
ps:
	$(S) $(D) ps --all

rm:
	$(E) USAGE: make rm rm=
	$(S) $(D) rm --force $(rm)

images:
	$(S) $(D) images --all

rmi:
	$(E) USAGE: make rmi rmi=
	$(S) $(D) rmi --force $(rmi)

prune:
	$(S) $(D) system prune --volumes --force

exec:
	$(E) USAGE: make exec exec=
	$(S) $(D) exec -it $(exec)


## DOCKER COMPOSE ##
build:
	$(S) $(DC) build

up:
	$(S) $(DC) up --detach --remove-orphans

down:
	$(S) $(DC) down

logs:
	$(E) USAGE: make logs logs=
	$(S) $(DC) logs --follow $(logs)
