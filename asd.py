Last login: Thu Mar  6 12:04:10 on ttys000
wowlass@MacBook-Air-Ulia ~ % docker exec -it db psql -U django_user -d django
Error response from daemon: container 22fc4d582672422dbe3bca548da0c96dc98cf65e1ca55a1192cc2cc955a1eda0 is not running
wowlass@MacBook-Air-Ulia ~ % docker exec -it db psql -U django_user -d django
psql (13.10 (Debian 13.10-1.pgdg110+1))
Type "help" for help.

django=# \dt
           List of relations
 Schema |  Name  | Type  |    Owner    
--------+--------+-------+-------------
 public | movies | table | django_user
(1 row)

django=# %                                                                      wowlass@MacBook-Air-Ulia ~ % 
  [Восстановлен 7 марта 2025 г., 07:18:38]
Last login: Fri Mar  7 07:18:31 on console
Restored session: пятница,  7 марта 2025 г. 00:37:08 (-05)
wowlass@MacBook-Air-Ulia ~ % 
  [Восстановлен 8 марта 2025 г., 00:46:38]
Last login: Sat Mar  8 00:46:38 on ttys000
wowlass@MacBook-Air-Ulia ~ % 
  [Восстановлен 9 марта 2025 г., 11:46:03]
Last login: Sun Mar  9 11:46:03 on ttys000
/bin/date: option requires an argument -- r
usage: date [-jnRu] [-I[date|hours|minutes|seconds]] [-f input_fmt]
            [-r filename|seconds] [-v[+|-]val[y|m|w|d|H|M|S]]
            [[[[mm]dd]HH]MM[[cc]yy][.SS] | new_date] [+output_fmt]
Restored session: 
wowlass@MacBook-Air-Ulia ~ % docker compose exec backend python manage.py migrate
no configuration file provided: not found
wowlass@MacBook-Air-Ulia ~ % docker compose exec backend python manage.py migrate
no configuration file provided: not found
wowlass@MacBook-Air-Ulia ~ % cd Dev     
wowlass@MacBook-Air-Ulia Dev % cd taski-docker 
wowlass@MacBook-Air-Ulia taski-docker % docker compose exec backend python manage.py migrate
WARN[0000] /Users/wowlass/Dev/taski-docker/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
Operations to perform:
  Apply all migrations: admin, api, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying api.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
wowlass@MacBook-Air-Ulia taski-docker % docker compose exec backend python manage.py collectstatic
WARN[0000] /Users/wowlass/Dev/taski-docker/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 

161 static files copied to '/app/collected_static'.
wowlass@MacBook-Air-Ulia taski-docker % docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
WARN[0000] /Users/wowlass/Dev/taski-docker/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
wowlass@MacBook-Air-Ulia taski-docker % docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
WARN[0000] /Users/wowlass/Dev/taski-docker/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 

161 static files copied to '/app/collected_static'.
wowlass@MacBook-Air-Ulia taski-docker % docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
WARN[0000] /Users/wowlass/Dev/taski-docker/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
wowlass@MacBook-Air-Ulia taski-docker % docker compose -f docker-compose.production.yml exec backend python manage.py migrate
WARN[0000] /Users/wowlass/Dev/taski-docker/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
Operations to perform:
  Apply all migrations: admin, api, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying api.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
wowlass@MacBook-Air-Ulia taski-docker % ssh -i /Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63 yc-user@158.160.23.155
Enter passphrase for key '/Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63': 
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Mar  9 11:17:34 AM UTC 2025

  System load:  0.173828125        Processes:             144
  Usage of /:   39.3% of 19.59GB   Users logged in:       0
  Memory usage: 28%                IPv4 address for eth0: 192.168.1.157
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

123 updates can be applied immediately.
To see these additional updates run: apt list --upgradable


