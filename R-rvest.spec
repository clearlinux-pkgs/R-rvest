#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v4
# autospec commit: da8b975
#
Name     : R-rvest
Version  : 1.0.4
Release  : 57
URL      : https://cran.r-project.org/src/contrib/rvest_1.0.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rvest_1.0.4.tar.gz
Summary  : Easily Harvest (Scrape) Web Pages
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-glue
Requires: R-httr
Requires: R-lifecycle
Requires: R-magrittr
Requires: R-rlang
Requires: R-selectr
Requires: R-tibble
Requires: R-xml2
BuildRequires : R-cli
BuildRequires : R-glue
BuildRequires : R-httr
BuildRequires : R-lifecycle
BuildRequires : R-magrittr
BuildRequires : R-rlang
BuildRequires : R-selectr
BuildRequires : R-tibble
BuildRequires : R-xml2
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
easy to download, then manipulate, HTML and XML.

%prep
%setup -q -n rvest
pushd ..
cp -a rvest buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707840234

%install
export SOURCE_DATE_EPOCH=1707840234
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rvest/DESCRIPTION
/usr/lib64/R/library/rvest/INDEX
/usr/lib64/R/library/rvest/LICENSE
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
/usr/lib64/R/library/rvest/R/sysdata.rdb
/usr/lib64/R/library/rvest/R/sysdata.rdx
/usr/lib64/R/library/rvest/WORDLIST
/usr/lib64/R/library/rvest/demo/tripadvisor.R
/usr/lib64/R/library/rvest/demo/united.R
/usr/lib64/R/library/rvest/demo/zillow.R
/usr/lib64/R/library/rvest/doc/index.html
/usr/lib64/R/library/rvest/doc/rvest.R
/usr/lib64/R/library/rvest/doc/rvest.Rmd
/usr/lib64/R/library/rvest/doc/rvest.html
/usr/lib64/R/library/rvest/doc/starwars.R
/usr/lib64/R/library/rvest/doc/starwars.Rmd
/usr/lib64/R/library/rvest/doc/starwars.html
/usr/lib64/R/library/rvest/help/AnIndex
/usr/lib64/R/library/rvest/help/aliases.rds
/usr/lib64/R/library/rvest/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/rvest/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/rvest/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/rvest/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/rvest/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/rvest/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/rvest/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/rvest/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/rvest/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/rvest/help/figures/logo.png
/usr/lib64/R/library/rvest/help/paths.rds
/usr/lib64/R/library/rvest/help/rvest.rdb
/usr/lib64/R/library/rvest/help/rvest.rdx
/usr/lib64/R/library/rvest/html-ex/bad-encoding.html
/usr/lib64/R/library/rvest/html/00Index.html
/usr/lib64/R/library/rvest/html/R.css
/usr/lib64/R/library/rvest/tests/spelling.R
/usr/lib64/R/library/rvest/tests/testthat.R
/usr/lib64/R/library/rvest/tests/testthat/_snaps/encoding.md
/usr/lib64/R/library/rvest/tests/testthat/_snaps/form.md
/usr/lib64/R/library/rvest/tests/testthat/_snaps/html.md
/usr/lib64/R/library/rvest/tests/testthat/_snaps/live.md
/usr/lib64/R/library/rvest/tests/testthat/_snaps/rename.md
/usr/lib64/R/library/rvest/tests/testthat/_snaps/selectors.md
/usr/lib64/R/library/rvest/tests/testthat/_snaps/session.md
/usr/lib64/R/library/rvest/tests/testthat/_snaps/table.md
/usr/lib64/R/library/rvest/tests/testthat/_snaps/utils.md
/usr/lib64/R/library/rvest/tests/testthat/helper.R
/usr/lib64/R/library/rvest/tests/testthat/html/bullets.html
/usr/lib64/R/library/rvest/tests/testthat/html/click.html
/usr/lib64/R/library/rvest/tests/testthat/html/press.html
/usr/lib64/R/library/rvest/tests/testthat/html/scroll.html
/usr/lib64/R/library/rvest/tests/testthat/html/table.html
/usr/lib64/R/library/rvest/tests/testthat/html/type.html
/usr/lib64/R/library/rvest/tests/testthat/test-encoding.R
/usr/lib64/R/library/rvest/tests/testthat/test-form.R
/usr/lib64/R/library/rvest/tests/testthat/test-html.R
/usr/lib64/R/library/rvest/tests/testthat/test-live.R
/usr/lib64/R/library/rvest/tests/testthat/test-rename.R
/usr/lib64/R/library/rvest/tests/testthat/test-selectors.R
/usr/lib64/R/library/rvest/tests/testthat/test-session.R
/usr/lib64/R/library/rvest/tests/testthat/test-table.R
/usr/lib64/R/library/rvest/tests/testthat/test-text.R
/usr/lib64/R/library/rvest/tests/testthat/test-utils.R
/usr/lib64/R/library/rvest/tests/testthat/test.html
