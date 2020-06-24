#!/bin/bash
echo What would you like to commit?
read var_commit
git pull
git add -A
git commit -m "$var_commit"
git push