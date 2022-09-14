# Shumba Money Coding Challenge

Author: [Andile Jaden Mbele](https://andilembele.netlify.app/)

Shumba Money is a money transfer service that allows one to send money from countries in the diaspora to recipients in Zimbabwe. You are required to build a basic web platform that Shumba Money customers can use to list their recipients. Your web platform should also make it possible for senders to update, create or delete recipients.

## Challenge Specifications

### The web platform must meet the following specifications:

1. It should comprise both a REST API and a web application
2. The REST API should be built using Spring Boot, NodeJS or NestJS. Using Django
3. The REST API data must be persisted using MySQL, MongoDB or Postgres: I am going with Postgres
4. The REST API must also use the de facto object relational mapper of the framework you choose to build it in (e.g Typeorm or Mongoose for NodeJs and Hibernate for Spring Boot). Django ORM
5. The web application should be built using Angular 2+ or ReactJS. I chose ReactJS
6. Your web application must also be user friendly and aesthetically pleasing in a way that adheres to the Shumba Money brand

## API Structure

1. Customer in this case will also be a user of the web application.Different users can have multiple recipients.
2. A recipient can belong to multiple users in the same application
3. A user can have multiple transactions

### API Design

```json
{
  "id": "string",
  "firstName": "string",
  "middleName": "string",
  "lastName": "string",
  "email": "string",
  "countryOfResidence": "string",
  "phoneNumber": "string",
  "password": "string",
  "recipients": [
    {
      "id": "string",
      "firstName": "string",
      "middleName": "string",
      "lastName": "string",
      "email": "string",
      "phoneNumber": "string",
      "countryOfResidence": "string",
      "cityOrTown": "string",
      "transactions": [
        {
          "id": "string",
          "amount": "number",
          "currency": "string",
          "status": "string",
          "sender": "string",
          "recipient": "string",
          "createdAt": "date",
          "updatedAt": "date"
        }
      ]
    }
  ]
}
```

## Frontend Design

The frontend design should be as simple as possible. It should have the following pages:

1. An auth page
2. A landing page
3. A page to list all recipients
4. A page to create a new recipient
5. A page to update a recipient

## How to use the API

### 1. Start the project on localhost

```python
$ python manage.py runserver
```

### 2. Create a customer

```json
{
  "firstName": "Andile",
  "middleName": "Jaden",
  "lastName": "Mbele",
  "email": "andilembele020@gmail.com",
  "countryOfResidence": "Australia",
  "phoneNumber": "778613888",
  "phoneCode": "+61",
  "password": "qwerty#2022"
}
```

### 3. Login

```json
{
}
```

### 4. Create a recipient

```json
{
}
```

### 5. Update a recipient

```json
{
}
```

### 6. Delete a recipient

API Endpoint: http://localhost:5001/api/v1/recipients/6313018f7f44a99dfd853b7a

```json
{
}
```

### 7. List all recipients

```json
{
  
}
```

### 8. Create a transaction

```json
{
}
```

### 9. Update a transaction

```json
{
}
```

### 10. Delete a transaction

```json
{
}
```

### 11. List all transactions

```json
{
}
```

## How to use the Reactjs Fronted App connected to the API

### 1. Start the project on localhost

```python
$ python manage.py runserver
```

### 2. Open your browser

## Submission

1. Fork this repository
2. Create a new branch with your name
3. Commit your code to the branch you created
4. Create a pull request to the master branch of this repository
5. Send an email to [email](mailto:andilembele020@gmail.com)
