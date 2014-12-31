    Licensed to the Apache Software Foundation (ASF) under one or more
    contributor license agreements. See the NOTICE file distributed with
    this work for additional information regarding copyright ownership.
    The ASF licenses this file to You under the Apache License, Version 2.0
    (the "License"); you may not use this file except in compliance with
    the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

# Ansible Roles and Playbooks for Bigtop

## Overview

## Setup requirements
1) Install Ansible (version 1.4 or higher)

Redhat/CentOS:
```
# yum install -y ansible

```

Ubuntu:
```
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y ansible

```

2) Passwordless SSH to hosts (optional)
 

## Usage
1) Create a new inventory file (optional)
```
# cp inventory.cluster.example hosts

```

2) Run the playbook
```
# ansible-playbook -i hosts site.yml

```

## Add a new role
1) Create directories for new role
```
mkdir -p roles/ROLE_NAME
mkdir -p roles/ROLE_NAME/{files,templates,tasks,handlers,vars,defaults,meta}
```
 - If roles/x/tasks/main.yml exists, tasks listed therein will be added to the play
 - If roles/x/handlers/main.yml exists, handlers listed therein will be added to the play
 - If roles/x/vars/main.yml exists, variables listed therein will be added to the play
 - If roles/x/meta/main.yml exists, any role dependencies listed therein will be added to the list of roles (1.3 and later)
 - Any copy tasks can reference files in roles/x/files/ without having to path them relatively or absolutely
 - Any script tasks can reference scripts in roles/x/files/ without having to path them relatively or absolutely
 - Any template tasks can reference files in roles/x/templates/ without having to path them relatively or absolutely
 - Any include tasks can reference files in roles/x/tasks/ without having to path them relatively or absolutely
