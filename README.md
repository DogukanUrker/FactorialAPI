# Factorial Calculator API

This is a simple Flask API that calculates the factorial of a given number.

## Endpoints

The API has three endpoints that all perform the same operation:

- `/calculate/<number>`
- `/factorial/<number>`
- `/<number>`

Replace `<number>` with the number you want to calculate the factorial of.

## Errors

If the input is not a valid number, or if the number is negative, the API will return an error message in the following format:

```json
{
  "error": "Please enter a valid number"
}
```
