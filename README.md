# Indian GDP Represented by python.

Simple app to show indian GDP by python plotly and USD to INR currency conversion in latest rates with docker.

## Screenshots



### Installing (for linux).

Prerequisite is that user should have python 3.8^ and poetry.

```sh
git clone git@github.com:shreyanshgautam24/IndianGDP.git
cd indiangdp/
poetry install
poetry shell
flask db init
flask db migrate
flask db upgrade
flask run
```
