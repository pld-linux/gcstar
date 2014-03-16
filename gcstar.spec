# NOTES: - warnings like this: /usr/lib/rpm/perl.prov: weird, cannot determine the package name for
#	 `/mnt/hda5/tmp/gcstar-0.5.0-root-inter/usr/lib/gcstar/GCLang/BG/GCstar.pm'
#	Above is caused by mismatches of file/dir names of *.pm files and "package PKGNAME;" declarations.
#	Fixing this is real PITA, moreover - our perl.{prov,req} don't handle declarations
#	more then 1 package in 1 file.
#	Anyway we don't want to provide/requires perl modules from non-standard dirs
#
# TODO:
#	- split font package or rm fonts (included in fonts-TTF-RedHat-liberation?)
#
%include	/usr/lib/rpm/macros.perl
Summary:	GCstar: collection manager
Summary(hu.UTF-8):	GCstar: gyűjtemény kezelő
Summary(pl.UTF-8):	GCstar: zarządca kolekcji
Name:		gcstar
Version:	1.7.0
Release:	0.2
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.gna.org/gcstar/%{name}-%{version}.tar.gz
# Source0-md5:	94d0c4d6acc912b4b4d3a72d934cc16d
Patch0:		%{name}-mandir.patch
Patch1:		%{name}-desktop.patch
# copy gcstar perl-libs to /usr/share instead of /usr/lib
Patch2:		%{name}-perlmoddir.patch
Patch3:		system-xdgopen.patch
URL:		http://www.gcstar.org/
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-Gtk2
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-Sort-Naturally
BuildRequires:	perl-XML-LibXML
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	xdg-utils
Requires(post,postun):	desktop-file-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# don't provide itself, it isn't in standard search path
%define	_noautoprov	'perl\\(GC.*\\)'
# don't require itself, it isn't in standard search path and subpackages of Gtk2.pm
%define _noautoreq_perl		GC.* Gtk2::Dialog Gtk2::EventBox Gtk2::Frame Gtk2::HBox Gtk2::MenuBar Gtk2::MessageDialog Gtk2::ScrolledWindow Gtk2::SimpleList Gtk2::Table Gtk2::Toolbar Gtk2::TreeView Gtk2::VBox Gtk2::Window

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
%patch3 -p1

#rm BOM from files - it can confuse perl.prov
find -type f -name '*.pm' | xargs sed -i 's/^\xef\xbb\xbf//'

%install
rm -rf $RPM_BUILD_ROOT

./install --text \
	--nomenu --noclean \
	--prefix=$RPM_BUILD_ROOT%{_prefix}

install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install share/applications/gcstar.desktop $RPM_BUILD_ROOT%{_desktopdir}
install share/gcstar/icons/gcstar_64x64.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,22x22,24x24,32x32,36x36,48x48,64x64,72x72,96x96,128x128,192x192,256x256,scalable}/apps
install share/gcstar/icons/gcstar_16x16.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install share/gcstar/icons/gcstar_22x22.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/22x22/apps/%{name}.png
install share/gcstar/icons/gcstar_24x24.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/24x24/apps/%{name}.png
install share/gcstar/icons/gcstar_32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install share/gcstar/icons/gcstar_36x36.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/36x36/apps/%{name}.png
install share/gcstar/icons/gcstar_48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install share/gcstar/icons/gcstar_64x64.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install share/gcstar/icons/gcstar_72x72.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/72x72/apps/%{name}.png
install share/gcstar/icons/gcstar_96x96.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/96x96/apps/%{name}.png
install share/gcstar/icons/gcstar_128x128.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/128x128/apps/%{name}.png
install share/gcstar/icons/gcstar_192x192.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/192x192/apps/%{name}.png
install share/gcstar/icons/gcstar_256x256.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/256x256/apps/%{name}.png
install share/gcstar/icons/gcstar_scalable.svg $RPM_BUILD_ROOT%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

install -d $RPM_BUILD_ROOT%{_datadir}/mime/packages
install share/applications/gcstar.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages

%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/LICENSE
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/helpers/xdg-open
%{__rmdir} $RPM_BUILD_ROOT%{_datadir}/%{name}/helpers

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
%{_datadir}/%{name}/html_models
%{_datadir}/%{name}/icons
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/GCBackend
%{_datadir}/%{name}/lib/GCExport
%{_datadir}/%{name}/lib/GCExtract
%{_datadir}/%{name}/lib/GCGraphicComponents
%{_datadir}/%{name}/lib/GCImport
%{_datadir}/%{name}/lib/GCItemsLists
%dir %{_datadir}/%{name}/lib/GCLang
%lang(ar) %{_datadir}/%{name}/lib/GCLang/AR
%lang(bg) %{_datadir}/%{name}/lib/GCLang/BG
%lang(ca) %{_datadir}/%{name}/lib/GCLang/CA
%lang(cs) %{_datadir}/%{name}/lib/GCLang/CS
%lang(de) %{_datadir}/%{name}/lib/GCLang/DE
%lang(el) %{_datadir}/%{name}/lib/GCLang/EL
%lang(en) %{_datadir}/%{name}/lib/GCLang/EN
%lang(es) %{_datadir}/%{name}/lib/GCLang/ES
%lang(fr) %{_datadir}/%{name}/lib/GCLang/FR
%lang(gl) %{_datadir}/%{name}/lib/GCLang/GL
%lang(hu) %{_datadir}/%{name}/lib/GCLang/HU
%lang(id) %{_datadir}/%{name}/lib/GCLang/ID
%lang(it) %{_datadir}/%{name}/lib/GCLang/IT
%lang(nl) %{_datadir}/%{name}/lib/GCLang/NL
%lang(pl) %{_datadir}/%{name}/lib/GCLang/PL
%lang(pt) %{_datadir}/%{name}/lib/GCLang/PT
%lang(ro) %{_datadir}/%{name}/lib/GCLang/RO
%lang(ru) %{_datadir}/%{name}/lib/GCLang/RU
%lang(sr) %{_datadir}/%{name}/lib/GCLang/SR
%lang(sv) %{_datadir}/%{name}/lib/GCLang/SV
%lang(tr) %{_datadir}/%{name}/lib/GCLang/TR
%lang(uk) %{_datadir}/%{name}/lib/GCLang/UK
%lang(zh) %{_datadir}/%{name}/lib/GCLang/ZH
%lang(zh_CN) %{_datadir}/%{name}/lib/GCLang/ZH_CN
%{_datadir}/%{name}/lib/GCLang/GCLangUtils.pm
%{_datadir}/%{name}/lib/GCLang/README
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
%{_iconsdir}/hicolor/*/apps/gcstar.*
%{_datadir}/mime/packages/gcstar.xml
