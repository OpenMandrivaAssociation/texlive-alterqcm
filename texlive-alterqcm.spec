# revision 23385
# category Package
# catalog-ctan /macros/latex/contrib/alterqcm
# catalog-date 2011-06-06 00:10:59 +0200
# catalog-license lppl
# catalog-version 3.7c
Name:		texlive-alterqcm
Version:	3.7c
Release:	5
Summary:	Multiple choice questionnaires in two column tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/alterqcm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alterqcm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alterqcm.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Macros to support the creation of multiple-choice
questionnaires in two-column tables.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/alterqcm/alterqcm.sty
%doc %{_texmfdistdir}/doc/latex/alterqcm/README
%doc %{_texmfdistdir}/doc/latex/alterqcm/README.doc
%doc %{_texmfdistdir}/doc/latex/alterqcm/doc_aq-screen.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/latex/AntillesESjuin2006.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/latex/alea.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/latex/annexe.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/latex/correct.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/latex/example_1.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/latex/example_2.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/latex/language.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/latex/points.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/latex/sep.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/latex/transparent-final.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/latex/transparent-init.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/latex/verb.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/AntillesESjuin2006.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/alea.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/annexe.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/correct.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/doc_aq.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/example_1.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/example_2.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/language.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/points.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/sep.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/transparent-final.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/transparent-init.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/examples/pdf/verb.pdf
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/180px-Gustave_Moreau_007.jpg
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/240px-Mort_du_fossoyeur.jpg
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/The_Wounded_Angel_-_Hugo_Simberg.jpg
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/aq.ist
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/doc-aq-def.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/doc-aq-excomp.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/doc-aq-globales.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/doc-aq-installation.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/doc-aq-locales.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/doc-aq-mc.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/doc-aq-points.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/doc-aq-problem.tex
%doc %{_texmfdistdir}/doc/latex/alterqcm/latex/doc_aq-main.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.7c-2
+ Revision: 749164
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.7c-1
+ Revision: 717816
- texlive-alterqcm
- texlive-alterqcm
- texlive-alterqcm
- texlive-alterqcm
- texlive-alterqcm

