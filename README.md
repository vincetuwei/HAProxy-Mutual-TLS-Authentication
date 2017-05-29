# HAProxy-Mutual-TLS-Authentication

This project is intended to demonstrate the use of [HAProxy](http://www.haproxy.org/) for mutual SSL authentication.

## Usage

* Clone the repo to your local machine.
* Create an alias 'foo.com' for 127.0.0.1 in /etc/hosts file.
* Install docker and docker compose
* Run `docker-compose up` to bring up haproxy and test server docker containers
* run `python test_client.py` to test mutual ssl with and without the client certificates
