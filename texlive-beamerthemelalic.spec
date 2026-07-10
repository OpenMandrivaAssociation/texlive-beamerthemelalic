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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the beamer theme for LALIC (Laboratorio de
Linguistica e Inteligencia Computacional of the Federal University of
Sao Carlos, Brazil).

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
%dir %{_datadir}/texmf-dist/doc/latex/beamerthemelalic
%dir %{_datadir}/texmf-dist/tex/latex/beamerthemelalic
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemelalic/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemelalic/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemelalic/beamerthemelalic-exemplo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemelalic/beamerthemelalic-exemplo.tex
%{_datadir}/texmf-dist/tex/latex/beamerthemelalic/beamercolorthemelalic.sty
%{_datadir}/texmf-dist/tex/latex/beamerthemelalic/beamerfontthemelalic.sty
%{_datadir}/texmf-dist/tex/latex/beamerthemelalic/beamerinnerthemelalic.sty
%{_datadir}/texmf-dist/tex/latex/beamerthemelalic/beamerouterthemelalic.sty
%{_datadir}/texmf-dist/tex/latex/beamerthemelalic/beamerthemelalic.sty
