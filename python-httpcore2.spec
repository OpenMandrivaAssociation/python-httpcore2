Name:		python-httpcore2
Version:	2.13.1
Release:	2
Summary:	Minimal low-level HTTP client
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/pydantic/httpx2
Source0:	https://files.pythonhosted.org/packages/source/h/httpcore2/httpcore2-%{version}.tar.gz
# uv-dynamic-versioning is not packaged. Without a git checkout the
# sdist would be stamped 0.0.0.
Patch0:		httpcore2-static-version.patch
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)

%description
httpcore2 is the low-level sync and async HTTP transport used by
httpx2. This is the 2.13.1 release, which httpx2 2.13.1 requires
exactly.

%files
%doc README.md CHANGELOG.md
%license LICENSE.md
%{py_sitedir}/httpcore2
%{py_sitedir}/httpcore2-*.*-info
