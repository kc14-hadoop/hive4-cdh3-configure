# hive4-cdh6-configure
Create mvn settings for building hive4-cdh3

# What is this?

This is a guide how to build a vanilla hive which:

* Contains the the Kafka Storage Handler. See also:
  * [Hive-Kafka integration](https://blog.cloudera.com/introducing-hive-kafka-sql/)
  * [Integrating Hive and Kafka](https://docs.cloudera.com/HDPDocuments/HDF3/HDF-3.4.1.1/kafka-hive-integration/content/hive-kafka-integration.html)
* Runs on a vanilla CDH 6.3.x distribution
* Allows Predicate Push-Down

# Needed Projects

First clone these projects into the same workspace directory:

* Docker Image with CentOS 7 with AdoptOpenJDK 8: https://github.com/kc14/docker-centos-openjdk.git
* Docker Image with CDH 6.3.0: https://github.com/kc14/docker-hadoop.git
* Docker Image with Vanilla Apache Hive 4.0.0 ported to CDH 6.3.0: https://github.com/kc14/docker-hive.git
* Forked Vanilla Apache Hive: https://github.com/kc14-hadoop/hive4-cdh6.git
* Setup for maven: https://github.com/kc14-hadoop/hive4-cdh6-configure.git

# Build Hive and Deploy Binary Distribution

After you have checked out all these projects:

1. `cd hive4-cdh6-configure`
2. `./configure.sh` - Should create `mvn.sh`
3. `./mvn.sh` - Should build hive and copy the bin distribution into the `Downloads` dir in `docker-hive`

# Create Default Network

1. `cd ../docker-hadoop/bin`
2. `./docker-create-br1.sh` - Set up a docker network bridge `br1` as default network

# Bring it all up

Now you are ready to build and start the necessary docker images:

1. `cd docker-centos-openjdk && docker-compose up --build`
2. `cd docker-hadoop && docker-compose up --build`
3. `cd docker-hive && docker-compose up --build`

Now all docker images are built and the corresponding containers are up and running. You can stop the containers in the terminal with `<ctrl>-C`.

The next time you start up the system `docker-compose up` is enough. The `docker-hive` container uses volumes. To delete them just use `docker-compose rm -v`.

# Using hive

Open a browser and connect to the follwoing URLs:

1. http://localhost:9870 - Webgui of Namenode
2. http://localhost:8088 - Webgui of Yarn Resource Manger
3. http://localhost:8188 - Webgui of Yarn Application History
4. http://localhost:10002 - Webgui of HiveServer2

Hive clients should connect to the following JDBC-URL:

* jdbc:hive2://127.0.0.1:10000/;auth=noSasl

E.g.:

* `beeline --convertBinaryArrayToString=true --fastConnect=false -u 'jdbc:hive2://127.0.0.1:10000/;auth=noSasl'`

Have fun.