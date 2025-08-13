$env:PYTHONPATH = "$env:PYTHONPATH;$(Get-Location)"
alembic revision --autogenerate -m $args[0]