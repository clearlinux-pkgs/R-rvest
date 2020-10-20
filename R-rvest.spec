#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rvest
Version  : 0.3.6
Release  : 32
URL      : https://cran.r-project.org/src/contrib/rvest_0.3.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rvest_0.3.6.tar.gz
Summary  : Easily Harvest (Scrape) Web Pages
Group    : Development/Tools
License  : GPL-3.0
Requires: R-httr
Requires: R-magrittr
Requires: R-png
Requires: R-selectr
Requires: R-xml2
BuildRequires : R-httr
BuildRequires : R-magrittr
BuildRequires : R-png
BuildRequires : R-selectr
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
make it easy to download, then manipulate, HTML and XML.

%prep
%setup -q -c -n rvest
cd %{_builddir}/rvest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595867700

%install
export SOURCE_DATE_EPOCH=1595867700
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rvest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rvest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rvest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rvest || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rvest/DESCRIPTION
/usr/lib64/R/library/rvest/INDEX
/usr/lib64/R/library/rvest/Meta/Rd.rds
/usr/lib64/R/library/rvest/Meta/demo.rds
/usr/lib64/R/library/rvest/Meta/features.rds
/usr/lib64/R/library/rvest/Meta/hsearch.rds
/usr/lib64/R/library/rvest/Meta/links.rds
/usr/lib64/R/library/rvest/Meta/nsInfo.rds
/usr/lib64/R/library/rvest/Meta/package.rds
/usr/lib64/R/library/rvest/Meta/vignette.rds
/usr/lib64/R/library/rvest/NAMESPACE
/usr/lib64/R/library/rvest/NEWS.md
/usr/lib64/R/library/rvest/R/rvest
/usr/lib64/R/library/rvest/R/rvest.rdb
/usr/lib64/R/library/rvest/R/rvest.rdx
/usr/lib64/R/library/rvest/WORDLIST
/usr/lib64/R/library/rvest/demo/tripadvisor.R
/usr/lib64/R/library/rvest/demo/united.R
/usr/lib64/R/library/rvest/demo/zillow.R
/usr/lib64/R/library/rvest/doc/harvesting-the-web.R
/usr/lib64/R/library/rvest/doc/harvesting-the-web.Rmd
/usr/lib64/R/library/rvest/doc/harvesting-the-web.html
/usr/lib64/R/library/rvest/doc/index.html
/usr/lib64/R/library/rvest/doc/selectorgadget.R
/usr/lib64/R/library/rvest/doc/selectorgadget.Rmd
/usr/lib64/R/library/rvest/doc/selectorgadget.html
/usr/lib64/R/library/rvest/help/AnIndex
/usr/lib64/R/library/rvest/help/aliases.rds
/usr/lib64/R/library/rvest/help/figures/logo.png
/usr/lib64/R/library/rvest/help/paths.rds
/usr/lib64/R/library/rvest/help/rvest.rdb
/usr/lib64/R/library/rvest/help/rvest.rdx
/usr/lib64/R/library/rvest/html-ex/bad-encoding.html
/usr/lib64/R/library/rvest/html/00Index.html
/usr/lib64/R/library/rvest/html/R.css
/usr/lib64/R/library/rvest/tests/spelling.R
/usr/lib64/R/library/rvest/tests/testthat.R
/usr/lib64/R/library/rvest/tests/testthat/test-forms.R
/usr/lib64/R/library/rvest/tests/testthat/test-selectors.R
/usr/lib64/R/library/rvest/tests/testthat/test-tables.R
/usr/lib64/R/library/rvest/tests/testthat/test.html
