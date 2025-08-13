$env:PYTHONPATH = "$env:PYTHONPATH;$(Get-Location)"
alembic upgrade head