# Python script which prints basic information about your OS to console. And Docker container.
Simple Python script which prints server metrics to console. Implemented metrics for CPU usage, RAM usage, disk partition and usage, running processes information.
- Docker Hub link - https://hub.docker.com/r/terenchukv/metrics-container

# REQUIREMENTS
- Linux OS 
- Docker (for container usage)
- Python 3.6 and pip (for running script without docker)

# Script arguments
- cpu - prints CPU metrics
Sample output:
```
system.cpu.idle 36.9M
system.cpu.user 25.5K
system.cpu.guest 0.0B
system.cpu.iowait 6.5K
system.cpu.stolen 1.3K
system.cpu.system 14.4K
```
- mem - prints RAM metrics
Sample output:
```
virtual total 992.2M
virtual used 272.7M
virtual free 575.8M
virtual shared 15.9M
swap total 1.2G
swap used 62.4M
swap free 1.1G
```
- disk - prints disk partition and disk space usage
Sample output:
```
Device                                   Total     Used     Free  Use %      Type  Mount
/dev/mapper/cl_testnode-root              9.8G     7.1G     2.7G    72%       xfs  /
/dev/sda1                              1014.0M   241.2M   772.8M    23%       xfs  /boot
/dev/mapper/cl_testnode-root              9.8G     7.1G     2.7G    72%       xfs  /var/lib/docker/plugins
/dev/mapper/cl_testnode-root              9.8G     7.1G     2.7G    72%       xfs  /var/lib/docker/overlay
```
- proc - running processes information
Sample output:
```
username:root -- name:systemd -- pid:1
username:root -- name:kthreadd -- pid:2
username:root -- name:ksoftirqd/0 -- pid:3
username:root -- name:kworker/0:0H -- pid:5
username:root -- name:migration/0 -- pid:7
```

# Installation with Docker
- Install Docker to your system (https://docs.docker.com/install/)
- clone this repo
- build image in the prject folder:
```
docker build -t metrics-container .
```

# Usage with Docker
get CPU metrics:
```
docker run --rm -it metrics-container cpu
```
get RAM metrics:
```
docker run --rm -it metrics-container mem
```
get Disk metrics:
```
docker run --rm --privileged --pid=host -it -v /:/rootfs:ro metrics-container disk
```
Note! We need to mount the whole host files system as read only into the docker container with ```-v /:/rootfs:ro ``` for correct mount point description. Mount points after "/rootfs" are system devices.
get processes information
```
docker run --rm --privileged --pid=host -it -v /etc/passwd:/etc/passwd:ro metrics-container proc
```
Note! We need to mount /etc/passwd into docker container with ```-v /etc/passwd:/etc/passwd:ro``` for correct username mapping.

# Installation on bare system
- Instal python3.6+ and pip
- Install psutil:
```
pip install psutil
```

# Usage on bare system 
Run python script with one of arguments:
```
python metrics.py cpu
```
```
python metrics.py mem
```
```
python metrics.py disk
```
```
python metrics.py proc
```