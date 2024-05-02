Electronics Vendor Django Project

Project Overview
This Django-based application simulates an electronics vendor akin to major retailers such as Best Buy. It is designed to handle both online and in-store sales operations, providing functionalities for product browsing, order management, and customer interactions.

Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher
- pip (Python package installer)

Installation Instructions:

Clone the Project:

To get started, clone the repository to your local machine:

git clone https://github.com/MaadRC/electronics_vendor.git
cd electronics_vendor

Set Up a Virtual Environment (Recommended):

Using a virtual environment is recommended to isolate package dependencies. To set up and activate a virtual environment:

python -m venv myprojectenv
source myprojectenv/bin/activate  # On Windows use `myprojectenv\Scripts\activate`

Install Dependencies:

Install the required Python packages by running:

pip install -r requirements.txt

Configuration:

Configure the Django settings in the `settings.py` file within the `electronics_vendor` directory. Adjust the database settings and other configurations as necessary.

Database Setup:

Initialize the database by running migrations:

python manage.py migrate

Running the Application:

To start the Django development server, run:

python manage.py runserver

Once the server is running, access the application in your web browser at `http://localhost:8000`.

Features
- Product Management: Add, update, and remove products.
- Order Processing: Handle online and in-store orders seamlessly.
- Customer Management: Register and manage customer accounts.
- Sales Reporting: Access detailed reports for business analysis.

To run tests, use the following command:
python manage.py test

Contributions to this project are welcome! Please review the current issues and propose your changes via pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Ahmaad Chapman - (https://github.com/MaadRC)

