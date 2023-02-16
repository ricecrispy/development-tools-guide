# reference: https://learn.microsoft.com/en-us/windows/wsl/install

# Run as Admin
wsl --install

# If you like to use another OS, run wsl -l -o to find another distribution
# wsl -l -o
wsl --install -d Ubuntu

# Depending on your firewall rule you may need to run the following command 
# and add a firewall rule to allow wsl traffic 
# New-NetFirewallRule -DisplayName "WSL" -Direction Inbound  -InterfaceAlias "vEthernet (WSL)"  -Action Allow
