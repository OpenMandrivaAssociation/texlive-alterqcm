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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The alterqcm package is a LaTeX2e package, for making multiple choices
questionnaires in a table with two columns. The aim is to provide some
useful macros to build QCM in tables. These macros may be used by only
LaTeX TeX users. The package works with utf8, pdfLaTeX, LuaLaTeX and
XeLaTeX (with some languages). The documentation is in English.

