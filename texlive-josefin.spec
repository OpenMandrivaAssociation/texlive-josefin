%global tl_name josefin
%global tl_revision 78793

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Josefin fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/josefin
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/josefin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/josefin.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Josefin Sans family of fonts, designed by Santiago Orozco of the
Typemade foundry in Monterey, Mexico. Josefin Sans is available in seven
weights, with corresponding italics.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from josefin:
Map josefin.map
TL_DROPIN_EOF
