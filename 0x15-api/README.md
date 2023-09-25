# API Cheatsheet

## HTTP Methods

- **GET**: Retrieve data from the server.
- **POST**: Create new data on the server.
- **PUT**: Update existing data on the server.
- **DELETE**: Remove data from the server.

## HTTP Status Codes

- **200 OK**: Successful request.
- **201 Created**: Resource created successfully.
- **204 No Content**: Request successful, but no response data.
- **400 Bad Request**: Invalid request.
- **401 Unauthorized**: Authentication required or failed.
- **403 Forbidden**: Authentication succeeded, but access is denied.
- **404 Not Found**: Resource not found.
- **500 Internal Server Error**: Server error.

## RESTful API Design

- Use nouns for resource names (e.g., `/users`, `/products`).
- Use HTTP methods to perform actions on resources.
- Keep URLs simple and avoid using verbs (e.g., use `/create` instead of `/add`).
- Use plural nouns for resource collections (e.g., `/users` instead of `/user`).

## Request Headers

- **Authorization**: Include tokens or credentials for authentication.
- **Content-Type**: Specify the format of the request body (e.g., `application/json`).
- **Accept**: Specify the desired response format (e.g., `application/json`).

## Request Parameters

- **Query Parameters**: Used in GET requests to filter, sort, or paginate data (e.g., `?page=1&limit=10`).
- **Path Parameters**: Used to specify a variable in the URL path (e.g., `/users/{id}`).
- **Request Body**: Contains data for POST or PUT requests (e.g., JSON or XML).

## Response Body

- Typically in JSON format.
- Contains data related to the requested resource.

## Authentication

- Use API keys, tokens, or OAuth for authentication.
- Secure sensitive data and endpoints.

## Rate Limiting

- Implement rate limiting to prevent abuse and ensure fair usage.

## Error Handling

- Return clear error messages in the response body.
- Use appropriate HTTP status codes.

## Versioning

- Include a version number in the API URL (e.g., `/v1/users`).
- Maintain backward compatibility when making changes.

## Pagination

- Use pagination for large collections of data.
- Include `page` and `limit` parameters in the query.

## Examples

### GET Request
```
http
GET /api/users
```

## POST Request
```
POST /api/users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "johndoe@example.com"
}
```

## PUT Request
```
PUT /api/users/123
Content-Type: application/json

{
  "name": "Updated Name"
}
```


## DELETE Request

```DELETE /api/users/123```
