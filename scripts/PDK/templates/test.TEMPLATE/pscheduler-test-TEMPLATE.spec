#
# RPM Spec for pScheduler TEMPLATE Test
#

#
# Development Order #1:
#
# This file is significant for building the test into pScheduler.
# If additional libraries or parts of pScheduler are required,
# they should be added here after line 25.
#

%define short	TEMPLATE
%define perfsonar_auto_version 4.4.0
%define perfsonar_auto_relnum 0.5.b1

Name:		pscheduler-test-%{short}
Version:	%{perfsonar_auto_version}
Release:	%{perfsonar_auto_relnum}%{?dist}

Summary:	TEMPLATE test for pScheduler
BuildArch:	noarch
License:	Apache 2.0
Group:		Unspecified

Source0:	%{short}-%{version}.tar.gz

Provides:	%{name} = %{version}-%{release}

# Include all required libraries here
Requires:	pscheduler-server
Requires:	%{_pscheduler_python}-pscheduler >= 1.3
Requires:	%{_pscheduler_python}-jsontemplate

BuildRequires:	pscheduler-rpm


%description
TEMPLATE test class for pScheduler


%prep
%setup -q -n %{short}-%{version}


%define dest %{_pscheduler_test_libexec}/%{short}

%build
make \
     PYTHON=%{_pscheduler_python} \
     DESTDIR=$RPM_BUILD_ROOT/%{dest} \
     install



%post
pscheduler internal warmboot


%postun
pscheduler internal warmboot


%files
%defattr(-,root,root,-)
%{dest}
