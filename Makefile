makemessages:
	python manage.py makemessages -l de --extension=html,txt,jinja,py

compilemessages:
	python manage.py compilemessages
