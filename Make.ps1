# Make.ps1

# Define common variables
$DJANGO_MANAGE = "python manage.py"
$DOCKER_COMPOSE = "docker-compose"
$DOCKER = "docker"

$BROWSER_PYSCRIPT = @"
    \$rel_current_path = \$args[0]
    \$abs_current_path = [System.IO.Path]::GetFullPath(\$rel_current_path)
    \$uri = "file://" + [System.Uri]::EscapeDataString(\$abs_current_path)
    [System.Diagnostics.Process]::Start("chrome.exe", \$uri)
"@

$PRINT_HELP_PYSCRIPT = @"
    \$regex_pattern = '^([a-zA-Z_-]+):.*?## (.*)$$'

    Get-Content \$PSCommandPath | ForEach-Object {
        if (\$_ -match \$regex_pattern) {
            \$target = \$matches[1]
            \$help = \$matches[2]
            Write-Host ("%-20s %s" -f \$target, \$help)
        }
    }
"@

# Function to display help
function Show-Help {
    Write-Host "Available targets:"
    PowerShell -Command $PRINT_HELP_PYSCRIPT
}

# Function to activate environment
function Activate-Env {
    # Replace with your activation command, e.g., 'poetry shell'
    # Example:
    Invoke-Expression "poetry shell"
}

# Function to prepare environment
function Prepare-Env {
    # Remove 'venv' directory if it exists
    Remove-Item -Path "venv" -Recurse -Force -ErrorAction SilentlyContinue

    # Activate the environment (replace with your activation command)
    Activate-Env

    # Install project dependencies using 'poetry'
    Invoke-Expression "poetry install"
}

# Function to clean up temporary files
function Clean {
    # Remove '.pyc' files
    Get-ChildItem -Path . -Filter *.pyc -File | ForEach-Object {
        Remove-Item -Path \$_.FullName -Force -ErrorAction SilentlyContinue
    }

    # Remove 'venv' directory
    Remove-Item -Path "venv" -Recurse -Force -ErrorAction SilentlyContinue

    # Remove 'htmlcov' directory
    Remove-Item -Path "htmlcov" -Recurse -Force -ErrorAction SilentlyContinue

    # Clean Docker volumes (optional)
    Invoke-Expression "$DOCKER system prune --volumes -f"
}

# Function to run initial migrations and create a superuser
function Migrate {
    Invoke-Expression "$DJANGO_MANAGE migrate"
}

# Function to collect static files for production environment
function Collect-Static {
    Invoke-Expression "$DJANGO_MANAGE collectstatic"
}

# Function to list containers
function List-Containers {
    Invoke-Expression "$DOCKER ps -a"
}

# Function to build Docker containers
function Build-Containers {
    Invoke-Expression "$DOCKER_COMPOSE build"
}

# Function to start Docker containers
function Start-Containers {
    Invoke-Expression "$DOCKER_COMPOSE up -d"
}

# Function to stop Docker containers
function Stop-Containers {
    Invoke-Expression "$DOCKER_COMPOSE down"
}

# Function to run the development server
function Run-Server {
    Invoke-Expression "$DJANGO_MANAGE runserver 0.0.0.0:8000"
}

# Function to deploy the server
function Deploy {
    Build-Containers
    Start-Containers
    Migrate
    Collect-Static
    Run-Server
}

# Function to create Django superuser
function Create-Superuser {
    Invoke-Expression "$DJANGO_MANAGE createsuperuser"
}

# Parse command-line arguments
if ($args.Count -eq 0) {
    Show-Help
    exit
}

# Test target
function Test {
    # Replace with your test command, e.g., 'coverage run -m pytest'
    # Example:
    Invoke-Expression "coverage run -m pytest"
}

# Report target
function Report {
    Test
    # Replace with your coverage report and HTML generation commands
    # Example:
    Invoke-Expression "coverage report"
    Invoke-Expression "coverage html"
    Invoke-Expression "$BROWSER htmlcov/index.html"
}

# Execute the specified target
$target = $args[0]

if (Get-Command $target -ErrorAction SilentlyContinue) {
    & $target
} else {
    Show-Help
    exit 1
}
