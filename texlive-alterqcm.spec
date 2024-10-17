Name:		texlive-alterqcm
Version:	59265
Release:	2
Summary:	Multiple choice questionnaires in two column tables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/alterqcm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alterqcm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alterqcm.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/alterqcm
%doc %{_texmfdistdir}/doc/latex/alterqcm

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
