## README

### Part 1 - REST API:

To start, we must create a REST-based API using Flask-Restful in Python. This API will contain four endpoints:

1. **/getProducts**: Returns a JSON list of all products stored in our local MongoDB.
2. **/getTitles**: Provides a JSON list of just the names of the products in the database using GraphQL.
3. **/insertProduct**: Allows the insertion of a new item into the database via Postman. Authentication is required using an API key within the URL.
4. **/**: The root page lists the available API URLs and a brief description of their functionality.

### Usage:

1. **/getProducts**: Accesses all products in the database and returns them in JSON format.
2. **/getTitles**: Retrieves only the titles of products from the database using GraphQL.
3. **/insertProduct**: Adds a new product to the database. Requires authentication via an API key.
4. **/**: Displays a list of available API endpoints and their descriptions.

### Implementation Details:

The API is implemented in `sample_api.py`. Each endpoint is described below:

#### /getProducts:

- Retrieves all products from the MongoDB database and returns them as JSON.
- Endpoint: `/getProducts`

#### /getTitles:

- Uses GraphQL to return a schema containing a list of all product titles.
- Endpoint: `/getTitles`

#### /insertProduct:

- Handles POST requests to insert new data into the database.
- Requires authentication via a custom API key.
- Endpoint: `/insertProduct`

#### /:

- Displays a list of available API endpoints and their descriptions.
- Endpoint: `/`

### Part 2: DevOps

In addition to the API development, a continuous integration setup using Jenkins and GitHub has been established.

1. **Jenkins Setup**: Jenkins is connected to the GitHub project to trigger builds upon new commits.

2. **Unit Testing**: Unit tests have been created to ensure the functionality of API endpoints.

3. **Execution via Jenkins**: A `run.sh` script executes both the API file and unit test file sequentially. It is integrated into Jenkins build steps.

### Usage:

1. **Unit Testing**: Ensure that API endpoints are functioning correctly by running unit tests.
2. **Continuous Integration**: Monitor Jenkins builds to verify the successful execution of API and unit tests.

### Conclusion:

This README provides an overview of the implemented REST API and the DevOps setup using Jenkins for continuous integration. For further details, refer to the code files and test results generated.
