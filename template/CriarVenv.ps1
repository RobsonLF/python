if (-not (Test-Path -Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}
write-Host "Activating virtual environment..."
& .\venv\Scripts\Activate.ps1