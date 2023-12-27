#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-tabulate
Version  : 0.9.0
Release  : 40
URL      : https://files.pythonhosted.org/packages/ec/fe/802052aecb21e3797b8f7902564ab6ea0d60ff8ca23952079064155d1ae1/tabulate-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ec/fe/802052aecb21e3797b8f7902564ab6ea0d60ff8ca23952079064155d1ae1/tabulate-0.9.0.tar.gz
Summary  : Pretty-print tabular data
Group    : Development/Tools
License  : MIT
Requires: pypi-tabulate-bin = %{version}-%{release}
Requires: pypi-tabulate-license = %{version}-%{release}
Requires: pypi-tabulate-python = %{version}-%{release}
Requires: pypi-tabulate-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(build)
BuildRequires : pypi(numpy)
BuildRequires : pypi(pandas)
BuildRequires : pypi(pip)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(tox)
BuildRequires : pypi(wcwidth)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pytest

%description


%package bin
Summary: bin components for the pypi-tabulate package.
Group: Binaries
Requires: pypi-tabulate-license = %{version}-%{release}

%description bin
bin components for the pypi-tabulate package.


%package license
Summary: license components for the pypi-tabulate package.
Group: Default

%description license
license components for the pypi-tabulate package.


%package python
Summary: python components for the pypi-tabulate package.
Group: Default
Requires: pypi-tabulate-python3 = %{version}-%{release}

%description python
python components for the pypi-tabulate package.


%package python3
Summary: python3 components for the pypi-tabulate package.
Group: Default
Requires: python3-core
Provides: pypi(tabulate)
Requires: pypi(build)
Requires: pypi(numpy)
Requires: pypi(pandas)
Requires: pypi(pip)
Requires: pypi(tox)
Requires: pypi(wcwidth)

%description python3
python3 components for the pypi-tabulate package.


%prep
%setup -q -n tabulate-0.9.0
cd %{_builddir}/tabulate-0.9.0
pushd ..
cp -a tabulate-0.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665153590
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export PYTHONPATH="${PYTHONPATH:+$PYTHONPATH:}$PWD"
pytest ./test/

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tabulate
cp %{_builddir}/tabulate-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tabulate/5089547e34dff8c7165575b355b8b5a2829cae95 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tabulate

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tabulate/5089547e34dff8c7165575b355b8b5a2829cae95

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
