#!/bin/bash

source autodeploy_env.sh

PROD=${PRODUCTION:-false}

if [ $# -eq 0 ]
then
	echo -e "\nIniciando servidor zaki..."
	python manage.py runserver
        exit 0
fi;


while [ $# -gt 0 ] ; do
    case $1 in
	-c | --cleandb)
	    echo -e "\nLimpiando Base de Datos... "
	    if [[ $DELETE_DB == true ]] || [[ $PROD == false ]] ; then
		rm db.sqlite3
		rm -rf */_pycache_
		if [[ $SUFFIX == test ]] || [[ $SUFFIX == stage ]] ; then
		    python drop_db.py;
		fi;
	    fi;

	    if [[ $MIGRATIONS == true ]] || [[ $PROD == false ]] ; then
		echo -e "\nAplicando migraciones al ORM..."
		python manage.py check
		python manage.py makemigrations
		python manage.py migrate
	    fi;

	    if [[ $LOADDATA == true ]] || [[ $PROD == false ]] ; then
		echo -e "\Aplicando fictures... "
		python manage.py loaddata perfiles/fixtures/*json
	    fi;
	    exit 0
	    ;;
	-t | --test)
	    echo -e "\nTesting... "
	    python manage.py test
	    exit 0
	    ;;
    esac
    shift
done
