$validStrategies = "dfs"
$validParams = "RDUL","RDLU"

foreach ($strategy in $validStrategies) {
    foreach ($param in $validParams) {
        $command = ".\dupa.ps1 -strategy $strategy -param $param"
        Write-Host "Running command: $command"
        Invoke-Expression $command
    }
}
