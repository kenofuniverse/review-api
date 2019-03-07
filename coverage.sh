#!/bin/bash
echo "================== Running Test =================="
coverage run  manage.py test
echo "================== Generating Report =================="
coverage report -m