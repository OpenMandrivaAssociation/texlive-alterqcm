%global tl_name alterqcm
%global tl_revision 59265

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.42c
Release:	%{tl_revision}.1
Summary:	Multiple choice questionnaires in two column tables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/alterqcm
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alterqcm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alterqcm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The alterqcm package is a LaTeX2e package, for making multiple choices
questionnaires in a table with two columns. The aim is to provide some
useful macros to build QCM in tables. These macros may be used by only
LaTeX TeX users. The package works with utf8, pdfLaTeX, LuaLaTeX and
XeLaTeX (with some languages). The documentation is in English.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/alterqcm
%dir %{_datadir}/texmf-dist/tex/latex/alterqcm
%dir %{_datadir}/texmf-dist/doc/latex/alterqcm/examples
%dir %{_datadir}/texmf-dist/doc/latex/alterqcm/latex
%dir %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/iut
%dir %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/README.md
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/article_post.pdf
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/doc-aq-main.pdf
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/iut/qcm-1.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/iut/qcm-10.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/iut/qcm-2.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/iut/qcm-3.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/iut/qcm-4.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/iut/qcm-5.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/iut/qcm-6.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/iut/qcm-7.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/iut/qcm-8.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/iut/qcm-9.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/AntillesESjuin2006.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/alea.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/annexe.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/correct.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/example_2.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/example_3.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/lang_chinese.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/lang_german.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/language.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/points.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/sep.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/test_language.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/transparent-final.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/transparent-init.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/examples/latex/verb.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/180px-Gustave_Moreau_007.jpg
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/240px-Mort_du_fossoyeur.jpg
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/The_Wounded_Angel_-_Hugo_Simberg.jpg
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/doc-aq-def.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/doc-aq-excomp.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/doc-aq-first.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/doc-aq-globales.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/doc-aq-greek.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/doc-aq-installation.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/doc-aq-locales.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/doc-aq-main.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/doc-aq-mc.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/doc-aq-points.tex
%doc %{_datadir}/texmf-dist/doc/latex/alterqcm/latex/doc-aq-problem.tex
%{_datadir}/texmf-dist/tex/latex/alterqcm/alterqcm.sty
