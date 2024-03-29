Name:		python-sphinx-markdown-tables
Version:	0.0.17
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-markdown-tables/sphinx-markdown-tables-%{version}.tar.gz
Summary:	A Sphinx extension for rendering tables written in markdown
URL:		https://pypi.org/project/sphinx-markdown-tables/
License:	GPL
Group:		Development/Python
BuildRequires:	python-setuptools
# Rather hard to trace because of the obscure error message:
# 'PathDistribution' object has no attribute '_normalized_name'
# (without a backtrace indicating where that comes from)
Conflicts:	python%{py_ver}dist(importlib-metadata) < 4.3.0
BuildArch:	noarch

%description
A Sphinx extension for rendering tables written in markdown

%prep
%autosetup -p1 -n sphinx-markdown-tables-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}
# License files don't belong straight to /usr
rm -f %{buildroot}%{_prefix}/LICENSE

%files
%{py_puresitedir}/sphinx_markdown_tables
%{py_puresitedir}/sphinx_markdown_tables*.egg-info
