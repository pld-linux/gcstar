# NOTES:- warnings like this: /usr/lib/rpm/perl.prov: weird, cannot determine the package name for
#	 `/mnt/hda5/tmp/gcstar-0.5.0-root-inter/usr/lib/gcstar/GCLang/BG/GCstar.pm'
#	- wrong? perl modules location: /usr/lib/gcstar
#	- putting files in /usr/lib/ makes this package arch dependent
#
%include        /usr/lib/rpm/macros.perl
Summary:	GCstar: collection manager
Summary(pl):	GCstar: zarz±dca kolekcji
Name:		gcstar
Version:	1.0.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://download.gna.org/gcstar/%{name}-%{version}.tar.gz
# Source0-md5:	0bf2ce46a4adba23136e65ec6d2bd65d
Patch0:		%{name}-mandir.patch
Patch1:		%{name}-desktop.patch
URL:		https://gna.org/projects/gcstar/
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-Gtk2
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-libwww
Requires(post,postun):	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GCstar is an application to manage different kind of collections. It
is designed to be able to support as many type of collections as
needed. For the moment it supports these ones:
 - Movies
 - Video games
 - Books
 - User defined collections

%description -l pl
GCstar jest aplikacj± do zarz±dzania ró¿nymi rodzajami kolekcji. Jest
zaprojektowana by móc wspieraæ wszystkie potrzebne typy kolekcji.
Aktualnie wspiera kolekcje:
 - filmów
 - gier wideo
 - ksi±¿ek
 - kolekcje zdefiniowane przez u¿ytkownika

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build

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
%{_datadir}/%{name}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%{_mandir}/man1/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
