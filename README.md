# docker-api

Prerequisites: 

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Docker](https://docs.docker.com/engine/install/)


##Step1:
Clone the project and go to docker-api directory else use Github Action genrated docker image https://hub.docker.com/r/shahrukhs/dockerapi

```shell
git clone https://github.com/shahrukh-s/docker-api.git
cd docker-api
```

##Step2:
Build docker image using below command: 

```shell
docker build -t dockerapi .
```

##Step3:
Run docker image using below command
```shell
docker run -it --rm -p 8000:8000 -v /var/run/docker.sock:/var/run/docker.sock dockerapi
```

##Step4:
For Accessing default page use below URL in CLI OR Chrome:

```shell
Curl localhost:8000
```

Create/Delete Container instruction given in the Default page.
##Default Page Output
![Preview](https://raw.githubusercontent.com/shahrukh-s/docker-api/master/default.png)


##Create Container Output
![Preview](https://raw.githubusercontent.com/shahrukh-s/docker-api/master/create_container.png.png)


##Delete Container Output
![Preview](https://raw.githubusercontent.com/shahrukh-s/docker-api/master/delete_conatiner.png)

