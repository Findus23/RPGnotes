.PHONY: things
all: makemessages compilemessages

makemessages:
	python manage.py makemessages -l de --extension=html,txt,jinja,py --ignore "node_modules/*"

compilemessages:
	python manage.py compilemessages
