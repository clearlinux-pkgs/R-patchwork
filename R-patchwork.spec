#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-patchwork
Version  : 1.1.2
Release  : 7
URL      : https://cran.r-project.org/src/contrib/patchwork_1.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/patchwork_1.1.2.tar.gz
Summary  : The Composer of Plots
Group    : Development/Tools
License  : MIT
Requires: R-ggplot2
Requires: R-gtable
BuildRequires : R-ggplot2
BuildRequires : R-gtable
BuildRequires : R-vdiffr
BuildRequires : buildreq-R

%description
building up a plot, but does not concern itself with composition of multiple
    plots. 'patchwork' is a package that expands the API to allow for 
    arbitrarily complex composition of plots by, among others, providing 
    mathematical operators for combining multiple plots. Other packages that try 
    to address this need (but with a different approach) are 'gridExtra' and 
    'cowplot'.

%prep
%setup -q -n patchwork
cd %{_builddir}/patchwork

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661188158

%install
export SOURCE_DATE_EPOCH=1661188158
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/patchwork/DESCRIPTION
/usr/lib64/R/library/patchwork/INDEX
/usr/lib64/R/library/patchwork/LICENSE
/usr/lib64/R/library/patchwork/Meta/Rd.rds
/usr/lib64/R/library/patchwork/Meta/features.rds
/usr/lib64/R/library/patchwork/Meta/hsearch.rds
/usr/lib64/R/library/patchwork/Meta/links.rds
/usr/lib64/R/library/patchwork/Meta/nsInfo.rds
/usr/lib64/R/library/patchwork/Meta/package.rds
/usr/lib64/R/library/patchwork/Meta/vignette.rds
/usr/lib64/R/library/patchwork/NAMESPACE
/usr/lib64/R/library/patchwork/NEWS.md
/usr/lib64/R/library/patchwork/R/patchwork
/usr/lib64/R/library/patchwork/R/patchwork.rdb
/usr/lib64/R/library/patchwork/R/patchwork.rdx
/usr/lib64/R/library/patchwork/doc/index.html
/usr/lib64/R/library/patchwork/doc/patchwork.R
/usr/lib64/R/library/patchwork/doc/patchwork.Rmd
/usr/lib64/R/library/patchwork/doc/patchwork.html
/usr/lib64/R/library/patchwork/help/AnIndex
/usr/lib64/R/library/patchwork/help/aliases.rds
/usr/lib64/R/library/patchwork/help/figures/README-example-1.png
/usr/lib64/R/library/patchwork/help/figures/README-unnamed-chunk-10-1.png
/usr/lib64/R/library/patchwork/help/figures/README-unnamed-chunk-11-1.png
/usr/lib64/R/library/patchwork/help/figures/README-unnamed-chunk-2-1.png
/usr/lib64/R/library/patchwork/help/figures/README-unnamed-chunk-3-1.png
/usr/lib64/R/library/patchwork/help/figures/README-unnamed-chunk-4-1.png
/usr/lib64/R/library/patchwork/help/figures/README-unnamed-chunk-5-1.png
/usr/lib64/R/library/patchwork/help/figures/README-unnamed-chunk-6-1.png
/usr/lib64/R/library/patchwork/help/figures/README-unnamed-chunk-7-1.png
/usr/lib64/R/library/patchwork/help/figures/README-unnamed-chunk-8-1.png
/usr/lib64/R/library/patchwork/help/figures/README-unnamed-chunk-9-1.png
/usr/lib64/R/library/patchwork/help/figures/logo.png
/usr/lib64/R/library/patchwork/help/figures/logo.svg
/usr/lib64/R/library/patchwork/help/patchwork.rdb
/usr/lib64/R/library/patchwork/help/patchwork.rdx
/usr/lib64/R/library/patchwork/help/paths.rds
/usr/lib64/R/library/patchwork/html/00Index.html
/usr/lib64/R/library/patchwork/html/R.css
/usr/lib64/R/library/patchwork/tests/figs/add-base-graphics-p1-plot-1-10-1-10.svg
/usr/lib64/R/library/patchwork/tests/figs/add-ggplot-elements-p1-p2-theme-bw.svg
/usr/lib64/R/library/patchwork/tests/figs/add-grob-p1-textgrob-test.svg
/usr/lib64/R/library/patchwork/tests/figs/add-patchwork-to-plot-p1-p2-p3.svg
/usr/lib64/R/library/patchwork/tests/figs/adding-to-all-on-level-patchwork-theme-bw.svg
/usr/lib64/R/library/patchwork/tests/figs/adding-to-all-subplots-patchwork-theme-bw.svg
/usr/lib64/R/library/patchwork/tests/figs/adding-to-patchwork-p1-p2-p3.svg
/usr/lib64/R/library/patchwork/tests/figs/basic-inset-works.svg
/usr/lib64/R/library/patchwork/tests/figs/complex-composition-p1-p2-p3-p4.svg
/usr/lib64/R/library/patchwork/tests/figs/deps.txt
/usr/lib64/R/library/patchwork/tests/figs/far-dimensions-can-be-set-with-units.svg
/usr/lib64/R/library/patchwork/tests/figs/far-legend-justification.svg
/usr/lib64/R/library/patchwork/tests/figs/far-optimise-space-by-default-p-f-p-f-p3-p4.svg
/usr/lib64/R/library/patchwork/tests/figs/far-optimise-space-by-default-p1-p-f-p-f-p4.svg
/usr/lib64/R/library/patchwork/tests/figs/far-optimise-space-by-default-p1-p-f-p3-p4.svg
/usr/lib64/R/library/patchwork/tests/figs/far-space-optimisation-can-be-turned-off-p1-p2-p-f-p4-plot-layout-widths-1.svg
/usr/lib64/R/library/patchwork/tests/figs/grobs-can-be-inset.svg
/usr/lib64/R/library/patchwork/tests/figs/insets-can-be-changed.svg
/usr/lib64/R/library/patchwork/tests/figs/nest-left-hand-side-p1-p2-p3.svg
/usr/lib64/R/library/patchwork/tests/figs/nest-right-hand-side-p1-p2-p3.svg
/usr/lib64/R/library/patchwork/tests/figs/other-alignments-work.svg
/usr/lib64/R/library/patchwork/tests/figs/pack-4-plots-p1-p2-p3-p4.svg
/usr/lib64/R/library/patchwork/tests/figs/patchworks-can-be-inset.svg
/usr/lib64/R/library/patchwork/tests/figs/setting-heights-as-units-p1-p2-p3-p4-plot-layout-heights-unit-3-cm.svg
/usr/lib64/R/library/patchwork/tests/figs/setting-heights-p1-p2-p3-p4-plot-layout-heights-c-1-2.svg
/usr/lib64/R/library/patchwork/tests/figs/setting-ncol-p1-p2-p3-p4-plot-layout-ncol-3.svg
/usr/lib64/R/library/patchwork/tests/figs/setting-nrow-p1-p2-p3-p4-plot-layout-nrow-3.svg
/usr/lib64/R/library/patchwork/tests/figs/setting-widths-as-units-p1-p2-p3-p4-plot-layout-widths-unit-3-cm.svg
/usr/lib64/R/library/patchwork/tests/figs/setting-widths-p1-p2-p3-p4-plot-layout-widths-c-1-2.svg
/usr/lib64/R/library/patchwork/tests/figs/stack-3-plots-p1-p2-p3.svg
/usr/lib64/R/library/patchwork/tests/figs/standard-addition-p1-p2-p3.svg
/usr/lib64/R/library/patchwork/tests/testthat.R
/usr/lib64/R/library/patchwork/tests/testthat/helper-setup.R
/usr/lib64/R/library/patchwork/tests/testthat/helper-vdiffr.R
/usr/lib64/R/library/patchwork/tests/testthat/test-arithmetic.R
/usr/lib64/R/library/patchwork/tests/testthat/test-layout.R
