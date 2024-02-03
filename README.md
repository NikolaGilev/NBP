# NBP

# Postgres

install pyenv which is a python package version management tool popular in the python community.

```sh
$ pip install pyenv-win
```

Now we need to add pyenv to our environment variables i.e. add two PATH variables:

- %USERPROFILE%\.pyenv\pyenv-win\shims
- %USERPROFILE%\.pyenv\pyenv-win\bin

alternatively we can install pyenv using windows power-shell like so:

```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

If Admin permissions aren't granted the following error will arise:

... File C:\Users\kok1\_\install-pyenv-win.ps1 cannot be loaded because running scripts is disabled on this system...

In order to fix this we need to give power-shell Admin privilages so it can successfully run the script:

```powershell
Set-ExecutionPolicy -Scope CurrentUser
```

When prompted for the "ExecutionPolicy", insert "RemoteSigned". Now rerun the first script and it should install pyenv.

==============================================================================

TODO: Idk if above is even necessary for creating a pipenv

run

```sh
$ pipenv --python 3.10
```

You should get the following message:

- "Successfully created virtual environment!"

To activate this project's virtualenv, run the following:

```sh
$ pipenv shell
```

Now since we are in the virtual env we can start adding necessary dependencies. We can add them using this command:

```sh
$ pipenv install %package_name%
```

the full list of installed packages will be in the "Pipfile" or we can generate a report with

```sh
$ pipenv requirements > requirements.txt
```

Tables look like this:

```sql
CREATE TABLE collections (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    movie_id INT,
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    movie_id INT,
);

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    imdb_id VARCHAR(20) NOT NULL,
    title VARCHAR(255) NOT NULL,
    for_adults BOOLEAN,
    collections_id INT,
    budget BIGINT,
    production_companies_id INT,
    production_countries_id INT,
    original_language VARCHAR(10) NOT NULL,
    original_title VARCHAR(255) NOT NULL,
    overview TEXT,
    popularity BIGINT,
    release_date DATE,
    revenue BIGINT,
    runtime FLOAT,
);

CREATE TABLE cast (
    id SERIAL PRIMARY KEY,
    movie_id INT,
    name VARCHAR(255) NOT NULL,
    character VARCHAR(255) NOT NULL,
    gender INT
);

CREATE TABLE crew (
    id SERIAL PRIMARY KEY,
    movie_id INT,
    department VARCHAR(255) NOT NULL,
    job VARCHAR(255) NOT NULL,
    gender VARCHAR(255),
    name VARCHAR(255) NOT NULL
);

CREATE TABLE keywords (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    movie_id INT,
);
```
