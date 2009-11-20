# NOTES:- warnings like this: /usr/lib/rpm/perl.prov: weird, cannot determine the package name for
#	 `/mnt/hda5/tmp/gcstar-0.5.0-root-inter/usr/lib/gcstar/GCLang/BG/GCstar.pm'
#	- mark with lang() _datadir/lib/GCLang/*
#
# /usr/lib/rpm/perl.prov: weird, cannot determine the package name for `/root/tmp/gcstar-1.4.2-root-root/usr/share/gcstar/lib/GCLang/SV/GCstar.pm'
# and similar
# TODO: - fix this message, IMHO the first byte of utf8 is the source of error - see with 'less' (uzsolt)
#       - after the done of the first todo, clear the 'Provides' fields
#	- maybe create subpackage
%include	/usr/lib/rpm/macros.perl
Summary:	GCstar: collection manager
Summary(hu.UTF-8):	GCstar: gyűjtemény kezelő
Summary(pl.UTF-8):	GCstar: zarządca kolekcji
Name:		gcstar
Version:	1.5.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.gna.org/gcstar/%{name}-%{version}.tar.gz
# Source0-md5:	966652b3f331d72c76509e13fc4dfba5
Patch0:		%{name}-mandir.patch
Patch1:		%{name}-desktop.patch
# copy gcstar perl-libs to /usr/share instead of /usr/lib
Patch2:		%{name}-perlmoddir.patch
URL:		http://www.gcstar.org/
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-Gtk2
BuildRequires:	perl-XML-LibXML
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov
Requires(post,postun):	desktop-file-utils
# I don't know why, but builder says the following:
# By install missed the following packages. /uzsolt/
Provides:	perl(GCBackend::GCBeXmlBase)
Provides:	perl(GCDoubleListDialog)
Provides:	perl(GCExport::GCExportBaseClass)
Provides:	perl(GCExportImportBase)
Provides:	perl(GCFieldsSelectionDialog)
Provides:	perl(GCImport::GCImportBaseClass)
Provides:	perl(GCItemExtracter)
Provides:	perl(GCModalDialog)
Provides:	perl(GCPluginParser)
Provides:	perl(GCPlugins::GCTVepisodes::GCPluginTvdb)
Provides:	perl(GCPlugins::GCTVepisodes::GCTVepisodesPluginsBase)
Provides:	perl(GCPlugins::GCboardgames::GCboardgamesPluginsBase)
Provides:	perl(GCPlugins::GCbooks::GCbooksAdlibrisPluginsBase)
Provides:	perl(GCPlugins::GCbooks::GCbooksAmazonPluginsBase)
Provides:	perl(GCPlugins::GCbooks::GCbooksPluginsBase)
Provides:	perl(GCPlugins::GCcomics::GCcomicsPluginsBase)
Provides:	perl(GCPlugins::GCfilms::GCfilmsAmazonPluginsBase)
Provides:	perl(GCPlugins::GCfilms::GCfilmsPluginsBase)
Provides:	perl(GCPlugins::GCgames::GCgamesAmazonPluginsBase)
Provides:	perl(GCPlugins::GCgames::GCgamesPluginsBase)
Provides:	perl(GCPlugins::GCmusics::GCmusicsPluginsBase)
Provides:	perl(GCItemsLists::GCImageLists)
Provides:	perl(GCItemsLists::GCTextLists)
Provides:	perl(Gtk2::Dialog)
Provides:	perl(Gtk2::MenuBar)
Provides:	perl(Gtk2::MessageDialog)
Provides:	perl(Gtk2::ScrolledWindow)
Provides:	perl(Gtk2::Toolbar)
Provides:	perl(Gtk2::TreeView)
Provides:	perl(Gtk2::VBox)
Provides:	perl(Gtk2::Window)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
# %{_libdir}/%{name}
# %dir %{_libdir}/%{name}
# %dir %{_libdir}/%{name}/GCPlugins
# %{_libdir}/%{name}/GCBackend
# %{_libdir}/%{name}/GCItemsLists
# %{_libdir}/%{name}/GCPlugins/GCPluginsBase.pm
# %{_libdir}/%{name}/*.pm
# %{_libdir}/%{name}/GCExport
# %{_libdir}/%{name}/GCExtract
%{_datadir}/%{name}/*
%{_mandir}/man1/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
