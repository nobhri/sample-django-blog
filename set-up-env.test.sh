#!/bin/bash

# Django
echo "SECRET_KEY=$SECRET_KEY" >> .env
echo "DJANGO_ALLOWED_HOSTS=$DJANGO_ALLOWED_HOSTS" >> .env
echo "DEBUG=$DEBUG" >> .env