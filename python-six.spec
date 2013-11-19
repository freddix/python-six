%define		module	six

Summary:	Python 2 and 3 compatibility utilities
Name:		python-%{module}
Version:	1.4.1
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/s/six/%{module}-%{version}.tar.gz
# Source0-md5:	bdbb9e12d3336c198695aa4cf3a61d62
URL:		http://pypi.python.org/pypi/six/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python
versions with the goal of writing Python code that is compatible
on both Python versions. See the documentation for more information
on what is provided.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/*.egg-info

