# Assignment

It contain node app with docker compose,python script to delete 30 days older AWS EC@ AMIs and ansibe playbook
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Docker
Ansible 2.8.2
python3
```
Install below package if ansible break while downloading source code on https
```
pip install urllib3 ndg-httpsclient pyasn1
```
### Installing

Configure the Dockerfile and docker-compose to build node app.
Ansible cases valid only for ubuntu-16.04 or centos6
Python- We can use local smtp server but in this script we have configure google's smtp to send email.
For gmail we need to enable lesssecureapps. FYI https://www.google.com/settings/security/lesssecureapps
We are asuming that we have access to AWS EC2 resources, if not then better approach is to use session based access like sts

## How To Use
We can deploy node app with below commands

```
docker-compose up
```

Use --build to rebuild app

```
docker-compose up --build
```

Ansible execution - We can pass inventory with -i option or can configure inventory file. We can limit the execution with -l
```
ansible-playbook -i 10.x.x.x, test.yml -vv
```

We need to pass sender's email address along with password and receiver's email.

```
python3 ami.py
```
Enter Sender's email address:vikaxxxxxxxx@gmail.com
Enter the password:
Enter receiver's email address:vikaxxxxxxxx@yahoo.com

## Running the load test/command

To simulate multiple requests to the application for load-testing.

```
ab -n 1000 -c 10 http://localhost/
```

Sample of commands to run on running container like the version of NodeJS,redis and nginx

```
docker exec -i node_container_id node -v
docker exec -i nginx_container_id nginx -v
docker exec -i redis_container_id redis-server --version
docker exec -i redis_container_id redis-cli GET visit-count
```



## Contributing

Please read [CONTRIBUTING.md](https://github.com/vikas-prabhakar/Assignment/blob/master/CONTRIBUTING.md) for details and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Vikas Sharma** - *work* - [github](https://github.com/vikas-prabhakar)


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
