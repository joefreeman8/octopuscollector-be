python manage.py dumpdata octopus --output octopus/seeds.json --indent=2
python manage.py dumpdata sightings --output sightings/seeds.json --indent=2
python manage.py dumpdata images --output images/seeds.json --indent=2
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2
