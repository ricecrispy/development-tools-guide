# development-tools-guide
A collection of guides/tips/notes for installing different tools for development

## Installing Docker Engine on WSL

1. Follow this [guide](https://docs.microsoft.com/en-us/windows/wsl/install) to configure WSL in your windows machine

2. Go to the Microsoft store and download your favorite Linux OS for WSL. I personally use Ubuntu

3. Open your newly downloaded Linux OS to configure it to your liking. I just did a simple `sudo apt-get update`

3. Go to this [page](https://docs.docker.com/engine/install/) and follow the guide to install docker engine on your WSL. Mainly you want to run these commands:

```
$ sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

```

```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

```
$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```
$ sudo apt-get update 
```
Note: You do need to run `sudo apt-get update` again for the next step to work

```
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```

At this point Docker should be installed successfully. You do need to run a couple extra commands to start Docker Daemon:

```
$ sudo usermod -aG docker $USER
```

```
$ newgrp docker
```

```
$ sudo service docker start
```

At this point you can verify that docker is up and running by running the following command:

```
$ docker run hello-world
```

## Developing in a container in WSL with VSCode

[Python container](https://github.com/ricecrispy/development-tools-guide/tree/main/python-poetry-container)

In this sample code, the Dockerfile builds a container that ships with python and the poetry package manager, so you can start developing right away without wasting time configuring your local machine.

[Ubuntu container with AWS, AWS SAM, and Terraform CLI](https://github.com/ricecrispy/development-tools-guide/tree/main/aws-cli-container)

In this sample code, the Dockerfile builds a simple ubuntu continer that ships with AWS, AWS SAM, and Terraform.