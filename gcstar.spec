# NOTES:- warnings like this: /usr/lib/rpm/perl.prov: weird, cannot determine the package name for
#	 `/mnt/hda5/tmp/gcstar-0.5.0-root-inter/usr/lib/gcstar/GCLang/BG/GCstar.pm'
#	- mark with lang() _datadir/lib/GCLang/*
#
# /usr/lib/rpm/perl.prov: weird, cannot determine the package name for `/root/tmp/gcstar-1.4.2-root-root/usr/share/gcstar/lib/GCLang/SV/GCstar.pm'
# and similar
# TODO: - fix this message, IMHO the first byte of utf8 is the source of error - see with 'less' (uzsolt)
#       - after the done of the first todo, clear the 'Provides' fields
#	- maybe create subpackage
#	- fix permssions of /usr/share/gcstar/helpers/xdg-open (or use system xdg-open)
#
%include	/usr/lib/rpm/macros.perl
Summary:	GCstar: collection manager
Summary(hu.UTF-8):	GCstar: gyűjtemény kezelő
Summary(pl.UTF-8):	GCstar: zarządca kolekcji
Name:		gcstar
Version:	1.7.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://download.gna.org/gcstar/%{name}-%{version}.tar.gz
# Source0-md5:	94d0c4d6acc912b4b4d3a72d934cc16d
Patch0:		%{name}-mandir.patch
Patch1:		%{name}-desktop.patch
# copy gcstar perl-libs to /usr/share instead of /usr/lib
Patch2:		%{name}-perlmoddir.patch
URL:		http://www.gcstar.org/
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-Gtk2
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-Sort-Naturally
BuildRequires:	perl-XML-LibXML
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov
Requires(post,postun):	desktop-file-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# parts of Gtk2.pm package
%define gtk2_subpkgs	Dialog\\\\|MenuBar\\\\|MessageDialog\\\\|ScrolledWindow\\\\|Toolbar\\\\|TreeView\\\\|VBox\\\\|Window

# don't require/provide itself, it isn't in standard search path
%define	_noautoprov	^perl(GC.*)$
%define	_noautoreq	^perl(GC.*)$ ^perl(Gtk2::\\\\(%{gtk2_subpkgs}\\\\))$

%description
GCstar is an application to manage different kind of collections. It
is designed to be able to support as many type of collections as
needed. For the moment it supports these ones:
 - Movies
 - Video games
 - Books
 - User defined collections

%description -l hu.UTF-8
GCstar egy alkalmazás, amellyel gyűjtemények különféle fajtáit
tarthatjuk nyilván. Annyi típusú gyűjteményt tud kezelni, amennyire
csak szükségünk lehet. Jelenleg a következőket:
 - filmek
 - videójátékok
 - könyvek
 - felhasználó által definiált gyűjtemények

%description -l pl.UTF-8
GCstar jest aplikacją do zarządzania różnymi rodzajami kolekcji. Jest
zaprojektowana by móc wspierać wszystkie potrzebne typy kolekcji.
Aktualnie wspiera kolekcje:
 - filmów
 - gier wideo
 - książek
 - kolekcje zdefiniowane przez użytkownika

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

#rm BOM from files - it can confuse perl.prov
find -type f -name '*.pm' | xargs sed -i 's/^\xef\xbb\xbf//'

%install
rm -rf $RPM_BUILD_ROOT

./install --text \
	--prefix=$RPM_BUILD_ROOT%{_prefix}

install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install share/applications/gcstar.desktop $RPM_BUILD_ROOT%{_desktopdir}
install share/gcstar/icons/gcstar_64x64.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor
%update_mime_database

%postun
%update_desktop_database_postun
%update_icon_cache hicolor
%update_mime_database

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/gcstar
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/genres
%{_datadir}/%{name}/helpers
%{_datadir}/%{name}/html_models
%{_datadir}/%{name}/icons
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/GCBackend
%{_datadir}/%{name}/lib/GCExport
%{_datadir}/%{name}/lib/GCExtract
%{_datadir}/%{name}/lib/GCGraphicComponents
%{_datadir}/%{name}/lib/GCImport
%{_datadir}/%{name}/lib/GCItemsLists
%{_datadir}/%{name}/lib/GCLang
%{_datadir}/%{name}/lib/GCModels
%{_datadir}/%{name}/lib/GCPlugins
%{_datadir}/%{name}/lib/*.pm
%{_datadir}/%{name}/list_bg
%{_datadir}/%{name}/logos
%{_datadir}/%{name}/overlays
%{_datadir}/%{name}/panels
%{_datadir}/%{name}/schemas
%{_datadir}/%{name}/style
%{_datadir}/%{name}/xml_models
%{_datadir}/%{name}/xslt
%{_mandir}/man1/gcstar.1*
%{_desktopdir}/gcstar.desktop
%{_pixmapsdir}/gcstar.png
