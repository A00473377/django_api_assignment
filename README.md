![image](https://github.com/A00473377/django_api_assignment/assets/144714614/d0428662-4ec6-4784-9258-52a9247a9109)

A#: A00473377
Author: Zaid Shaikh
 
HOTEL RESERVATION SYSTEM API
•	Setup and Installation

-	Clone the repository: `git clone https://github.com/A00473377/django_api_assignment.git`
-	Install dependencies: Install all necessary dependencies before running the server
-	Run migrations: `python manage.py migrate`
-	Start the server: `python manage.py runserver`

•	API Endpoints

-	GET /app/hotels/ : List all hotels
-	POST /app/hotels/ : Add a new hotel
-	Required fields: ‘name’, ‘location’, ‘price_per_night’, ‘availability’

•	Example

To add a new hotel:

Json:

POST /app/hotels/
{
    "name": "Sunrise Hotel",
    "location": "Miami",
    "price_per_night": 150.00,
    "availability": true
}
