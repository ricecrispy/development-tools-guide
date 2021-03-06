# development-tools-guide
A collection of guides/tips/notes for installing different tools for development

## Installing Docker Engine on WSL

1. Follow this [guide](https://docs.microsoft.com/en-us/windows/wsl/install) to configure WSL on your windows machine

2. Open PowerShell in admin mode to install a linux distro of your choice. Mainly you want to run the following command:

```
wsl --list --online # this list the available linux distro to install
```
```
wsl --install -d <Distro> # replace <Distro> with the linux distro name of your choice
```
```
New-NetFirewallRule -DisplayName "WSL" -Direction Inbound  -InterfaceAlias "vEthernet (WSL)"  -Action Allow # add a firewall rule to allow wsl traffic 
```

3. Open your newly downloaded Linux OS to configure it to your liking. I just did a simple `sudo apt-get update`

3. Go to this [page](https://docs.docker.com/engine/install/) and follow the guide to install docker engine on your WSL. Mainly you want to run these commands:

```
sudo apt-get install \
  ca-certificates \
  curl \
  gnupg \
  lsb-release

```

```
sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```
sudo apt-get update 
```
Note: You do need to run `sudo apt-get update` again for the next step to work

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

At this point Docker should be installed successfully. You do need to run a couple extra commands to start Docker Daemon:

```
sudo groupadd docker

sudo usermod -aG docker $USER
```

```
newgrp docker
```

```
sudo service docker start
```

At this point you can verify that docker is up and running by running the following command:

```
docker run hello-world
```

## Developing in a container in WSL with VSCode

[Python container](https://github.com/ricecrispy/development-tools-guide/tree/main/python-poetry-container)

In this sample code, the Dockerfile builds a container that ships with python and the poetry package manager, so you can start developing right away without wasting time configuring your local machine.

[Ubuntu container with AWS, AWS SAM, and Terraform CLI](https://github.com/ricecrispy/development-tools-guide/tree/main/aws-cli-container)

In this sample code, the Dockerfile builds a simple ubuntu continer that ships with AWS, AWS SAM, and Terraform.
