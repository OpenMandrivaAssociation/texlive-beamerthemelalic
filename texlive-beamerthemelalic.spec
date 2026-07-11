%global tl_name beamerthemelalic
%global tl_revision 58777

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A beamer theme for LALIC
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamerthemelalic
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemelalic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemelalic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the beamer theme for LALIC (Laboratorio de
Linguistica e Inteligencia Computacional of the Federal University of
Sao Carlos, Brazil).

