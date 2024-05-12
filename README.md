# wingz

RESTful API for managing ride information

## Development

```
# build docker container
make build

# start docker container
make up

# run migrations
make migrate

# create super user
make superuser

# serve locally on http://localhost:8000
# CTRL-C will stop the development server
make serve

# stop docker container
make down
```

### OpenAPI Schema

Available as both SwaggerUI ([http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)) and Redoc ([http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/))

## Design Decisions

Some notes on design decisions

### Authentication

- Defined custom user because modifying default user after migrations have been created is a royal pain
- Extended `AbstractBaseUser` instead of `AbstractUser` in case the method of authentication changes

### Database

- Set the default `on_delete` behavior to `models.SET_NULL` out of convenience
- Used `DecimalField` versus `FloatField` (as specified in the requirements) since decimal math is more precise compared to float math
    - Based on whether we are reading or writing more frequently to the database, "good enough" float math may be worth the performance benefits
- Chose Postgres over MySQL because Postgres offers geospatial extensions
- Calculated distance to pickup using the [Haversine distance](https://en.wikipedia.org/wiki/Haversine_formula) due to simpler math. If greater accuracy is needed, worth looking into proper geodesic distance using [Vincenty algorithm](https://en.wikipedia.org/wiki/Vincenty%27s_formulae)

## Other Notes

Miscellaneous notes and features to be implemented

- Use `django-environ` to load settings from `.env` based on environment
- Disable `django-silk` or require authentication
- Validate user phone numbers as [E.164](https://en.wikipedia.org/wiki/E.164)
- Lint with `flake8`
- Write unit tests
