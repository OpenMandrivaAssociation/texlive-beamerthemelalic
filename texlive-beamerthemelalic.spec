Name:		texlive-beamerthemelalic
Version:	58777
Release:	2
Summary:	A beamer theme for LALIC
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamerthemelalic
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemelalic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemelalic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the beamer theme for LALIC (Laboratorio
de Linguistica e Inteligencia Computacional of the Federal
University of Sao Carlos, Brazil).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamerthemelalic
%doc %{_texmfdistdir}/doc/latex/beamerthemelalic

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
