Name:		python-sphinx-markdown-tables
Version:	0.0.17
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-markdown-tables/sphinx-markdown-tables-%{version}.tar.gz
Summary:	A Sphinx extension for rendering tables written in markdown
URL:		https://pypi.org/project/sphinx-markdown-tables/
License:	GPL
Group:		Development/Python
BuildRequires:	python-setuptools
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
