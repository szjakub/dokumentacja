# Tworzenie superusera
    docker exec -it cyprus_backend_1 /bin/bash
    python manage.py createsuperuser

jeśli wyświetli się `Bypass password validation and create user anyway? [y/N]:` dajcie `y`

# Endpointy
Backend stoi na porcie 8000

    localhost:8000


### Django admin
Tutaj podajecie credsy superusera, którego storzyliście wcześniej

    /admin/

### API Swagger
    /api/schema/swagger-ui/