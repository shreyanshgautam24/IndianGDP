# Indian GDP Represented by python.

Simple app to show indian GDP by python plotly and USD to INR currency conversion in latest rates with docker.

## Screenshots
![Screenshot from 2023-03-10 01-31-58](https://user-images.githubusercontent.com/45899648/224157327-a601a5d2-17e7-46e3-a8a8-6e6e2a83dd3e.png)

### Installing (for linux).

Prerequisite is that user should have python 3.8^ and poetry.

To install Poetry(PYTHON PACKAGING AND DEPENDENCY MANAGEMENT):
curl -sSL https://install.python-poetry.org | python3 -

```sh
git clone git@github.com:shreyanshgautam24/IndianGDP.git
cd IndianGDP/
poetry install
poetry shell
flask db init
flask db migrate
flask db upgrade
flask run
```

http://localhost:5000/
