# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%define lib_dir /usr/lib/bigtop-db
%define data_dir /var/lib/bigtop-db
%define doc_dir /usr/share/doc/bigtop-db-%{bigtop_db_version}
%define lib_hive /usr/lib/hive

Name: bigtop-db
Version: %{bigtop_db_version}
Release: %{bigtop_db_release}
Summary: Metastore database for Bigtop components

Group:      Development/Libraries
License:    ASL 2.0
URL:        http://bigtop.apache.org/
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:  noarch
Source0:    LICENSE
Source1:    install_bigtop_db.sh

Requires:   postgresql-server, postgresql-jdbc

%description
Metastore databse for Bigtop components

%package -n hive
Summary: Hive Metastore
Group: Development/Libraries
Requires: bigtop-db = %{version}-%{release}

%description -n hive
Bigtop DB - Hive

%prep
%setup -q -T -c

%build

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE1} \
  --build-dir=$RPM_SOURCE_DIR \
  --prefix=$RPM_BUILD_ROOT \
  --doc-dir=$RPM_BUILD_ROOT/%{doc_dir}

%__install -d -m 0755 $RPM_BUILD_ROOT/etc/init.d/
%__ln_s /etc/init.d/postgresql $RPM_BUILD_ROOT/etc/init.d/bigtop-db

%pre

%post

%clean

%files
%defattr(-,root,root,-)
/etc/sysconfig/bigtop-db
/etc/init.d/bigtop-db
%{doc_dir}
/var/lib/bigtop-db
/var/log/bigtop-db



