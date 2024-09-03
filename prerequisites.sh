#!/bin/bash


## Variables ##
source .env || source .env.example


## ReName .env.example to .env ##
if [ -f .env.example ]; then
  mv .env.example .env
fi


## GitIgnore ##
if [ "${SAVE_ENV}" == "1" ]; then
    sed -i "s/^.env/##.env/" .gitignore
fi


## Redis Memory OverCommit ##
if [ "$(sudo cat /proc/sys/vm/overcommit_memory)" != "1" ]; then
    echo 1 | sudo tee /proc/sys/vm/overcommit_memory
fi
