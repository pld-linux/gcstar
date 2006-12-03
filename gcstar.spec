%include        /usr/lib/rpm/macros.perl
Summary:	GCstar: collection manager
Name:		gcstar
Version:	0.5.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://download.gna.org/gcstar/%{name}-%{version}.tar.gz
# Source0-md5:	12ba75fe2f3091c1ccd03864424a34e2
Patch0:		%{name}-mandir.patch
Patch1:		%{name}-desktop.patch
BuildRequires:	perl-Gtk2
BuildRequires:	perl-libwww
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GCstar is a free application for managing your collections.

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
