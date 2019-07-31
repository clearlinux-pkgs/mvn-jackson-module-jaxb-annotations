#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jackson-module-jaxb-annotations
Version  : 2.6.7
Release  : 2
URL      : https://github.com/FasterXML/jackson-module-jaxb-annotations/archive/jackson-module-jaxb-annotations-2.6.7.tar.gz
Source0  : https://github.com/FasterXML/jackson-module-jaxb-annotations/archive/jackson-module-jaxb-annotations-2.6.7.tar.gz
Source1  : https://repo1.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.6.7/jackson-module-jaxb-annotations-2.6.7.jar
Source2  : https://repo1.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.6.7/jackson-module-jaxb-annotations-2.6.7.pom
Source3  : https://repo1.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.9.5/jackson-module-jaxb-annotations-2.9.5.jar
Source4  : https://repo1.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.9.5/jackson-module-jaxb-annotations-2.9.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-jackson-module-jaxb-annotations-data = %{version}-%{release}

%description
## Overview
This Jackson extension module provides support for using JAXB (`javax.xml.bind`) annotations as an alternative to native Jackson annotations.
It is most often used to make it easier to reuse existing data beans that used with JAXB framework to read and write XML.

%package data
Summary: data components for the mvn-jackson-module-jaxb-annotations package.
Group: Data

%description data
data components for the mvn-jackson-module-jaxb-annotations package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.6.7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.6.7/jackson-module-jaxb-annotations-2.6.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.6.7
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.6.7/jackson-module-jaxb-annotations-2.6.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.9.5
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.9.5/jackson-module-jaxb-annotations-2.9.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.9.5
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.9.5/jackson-module-jaxb-annotations-2.9.5.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.6.7/jackson-module-jaxb-annotations-2.6.7.jar
/usr/share/java/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.6.7/jackson-module-jaxb-annotations-2.6.7.pom
/usr/share/java/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.9.5/jackson-module-jaxb-annotations-2.9.5.jar
/usr/share/java/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.9.5/jackson-module-jaxb-annotations-2.9.5.pom
