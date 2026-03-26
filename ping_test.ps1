# Ping test script for host 172.27.22.139
$target = "172.27.22.139"

Write-Host "Pinging $target..." -ForegroundColor Green

# Use Test-Connection cmdlet for pinging
try {
    $pingResult = Test-Connection -ComputerName $target -Count 4 -Quiet -ErrorAction Stop
    
    if ($pingResult) {
        Write-Host "Ping successful to $target" -ForegroundColor Green
    } else {
        Write-Host "Ping failed to $target" -ForegroundColor Red
    }
} catch {
    Write-Host "Error occurred while pinging $target" -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "Script execution completed." -ForegroundColor Yellow