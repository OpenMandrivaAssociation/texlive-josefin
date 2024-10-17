Name:		texlive-josefin
Version:	64569
Release:	2
Summary:	Josefin fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/josefin
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/josefin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/josefin.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Josefin Sans family of fonts, designed by
Santiago Orozco of the Typemade foundry in Monterey, Mexico.
Josefin Sans is available in seven weights, with corresponding
italics.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/josefin
%{_texmfdistdir}/fonts/vf/public/josefin
%{_texmfdistdir}/fonts/type1/public/josefin
%{_texmfdistdir}/fonts/truetype/public/josefin
%{_texmfdistdir}/fonts/tfm/public/josefin
%{_texmfdistdir}/fonts/map/dvips/josefin
%{_texmfdistdir}/fonts/enc/dvips/josefin
%doc %{_texmfdistdir}/doc/fonts/josefin

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
