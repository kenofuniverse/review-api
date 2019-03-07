#!/bin/bash
echo "================== Installing Dependencies =================="
pip install -r requirements.txt
echo "================== Migrating =================="
python manage.py migrate
echo "================== Creating Super User =================="
python manage.py createsuperuser
echo "Thank You!!!"