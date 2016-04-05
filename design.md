package-name/
\--setup.py
\--README
\--package-name/
    |--__init__.py
    |--models.py
    |--client.py
    |--repl.py       (Use client lib to present a CLI for the REST API)
    |--run.py        (Change user ID, detach from TTY, spawn subprocesses etc)
    |--config.py     (Read things like database URI from the environment)
    |--controllers/  (Business logic.)
    |--resources/    (RESTful HTTP endpoints)
    |--views/        (Static view logic)
    |--templates/    (base.html, index.html, a generic error template that can be filled with the appropriate status code and message)
    |--static/       (CSS, images, fonts, javascript libraries and an app.js if it's a single-page app)