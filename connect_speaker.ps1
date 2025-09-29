# connect_speaker.ps1
param (
    [string]$DeviceName = "KILBURN II",
    [string]$BluetoothCLIPath = "L:\bluetoothcl\BluetoothCL.exe"
)

function Connect-BluetoothDevice {
    param([string]$name)
    Write-Host "Checking device $name..."
    $output = & $BluetoothCLIPath /list
    if ($output -match $name) {
        if ($output -match "$name.*Connected") {
            Write-Host "$name is already connected."
        } else {
            Write-Host "$name disconnected, reconnecting..."
            & $BluetoothCLIPath /connect "$name"
            Start-Sleep -Seconds 5
        }
    } else {
        Write-Host "Device $name not found."
    }
}

Connect-BluetoothDevice -name $DeviceName
