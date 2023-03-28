# Employee Management System

Developing an application for Employee Management, should be able to add new employees by department,edit and delete the employees.

## Getting Started
To get started with this project, you will need to have the following software installed on your machine:
1. Download and Install [MSSMS](https://www.microsoft.com/en-in/sql-server/sql-server-downloads?rtc=1)(Version: 19.0.2)<br>
* Create database and it's corresponding tables.
2. Download and Install [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/)<br>
3. Download and Install [Node.js](https://nodejs.org/en/download)(version: 18.15.0)<br>
* Install the following NuGet Packages-

  * Microsoft.AspNetCore.Cors
  * Microsoft.AspNetCore.Mvc.NewtonsoftJson
  * System.Data.SqlClient
  * Microsoft.AspNetCore.OpenApi
  
4. Download and Install [Visual Studio Code](https://code.visualstudio.com/Download)(1.76.2)<br>
* Create new react app
```
npx create-react-app my-app
cd my-app
npm start
```
* Now Install CORS by-
``` 
npm install cors
```
 or
* install chrome extention
ALLOW CORS: Access-Control-Allow-Origin

## Technologies Used
This project uses the following technologies:
* ASP.NET Web API
* React
* Bootstrap

## API Endpoints
The API has the following endpoints:

* GET /api/employee - retrieves a list of all employees
* POST /api/employee - adds a new employee
* PUT /api/employee/:id - updates an existing employee by ID
* DELETE /api/employee/:id - deletes an existing employee by ID
