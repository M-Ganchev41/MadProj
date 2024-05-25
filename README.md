### Requirements

-   Docker Desktop or similar container tool for local development.

## Data Model

![Data Model](data-model.png 'System Architecture Diagram')

### Setup

Execute the following commands in the root directory of the project:

```bash
docker-compose up -d

docker-compose down

docker-compose up -d
```

!(Failed to successfuly make service_1 wait for the db service to build its volume so it refuses connection on first composition)

### Usage

To reach the Swagger UI, open the following link in your web browser:

-   http://localhost:8080/api/v1/service/docs

### Known issues

-   You have to compose docker twice on first initialization(or after running docker-compose down -v).
-   Create/Post requests do not return the ID of the table. This is caused by the ID being unnecessary in the request itself as it is auto-incremented by the database. If the ID is enforced by the response model the request returns error code 500 but still functions as intended.

### Pandas Function(s)

-   Function (Filter Pandas) uses Pandas to join 3 tables(car, make, model(refer to data_model.png)) and filters cars with higher horsepower than the one entered in the request.
