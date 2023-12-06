Name:		texlive-expex-acro
Version:	68046
Release:	1
Summary:	Wrapper for the expex package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/expex-acro
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expex-acro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expex-acro.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expex-acro.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a small wrapper for the expex package, adding ways to
define, use, and summarize glossing abbreviations. It also
provides commands to refer to examples, as well as some inline
formatting commands commonly used in linguistics.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/expex-acro
%{_texmfdistdir}/tex/generic/expex-acro
%doc %{_texmfdistdir}/doc/generic/expex-acro

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
