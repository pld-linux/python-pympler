#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Tool to measure, monitor and analyse the memory behaviour of Python 2 objects
Summary(pl.UTF-8):	Narzędzie do pomiaru, monitorowania i analizy zachowania pamięciowego obiektów Pythona 2
Name:		python-pympler
Version:	0.5
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pympler/
Source0:	https://files.pythonhosted.org/packages/source/P/Pympler/Pympler-%{version}.tar.gz
# Source0-md5:	831d12beca2ff2ea56407c5ed8ffc4b0
URL:		https://pythonhosted.org/Pympler/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pympler is a development tool to measure, monitor and analyse the
memory behaviour of Python objects in a running Python application.

%description -l pl.UTF-8
Pympler to narzędzie programistyczne do pomiaru, monitorowania i
analizy zachowania pamięciowego obiektów Pythona w działającej
aplikacji.

%package -n python3-pympler
Summary:	Tool to measure, monitor and analyse the memory behaviour of Python 3 objects
Summary(pl.UTF-8):	Narzędzie do pomiaru, monitorowania i analizy zachowania pamięciowego obiektów Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pympler
Pympler is a development tool to measure, monitor and analyse the
memory behaviour of Python objects in a running Python application.

%description -n python3-pympler -l pl.UTF-8
Pympler to narzędzie programistyczne do pomiaru, monitorowania i
analizy zachowania pamięciowego obiektów Pythona w działającej
aplikacji.

%prep
%setup -q -n Pympler-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python} test/runtest.py -post-install -verbose 3
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} test/runtest.py -post-install -verbose 3
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NOTICE README.md
%{py_sitescriptdir}/pympler
%{py_sitescriptdir}/Pympler-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pympler
%defattr(644,root,root,755)
%doc NOTICE README.md
%{py3_sitescriptdir}/pympler
%{py3_sitescriptdir}/Pympler-%{version}-py*.egg-info
%endif