*** System restart required ***
Last login: Mon Feb 24 18:56:24 2025 from 94.231.136.198
yc-user@epdem2uvm78ltigqd1s2:~$ sudo systemctl stop gunicorn
yc-user@epdem2uvm78ltigqd1s2:~$ sudo rm /etc/systemd/system/gunicorn.service
yc-user@epdem2uvm78ltigqd1s2:~$ ls
infra_sprint1  taski
yc-user@epdem2uvm78ltigqd1s2:~$ rm -r ./taski/*
^C      
yc-user@epdem2uvm78ltigqd1s2:~$ cd taski/
yc-user@epdem2uvm78ltigqd1s2:~/taski$ ls
venv
yc-user@epdem2uvm78ltigqd1s2:~/taski$ rm -r ./taski/*
rm: cannot remove './taski/*': No such file or directory
yc-user@epdem2uvm78ltigqd1s2:~/taski$ cd ..
yc-user@epdem2uvm78ltigqd1s2:~$ rm -r ./taski/*
yc-user@epdem2uvm78ltigqd1s2:~$ cd taski/
yc-user@epdem2uvm78ltigqd1s2:~/taski$ ls
yc-user@epdem2uvm78ltigqd1s2:~/taski$ cd ..
yc-user@epdem2uvm78ltigqd1s2:~$ rm -r ./infra_sprint1/*
yc-user@epdem2uvm78ltigqd1s2:~$ ls
infra_sprint1  taski
yc-user@epdem2uvm78ltigqd1s2:~$ rm 
.bash_history              .npm/
.bash_logout               .profile
.bashrc                    .pytest_cache/
.cache/                    .ssh/
.gitconfig                 .sudo_as_admin_successful
infra_sprint1/             taski/
.local/                    
yc-user@epdem2uvm78ltigqd1s2:~$ rm 
.bash_history              .npm/
.bash_logout               .profile
.bashrc                    .pytest_cache/
.cache/                    .ssh/
.gitconfig                 .sudo_as_admin_successful
infra_sprint1/             taski/
.local/                    
yc-user@epdem2uvm78ltigqd1s2:~$ rm infra_sprint1/
rm: cannot remove 'infra_sprint1/': Is a directory
yc-user@epdem2uvm78ltigqd1s2:~$ npm cache clean --force
npm warn using --force Recommended protections disabled.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.2.0
npm notice To update run: npm install -g npm@11.2.0
npm notice
yc-user@epdem2uvm78ltigqd1s2:~$ sudo apt clean
yc-user@epdem2uvm78ltigqd1s2:~$  sudo journalctl --vacuum-time=1d
 
Vacuuming done, freed 0B of archived journals from /var/log/journal.
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-0000000000000001-00062e476a3e962a.journal (40.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-0000000000008295-00062e5577a55dc9.journal (72.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-00000000000187c0-00062e7d8c157b9f.journal (72.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/user-1000@e2193a0f9c8442e5b0d6b6eef3fb37ce-0000000000021b3e-00062e9628c40349.journal (8.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-0000000000028fb2-00062eabfb6230f9.journal (104.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/user-1000@e2193a0f9c8442e5b0d6b6eef3fb37ce-0000000000029dde-00062eacb24d9652.journal (8.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-00000000000411c4-00062ec40f804025.journal (104.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/user-1000@e2193a0f9c8442e5b0d6b6eef3fb37ce-0000000000047be1-00062eca32e75c39.journal (8.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-0000000000059531-00062edc0d73584f.journal (96.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/user-1000@e2193a0f9c8442e5b0d6b6eef3fb37ce-00000000000635d3-00062ee64ecfdadb.journal (8.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-000000000007129d-00062ef376c82864.journal (96.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-0000000000088fed-00062f0b24635247.journal (104.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-00000000000a284e-00062f271efb1bfd.journal (104.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-00000000000bc393-00062f440244582f.journal (104.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-00000000000d5bbf-00062f6021611ac5.journal (104.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-00000000000ef11a-00062f7b9d6e3c25.journal (104.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-0000000000109087-00062f9875521455.journal (104.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-0000000000122967-00062fb47d9fd0b8.journal (104.0M).
Vacuuming done, freed 1.3G of archived journals from /var/log/journal/2300000765aeb0bdfb1d15eca1a68782.
Vacuuming done, freed 0B of archived journals from /run/log/journal.
yc-user@epdem2uvm78ltigqd1s2:~$ sudo apt update
Hit:1 http://ru.archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://ru.archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]
Get:3 http://ru.archive.ubuntu.com/ubuntu jammy-backports InRelease [127 kB]
Get:4 http://ru.archive.ubuntu.com/ubuntu jammy-security InRelease [129 kB]
Hit:5 https://deb.nodesource.com/node_18.x nodistro InRelease
Get:6 http://ru.archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [2,377 kB]
Get:7 http://ru.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1,193 kB]
Fetched 3,954 kB in 1s (3,498 kB/s)                     
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
119 packages can be upgraded. Run 'apt list --upgradable' to see them.
yc-user@epdem2uvm78ltigqd1s2:~$ sudo apt install curl
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
curl is already the newest version (7.81.0-1ubuntu1.20).
0 upgraded, 0 newly installed, 0 to remove and 119 not upgraded.
yc-user@epdem2uvm78ltigqd1s2:~$ curl -fSL https://get/docker/com -o get-docker.sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0curl: (6) Could not resolve host: get
yc-user@epdem2uvm78ltigqd1s2:~$ curl -fSL https://get.docker.com -o get-docker.sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 22592  100 22592    0     0   153k      0 --:--:-- --:--:-- --:--:--  154k
yc-user@epdem2uvm78ltigqd1s2:~$ sudo sh ./get-docker.sh
# Executing docker install script, commit: 4c94a56999e10efcf48c5b8e3f6afea464f9108e
+ sh -c apt-get -qq update >/dev/null
+ sh -c DEBIAN_FRONTEND=noninteractive apt-get -y -qq install ca-certificates curl >/dev/null
+ sh -c install -m 0755 -d /etc/apt/keyrings
+ sh -c curl -fsSL "https://download.docker.com/linux/ubuntu/gpg" -o /etc/apt/keyrings/docker.asc
+ sh -c chmod a+r /etc/apt/keyrings/docker.asc
+ sh -c echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu jammy stable" > /etc/apt/sources.list.d/docker.list
+ sh -c apt-get -qq update >/dev/null
sudo apt install docker-compose-plugin 
+ sh -c DEBIAN_FRONTEND=noninteractive apt-get -y -qq install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-ce-rootless-extras docker-buildx-plugin >/dev/null
^CE: Sub-process /usr/sbin/dpkg-preconfigure --apt || true received signal 2.
E: Failure running script /usr/sbin/dpkg-preconfigure --apt || true

yc-user@epdem2uvm78ltigqd1s2:~$ sudo sh ./get-docker.sh
# Executing docker install script, commit: 4c94a56999e10efcf48c5b8e3f6afea464f9108e
+ sh -c apt-get -qq update >/dev/null
+ sh -c DEBIAN_FRONTEND=noninteractive apt-get -y -qq install ca-certificates curl >/dev/null
+ sh -c install -m 0755 -d /etc/apt/keyrings
+ sh -c curl -fsSL "https://download.docker.com/linux/ubuntu/gpg" -o /etc/apt/keyrings/docker.asc
+ sh -c chmod a+r /etc/apt/keyrings/docker.asc
+ sh -c echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu jammy stable" > /etc/apt/sources.list.d/docker.list
+ sh -c apt-get -qq update >/dev/null
+ sh -c DEBIAN_FRONTEND=noninteractive apt-get -y -qq install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-ce-rootless-extras docker-buildx-plugin >/dev/null
+ sh -c docker version
Client: Docker Engine - Community
 Version:           28.0.1
 API version:       1.48
 Go version:        go1.23.6
 Git commit:        068a01e
 Built:             Wed Feb 26 10:41:08 2025
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          28.0.1
  API version:      1.48 (minimum version 1.24)
  Go version:       go1.23.6
  Git commit:       bbd0a17
  Built:            Wed Feb 26 10:41:08 2025
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.7.25
  GitCommit:        bcc810d6b9066471b0b6fa75f557a15a1cbf31bb
 runc:
  Version:          1.2.4
  GitCommit:        v1.2.4-0-g6c52b3f
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0

================================================================================

To run Docker as a non-privileged user, consider setting up the
Docker daemon in rootless mode for your user:

    dockerd-rootless-setuptool.sh install

Visit https://docs.docker.com/go/rootless/ to learn about rootless mode.


To run the Docker daemon as a fully privileged service, but granting non-root
users access, refer to https://docs.docker.com/go/daemon-access/

WARNING: Access to the remote API on a privileged Docker daemon is equivalent
         to root access on the host. Refer to the 'Docker daemon attack surface'
         documentation for details: https://docs.docker.com/go/attack-surface/

================================================================================

yc-user@epdem2uvm78ltigqd1s2:~$ sudo apt install docker-compose-plugin 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
docker-compose-plugin is already the newest version (2.33.1-1~ubuntu.22.04~jammy).
0 upgraded, 0 newly installed, 0 to remove and 119 not upgraded.
yc-user@epdem2uvm78ltigqd1s2:~$ touch docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~$ nano docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~$ nano docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~$ cd 
.cache/        infra_sprint1/ .local/        .npm/          .pytest_cache/ .ssh/          taski/         
yc-user@epdem2uvm78ltigqd1s2:~$ cd taski/
yc-user@epdem2uvm78ltigqd1s2:~/taski$ touch .env
yc-user@epdem2uvm78ltigqd1s2:~/taski$ nano .env
yc-user@epdem2uvm78ltigqd1s2:~/taski$ cd ..
yc-user@epdem2uvm78ltigqd1s2:~$ docker ps -a
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.48/containers/json?all=1": dial unix /var/run/docker.sock: connect: permission denied
yc-user@epdem2uvm78ltigqd1s2:~$ cd taski/
yc-user@epdem2uvm78ltigqd1s2:~/taski$ docker ps -a
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.48/containers/json?all=1": dial unix /var/run/docker.sock: connect: permission denied
yc-user@epdem2uvm78ltigqd1s2:~/taski$ sudo docker compose -f docker-compose.production.yml up -d
open /home/yc-user/taski/docker-compose.production.yml: no such file or directory
yc-user@epdem2uvm78ltigqd1s2:~/taski$ св юю
св: command not found
yc-user@epdem2uvm78ltigqd1s2:~/taski$ cd ..
yc-user@epdem2uvm78ltigqd1s2:~$ ls
docker-compose.production.yml  get-docker.sh  infra_sprint1  taski
yc-user@epdem2uvm78ltigqd1s2:~$ rm docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~$ cd taski/
yc-user@epdem2uvm78ltigqd1s2:~/taski$ touch docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~/taski$ nano docker-compose.production.yml 
yc-user@epdem2uvm78ltigqd1s2:~/taski$ sudo docker compose -f docker-compose.production.yml up -d
WARN[0000] /home/yc-user/taski/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 46/46
 ✔ gateway Pulled                                                                                                         75.0s 
 ✔ frontend Pulled                                                                                                       212.4s 
 ✔ db Pulled                                                                                                             111.0s 
 ✔ backend Pulled                                                                                                        171.6s 
[+] Running 7/7
 ✔ Network taski_default              Created                                                                              0.6s 
 ✔ Volume "taski_static_volume"       Created                                                                              0.0s 
 ✔ Volume "taski_pg_data_production"  Created                                                                              0.0s 
 ✔ Container taski-frontend-1         Started                                                                              9.7s 
 ✔ Container taski-gateway-1          Started                                                                              9.9s 
 ✔ Container taski-db-1               Started                                                                              9.7s 
 ✔ Container taski-backend-1          Started                                                                              9.7s 
yc-user@epdem2uvm78ltigqd1s2:~/taski$ sudo docker compose -f docker-compose.production.yml ps
WARN[0000] /home/yc-user/taski/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
NAME              IMAGE                   COMMAND                  SERVICE   CREATED          STATUS         PORTS
taski-backend-1   wowlass/taski_backend   "gunicorn --bind 0.0…"   backend   13 seconds ago   Up 7 seconds   
taski-db-1        postgres:13.10          "docker-entrypoint.s…"   db        13 seconds ago   Up 7 seconds   5432/tcp
taski-gateway-1   wowlass/taski_gateway   "/docker-entrypoint.…"   gateway   12 seconds ago   Up 7 seconds   0.0.0.0:8000->80/tcp, [::]:8000->80/tcp
yc-user@epdem2uvm78ltigqd1s2:~/taski$ sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
WARN[0000] /home/yc-user/taski/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
Operations to perform:
  Apply all migrations: admin, api, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying api.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
yc-user@epdem2uvm78ltigqd1s2:~/taski$ sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
WARN[0000] /home/yc-user/taski/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 

161 static files copied to '/app/collected_static'.
yc-user@epdem2uvm78ltigqd1s2:~/taski$ sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/ 
WARN[0000] /home/yc-user/taski/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
yc-user@epdem2uvm78ltigqd1s2:~/taski$ ls
docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~/taski$ cd ..
yc-user@epdem2uvm78ltigqd1s2:~$ sudo nano /etc/nginx/sites-enabled/default
yc-user@epdem2uvm78ltigqd1s2:~$ sudo nginx -t
nginx: [warn] conflicting server name "158.160.23.155" on 0.0.0.0:443, ignored
nginx: [warn] conflicting server name "158.160.23.155" on 0.0.0.0:80, ignored
nginx: [warn] conflicting server name "158.160.23.155" on 0.0.0.0:80, ignored
nginx: [warn] conflicting server name "kitttygram.zapto.org" on 0.0.0.0:80, ignored
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
yc-user@epdem2uvm78ltigqd1s2:~$ sudo service nginx reload
yc-user@epdem2uvm78ltigqd1s2:~$ Read from remote host 158.160.23.155: Connection reset by peer
Connection to 158.160.23.155 closed.
client_loop: send disconnect: Broken pipe
wowlass@MacBook-Air-Ulia taski-docker % 
  [Восстановлен 10 марта 2025 г., 06:34:23]
Last login: Mon Mar 10 06:34:11 on console
/bin/date: option requires an argument -- r
usage: date [-jnRu] [-I[date|hours|minutes|seconds]] [-f input_fmt]
            [-r filename|seconds] [-v[+|-]val[y|m|w|d|H|M|S]]
            [[[[mm]dd]HH]MM[[cc]yy][.SS] | new_date] [+output_fmt]
Restored session: 
wowlass@MacBook-Air-Ulia taski-docker % 
  [Восстановлен 10 марта 2025 г., 21:40:09]
Last login: Mon Mar 10 21:40:00 on console
/bin/date: option requires an argument -- r
usage: date [-jnRu] [-I[date|hours|minutes|seconds]] [-f input_fmt]
            [-r filename|seconds] [-v[+|-]val[y|m|w|d|H|M|S]]
            [[[[mm]dd]HH]MM[[cc]yy][.SS] | new_date] [+output_fmt]
Restored session: 
wowlass@MacBook-Air-Ulia taski-docker % 
  [Восстановлен 12 марта 2025 г., 07:43:42]
Last login: Wed Mar 12 07:43:30 on console
wowlass@MacBook-Air-Ulia taski-docker % 
  [Восстановлен 13 марта 2025 г., 21:29:27]
Last login: Thu Mar 13 21:29:16 on console
Restored session: четверг, 13 марта 2025 г. 00:57:54 (-05)
wowlass@MacBook-Air-Ulia taski-docker % 
  [Восстановлен 14 марта 2025 г., 07:36:19]
Last login: Fri Mar 14 07:36:13 on console
Restored session: пятница, 14 марта 2025 г. 01:05:44 (-05)
wowlass@MacBook-Air-Ulia taski-docker % 
  [Восстановлен 14 марта 2025 г., 22:25:41]
Last login: Fri Mar 14 22:25:31 on console
Restored session: пятница, 14 марта 2025 г. 07:53:19 (-05)
wowlass@MacBook-Air-Ulia taski-docker % ssh -i /Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63 yc-user@158.160.23.155
Enter passphrase for key '/Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63': 
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Mar 14 08:22:58 PM UTC 2025

  System load:                      0.0
  Usage of /:                       49.3% of 19.59GB
  Memory usage:                     32%
  Swap usage:                       0%
  Processes:                        156
  Users logged in:                  0
  IPv4 address for br-446457717e54: 172.18.0.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for eth0:            192.168.1.157

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

124 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

New release '24.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Fri Mar 14 19:59:43 2025 from 91.84.113.7
yc-user@epdem2uvm78ltigqd1s2:~$ ls
get-docker.sh  infra_sprint1  taski
yc-user@epdem2uvm78ltigqd1s2:~$ cd taski/
yc-user@epdem2uvm78ltigqd1s2:~/taski$ ls
docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~/taski$ Read from remote host 158.160.23.155: Connection reset by peer
Connection to 158.160.23.155 closed.
client_loop: send disconnect: Broken pipe
wowlass@MacBook-Air-Ulia taski-docker % ssh -i /Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63 yc-user@158.160.23.155
Enter passphrase for key '/Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63': 
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Mar 14 08:26:12 PM UTC 2025

  System load:                      0.0
  Usage of /:                       49.3% of 19.59GB
  Memory usage:                     33%
  Swap usage:                       0%
  Processes:                        156
  Users logged in:                  0
  IPv4 address for br-446457717e54: 172.18.0.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for eth0:            192.168.1.157

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

124 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

New release '24.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Fri Mar 14 20:22:59 2025 from 89.169.52.151
yc-user@epdem2uvm78ltigqd1s2:~$ sudo systemctl stop gunicorn
Failed to stop gunicorn.service: Unit gunicorn.service not loaded.
yc-user@epdem2uvm78ltigqd1s2:~$ sudo rm /etc/systemd/system/gunicorn.service
rm: cannot remove '/etc/systemd/system/gunicorn.service': No such file or directory
yc-user@epdem2uvm78ltigqd1s2:~$ ls
get-docker.sh  infra_sprint1  taski
yc-user@epdem2uvm78ltigqd1s2:~$ rm -r ./infra_sprint
rm: cannot remove './infra_sprint': No such file or directory
yc-user@epdem2uvm78ltigqd1s2:~$ rm -r ./infra_sprint/
rm: cannot remove './infra_sprint/': No such file or directory
yc-user@epdem2uvm78ltigqd1s2:~$ rm -r infra_sprint1/
rm: remove write-protected regular file 'infra_sprint1/.git/objects/30/bd623c235a8810777bf14d0bbeb674f4fe6295'? y
rm: remove write-protected regular file 'infra_sprint1/.git/objects/90/b043ee176f04488599b95874cb177dcf5f13c2'? yes
rm: remove write-protected regular file 'infra_sprint1/.git/objects/94/d70877c856a32a54ca334dbe16337dff9efff2'? 
rm: cannot remove 'infra_sprint1/.git/objects/94': Directory not empty
rm: remove write-protected regular file 'infra_sprint1/.git/objects/9a/bbf2fc2fa10f4dfc108b3dbe4d1bf624838a9d'? ^C
yc-user@epdem2uvm78ltigqd1s2:~$ ls
get-docker.sh  infra_sprint1  taski
yc-user@epdem2uvm78ltigqd1s2:~$ rm -r ./infra_sprint1/
rm: remove write-protected regular file './infra_sprint1/.git/objects/94/d70877c856a32a54ca334dbe16337dff9efff2'? rm
rm: cannot remove './infra_sprint1/.git/objects/94': Directory not empty
rm: remove write-protected regular file './infra_sprint1/.git/objects/9a/bbf2fc2fa10f4dfc108b3dbe4d1bf624838a9d'? ^[[A^[[A^C
yc-user@epdem2uvm78ltigqd1s2:~$ rm -r ./infra_sprint1/*
rm: cannot remove './infra_sprint1/*': No such file or directory
yc-user@epdem2uvm78ltigqd1s2:~$ ls
get-docker.sh  infra_sprint1  taski
yc-user@epdem2uvm78ltigqd1s2:~$ cd infra_sprint1/
yc-user@epdem2uvm78ltigqd1s2:~/infra_sprint1$ ls
yc-user@epdem2uvm78ltigqd1s2:~/infra_sprint1$ rm -rf ./infra_sprint1
yc-user@epdem2uvm78ltigqd1s2:~/infra_sprint1$ ls
yc-user@epdem2uvm78ltigqd1s2:~/infra_sprint1$ cd ..
yc-user@epdem2uvm78ltigqd1s2:~$ rm -rf ./infra_sprint1
yc-user@epdem2uvm78ltigqd1s2:~$ ls
get-docker.sh  taski
yc-user@epdem2uvm78ltigqd1s2:~$ npm cache clean --force
npm warn using --force Recommended protections disabled.
yc-user@epdem2uvm78ltigqd1s2:~$ sudo apt clean
yc-user@epdem2uvm78ltigqd1s2:~$  sudo journalctl --vacuum-time=1d
 
Vacuuming done, freed 0B of archived journals from /run/log/journal.
Vacuuming done, freed 0B of archived journals from /var/log/journal.
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-000000000013c55d-00062fd1031af882.journal (96.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/user-1000@e2193a0f9c8442e5b0d6b6eef3fb37ce-0000000000150f4b-00062fe7009441ec.journal (8.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-0000000000153979-00062fe8c1a39b96.journal (96.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/user-1000@e2193a0f9c8442e5b0d6b6eef3fb37ce-0000000000154572-00062fe956b8c7f7.journal (8.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-0000000000169662-00062ff9e43383f9.journal (104.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-00000000001829a1-00063013cdce7fa8.journal (104.0M).
Deleted archived journal /var/log/journal/2300000765aeb0bdfb1d15eca1a68782/system@01b01bbd143d40399a491b4199e173ce-000000000019b434-0006302dd81efa71.journal (96.0M).
Vacuuming done, freed 512.0M of archived journals from /var/log/journal/2300000765aeb0bdfb1d15eca1a68782.
yc-user@epdem2uvm78ltigqd1s2:~$ ls
get-docker.sh  taski
yc-user@epdem2uvm78ltigqd1s2:~$ Read from remote host 158.160.23.155: Connection reset by peer
Connection to 158.160.23.155 closed.
client_loop: send disconnect: Broken pipe
wowlass@MacBook-Air-Ulia taski-docker % ssh -i /Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63 yc-user@158.160.23.155
Enter passphrase for key '/Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63': 
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Mar 14 08:33:27 PM UTC 2025

  System load:                      0.0107421875
  Usage of /:                       45.6% of 19.59GB
  Memory usage:                     33%
  Swap usage:                       0%
  Processes:                        156
  Users logged in:                  0
  IPv4 address for br-446457717e54: 172.18.0.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for eth0:            192.168.1.157

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

124 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

New release '24.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Fri Mar 14 20:26:13 2025 from 89.169.52.151
yc-user@epdem2uvm78ltigqd1s2:~$ mkdir ./Kittygram
yc-user@epdem2uvm78ltigqd1s2:~$ ls
get-docker.sh  Kittygram  taski
yc-user@epdem2uvm78ltigqd1s2:~$ cd Kittygram/
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ touch docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ ls
docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ ls
docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano Вывод Терминала
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml up -d
WARN[0001] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
env file /home/yc-user/Kittygram/.env not found: stat /home/yc-user/Kittygram/.env: no such file or directory
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml ps
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
env file /home/yc-user/Kittygram/.env not found: stat /home/yc-user/Kittygram/.env: no such file or directory
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ Read from remote host 158.160.23.155: Connection reset by peer
Connection to 158.160.23.155 closed.
client_loop: send disconnect: Broken pipe
wowlass@MacBook-Air-Ulia taski-docker % ssh -i /Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63 yc-user@158.160.23.155
Enter passphrase for key '/Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63': 
Enter passphrase for key '/Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63': 
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Mar 14 08:37:46 PM UTC 2025

  System load:                      0.09912109375
  Usage of /:                       45.6% of 19.59GB
  Memory usage:                     32%
  Swap usage:                       0%
  Processes:                        155
  Users logged in:                  0
  IPv4 address for br-446457717e54: 172.18.0.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for eth0:            192.168.1.157

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

124 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

New release '24.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Fri Mar 14 20:33:28 2025 from 89.169.52.151
yc-user@epdem2uvm78ltigqd1s2:~$ sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
open /home/yc-user/docker-compose.production.yml: no such file or directory
yc-user@epdem2uvm78ltigqd1s2:~$ cd Kittygram/
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
env file /home/yc-user/Kittygram/.env not found: stat /home/yc-user/Kittygram/.env: no such file or directory
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ Read from remote host 158.160.23.155: Connection reset by peer
Connection to 158.160.23.155 closed.
client_loop: send disconnect: Broken pipe
wowlass@MacBook-Air-Ulia taski-docker % ssh -i /Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63 yc-user@158.160.23.155
Enter passphrase for key '/Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63': 
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Mar 14 08:39:26 PM UTC 2025

  System load:                      0.0166015625
  Usage of /:                       45.6% of 19.59GB
  Memory usage:                     32%
  Swap usage:                       0%
  Processes:                        157
  Users logged in:                  0
  IPv4 address for br-446457717e54: 172.18.0.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for eth0:            192.168.1.157

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

124 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

New release '24.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Fri Mar 14 20:37:47 2025 from 89.169.52.151
yc-user@epdem2uvm78ltigqd1s2:~$ cd Kittygram/
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ touch .env
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ ls
docker-compose.production.yml
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano .env
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano ,env
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano .env
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano .env
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml ps
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml up -d
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
[+] Running 0/4
 ⠋ frontend Pulling                                                                                                        2.1s 
 ⠋ db Pulling                                                                                                              2.1s 
 ⠋ backend Pulling                                                                                                         2.1s 
 ⠋ gateway Pulling                                                                                                         2.1s 
no matching manifest for linux/amd64 in the manifest list entries
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml ps
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
service "backend" is not running
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrateRead from remote host 158.160.23.155: Connection reset by peer
Connection to 158.160.23.155 closed.
client_loop: send disconnect: Broken pipe
wowlass@MacBook-Air-Ulia taski-docker % 
  [Восстановлен 15 марта 2025 г., 08:14:55]
Last login: Sat Mar 15 08:14:46 on console
Restored session: суббота, 15 марта 2025 г. 02:56:32 (-05)
wowlass@MacBook-Air-Ulia taski-docker % ssh -i /Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63 yc-user@158.160.23.155
Enter passphrase for key '/Users/wowlass/.ssh/yandexpraktikum/yc-wowlass63': 
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sat Mar 15 04:54:21 AM UTC 2025

  System load:                      0.080078125
  Usage of /:                       46.3% of 19.59GB
  Memory usage:                     32%
  Swap usage:                       0%
  Processes:                        155
  Users logged in:                  0
  IPv4 address for br-446457717e54: 172.18.0.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for eth0:            192.168.1.157

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

124 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

New release '24.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Fri Mar 14 20:39:26 2025 from 89.169.52.151
yc-user@epdem2uvm78ltigqd1s2:~$ ды
lды: command not found
yc-user@epdem2uvm78ltigqd1s2:~$ ls
get-docker.sh  Kittygram  taski
yc-user@epdem2uvm78ltigqd1s2:~$ docker ps -a
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.48/containers/json?all=1": dial unix /var/run/docker.sock: connect: permission denied
yc-user@epdem2uvm78ltigqd1s2:~$ cd Kittygram/
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ docker ps -a
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.48/containers/json?all=1": dial unix /var/run/docker.sock: connect: permission denied
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml up -d
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
[+] Running 2/4
 ⠦ backend Pulling                                                                                                         1.7s 
 ✘ frontend Error  no matching manifest for linux/amd64 in the manifest list entries                                       1.7s 
 ✘ gateway Error   no matching manifest for linux/amd64 in the manifest list entries                                       1.7s 
 ⠦ db Pulling                                                                                                              1.7s 
no matching manifest for linux/amd64 in the manifest list entries
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ uname -m
x86_64
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ docker pull myfrontend:latest
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.48/images/create?fromImage=myfrontend&tag=latest": dial unix /var/run/docker.sock: connect: permission denied
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo uname -m
x86_64
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker pull myfrontend:latest
Error response from daemon: pull access denied for myfrontend, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ docker image
Usage:  docker image COMMAND

Manage images

Commands:
  build       Build an image from a Dockerfile
  history     Show the history of an image
  import      Import the contents from a tarball to create a filesystem image
  inspect     Display detailed information on one or more images
  load        Load an image from a tar archive or STDIN
  ls          List images
  prune       Remove unused images
  pull        Download an image from a registry
  push        Upload an image to a registry
  rm          Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE

Run 'docker image COMMAND --help' for more information on a command.
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano 
docker-compose.production.yml  .env                           
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano 
docker-compose.production.yml  .env                           
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano docker-compose.production.yml 
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano docker-compose.production.yml 
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano docker-compose.production.yml 
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml up -d
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
[+] Running 1/4
 ⠧ db Pulling                                                                                                              1.7s 
 ⠧ backend Pulling                                                                                                         1.7s 
 ✘ frontend Error  no matching manifest for linux/amd64 in the manifest list entries                                       1.7s 
 ⠧ gateway Pulling                                                                                                         1.7s 
no matching manifest for linux/amd64 in the manifest list entries
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml up -d
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
[+] Running 2/4
 ✘ gateway Error    no matching manifest for linux/amd64 in the manifest list entries                                      1.7s 
 ⠦ frontend Pulling                                                                                                        1.7s 
 ⠦ db Pulling                                                                                                              1.7s 
 ✘ backend Error    no matching manifest for linux/amd64 in the manifest list entries                                      1.7s 
no matching manifest for linux/amd64 in the manifest list entries
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml up -d
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
[+] Running 2/4
 ⠦ db Pulling                                                                                                              1.6s 
 ⠦ backend Pulling                                                                                                         1.6s 
 ✘ frontend Error  no matching manifest for linux/amd64 in the manifest list entries                                       1.6s 
 ✘ gateway Error   no matching manifest for linux/amd64 in the manifest list entries                                       1.6s 
no matching manifest for linux/amd64 in the manifest list entries
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml up -d
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
[+] Running 2/4
 ✘ gateway Error   no matching manifest for linux/amd64 in the manifest list entries                                       1.7s 
 ⠦ db Pulling                                                                                                              1.7s 
 ⠧ backend Pulling                                                                                                         1.7s 
 ✘ frontend Error  no matching manifest for linux/amd64 in the manifest list entries                                       1.7s 
no matching manifest for linux/amd64 in the manifest list entries
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ env | grep vmxm4
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano .env
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml up -d
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 2/4
 ⠦ db Pulling                                                                                                              1.6s 
 ⠦ backend Pulling                                                                                                         1.6s 
 ✘ frontend Error  no matching manifest for linux/amd64 in the manifest list entries                                       1.6s 
 ✘ gateway Error   no matching manifest for linux/amd64 in the manifest list entries                                       1.6s 
no matching manifest for linux/amd64 in the manifest list entries
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ docker system prune -a
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all images without at least one container associated to them
  - all build cache

Are you sure you want to continue? [y/N] y
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Head "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker system prune -a
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all images without at least one container associated to them
  - all build cache

Are you sure you want to continue? [y/N] y
Deleted Containers:
77c96c2923f290df3c36df5a0ece006d7adeaa418c1c2861665b5b87b62f16aa


н
^Cyc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ suddocker compose -f docker-compose.production.yml pullll
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0001] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Pulling 2/4
 ✘ gateway Error    no matching manifest for linux/amd64 in the manifest list entries                                      1.7s 
 ⠧ db Pulling                                                                                                              1.7s 
 ✘ backend Error    no matching manifest for linux/amd64 in the manifest list entries                                      1.7s 
 ⠧ frontend Pulling                                                                                                        1.7s 
no matching manifest for linux/amd64 in the manifest list entries
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ docker manifest inspect wowlass/kyttigram_frontend
errors:
denied: requested access to the resource is denied
unauthorized: authentication required

yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano docker-compose.production.yml 
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml pull
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Pulling 2/4
 ⠦ db Pulling                                                                                                              1.7s 
 ⠦ backend Pulling                                                                                                         1.7s 
 ✘ frontend Error  no matching manifest for linux/amd64 in the manifest list entries                                       1.7s 
 ✘ gateway Error   no matching manifest for linux/amd64 in the manifest list entries                                       1.7s 
no matching manifest for linux/amd64 in the manifest list entries
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ nano docker-compose.production.yml 
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml pull
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Pulling 49/49
 ✔ backend Pulled                                                                                                         43.0s 
 ✔ gateway Pulled                                                                                                         17.5s 
 ✔ db Pulled                                                                                                              86.5s 
 ✔ frontend Pulled                                                                                                       105.1s 
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml ps
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker images
REPOSITORY                   TAG       IMAGE ID       CREATED          SIZE
wowlass/kittygram_gateway    latest    bc60ee8a7b49   18 minutes ago   142MB
wowlass/kittygram_frontend   latest    050b2c624364   18 minutes ago   1.4GB
wowlass/kittygram_backend    latest    8af97f7b9595   19 minutes ago   1.1GB
wowlass/taski_gateway        <none>    26018bbdc1b1   5 days ago       142MB
wowlass/taski_backend        <none>    f65b0e61a594   5 days ago       1.04GB
wowlass/taski_backend        latest    16d9733bbc1e   5 days ago       1.04GB
wowlass/taski_gateway        latest    d1ced18ae0f0   5 days ago       142MB
wowlass/taski_gateway        <none>    2df9e2174731   5 days ago       142MB
postgres                     13        6c774c1ad2b9   2 weeks ago      423MB
postgres                     13.10     c562f2f06bc5   22 months ago    374MB
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml up -d
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 8/8
 ✔ Network kittygram_default       Created                                                                                 0.3s 
 ✔ Volume "kittygram_media"        Created                                                                                 0.1s 
 ✔ Volume "kittygram_pg_data"      Created                                                                                 0.0s 
 ✔ Volume "kittygram_static"       Created                                                                                 0.0s 
 ✔ Container kittygram-db-1        Started                                                                                 3.5s 
 ✔ Container kittygram-frontend-1  Started                                                                                 3.5s 
 ✔ Container kittygram-gateway-1   Started                                                                                 3.5s 
 ✔ Container kittygram-backend-1   Started                                                                                 3.4s 
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml ps
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
NAME                  IMAGE                              COMMAND                  SERVICE   CREATED          STATUS          PORTS
kittygram-backend-1   wowlass/kittygram_backend:latest   "gunicorn --bind 0.0…"   backend   13 seconds ago   Up 10 seconds   
kittygram-db-1        postgres:13                        "docker-entrypoint.s…"   db        13 seconds ago   Up 12 seconds   5432/tcp
kittygram-gateway-1   wowlass/kittygram_gateway:latest   "/docker-entrypoint.…"   gateway   13 seconds ago   Up 12 seconds   0.0.0.0:9000->80/tcp, [::]:9000->80/tcp
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
Operations to perform:
  Apply all migrations: admin, auth, authtoken, cats, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying authtoken.0003_tokenproxy... OK
  Applying cats.0001_initial... OK
  Applying sessions.0001_initial... OK
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 

161 static files copied to '/app/collected_static'.
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /static/static/ 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] The "vmxm4" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/yc-user/Kittygram/docker-compose.production.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
yc-user@epdem2uvm78ltigqd1s2:~/Kittygram$ cd ..
yc-user@epdem2uvm78ltigqd1s2:~$ sudo nano /etc/nginx/sites-enabled/default

  GNU nano 6.2                                    /etc/nginx/sites-enabled/default                                              
    location /admin/ {
        proxy_pass http://127.0.0.1:8080;
    }

    location /static/ {
        root /var/www/infra_sprint1;
    }

    location /media/ {
        alias /var/www/infra_sprint1/media/;
    }

    location / {
        root   /var/www/infra_sprint1;
        index  index.html index.htm;
        try_files $uri /index.html;
    }

^G Help         ^O Write Out    ^W Where Is     ^K Cut          ^T Execute      ^C Location     M-U Undo        M-A Set Mark
^X Exit         ^R Read File    ^\ Replace      ^U Paste        ^J Justify      ^/ Go To Line   M-E Redo        M-6 Copy
