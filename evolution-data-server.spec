%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.2
%define uiapi	3.0

%define camelmajor 40
%define libcamel %mklibname camel %{api} %{camelmajor}
%define devcamel %mklibname camel -d

%define ebackendmajor 5
%define libebackend %mklibname ebackend %{api} %{ebackendmajor}
%define devebackend %mklibname ebackend -d

%define ebookmajor 14
%define libebook %mklibname ebook %{api} %{ebookmajor}
%define devebook %mklibname ebook -d

%define ecalmajor 15
%define libecal %mklibname ecal %{api} %{ecalmajor}
%define devecal %mklibname ecal -d

%define edatabookmajor 15
%define libedatabook %mklibname edata-book %{api} %{edatabookmajor}
%define devedatabook %mklibname edata-book -d

%define edatacalmajor 18
%define libedatacal %mklibname edata-cal %{api} %{edatacalmajor}
%define devedatacal %mklibname edata-cal -d

%define edataservermajor 17
%define libedataserver %mklibname edataserver %{api} %{edataservermajor}
%define devedataserver %mklibname -d edataserver

%define edataserveruimajor 4
%define libedataserverui %mklibname edataserverui %{uiapi} %{edataserveruimajor}
%define devedataserverui %mklibname edataserverui -d

%define girname		%mklibname edataserver-gir %{api}
%define	girecalendar	%mklibname ecalendar-gir %{api}
%define	girebook	%mklibname ebook-gir %{api}

Summary:	Evolution Data Server
Name:		evolution-data-server
Version:	3.8.1
Release:	1
License: 	LGPLv2+
Group:		System/Libraries
Url: 		http://www.gnome.org/projects/evolution/
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/evolution-data-server/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	gettext
BuildRequires:	gnome-common
BuildRequires:	gperf
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	openldap-devel
BuildRequires:	krb5-devel
BuildRequires:	pkgconfig(gio-2.0) >= 2.28
BuildRequires:	pkgconfig(gconf-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gcr-base-3) >= 3.4
BuildRequires:	pkgconfig(goa-1.0) >= 3.1.1
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gnome-keyring-1) >= 2.20.1
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(gweather-3.0) >= 2.90.0
BuildRequires:	pkgconfig(libgdata) >= 0.7.0
BuildRequires:	pkgconfig(libical) >= 0.43
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.31.2
BuildRequires:	pkgconfig(libxml-2.0) >= 2.0.0
BuildRequires:	pkgconfig(nspr)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(oauth) >= 0.9.4
BuildRequires:	pkgconfig(sqlite3) >= 3.5
BuildRequires:	pkgconfig(libaccounts-glib)

%description
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{libcamel}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{_lib}camel40 < 3.6.4-2

%description -n %{libcamel}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{libebackend}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{_lib}ebackend5 < 3.6.4-2

%description -n %{libebackend}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{libebook}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{_lib}ebook14 < 3.6.4-2

%description -n %{libebook}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{libecal}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{_lib}ecal15 < 3.6.4-2

%description -n %{libecal}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{libedatabook}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{_lib}edata-book15 < 3.6.4-2

%description -n %{libedatabook}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{libedatacal}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{_lib}edata-cal18 < 3.6.4-2

%description -n %{libedatacal}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{libedataserver}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{_lib}edataserver17 < 3.6.4-2

%description -n %{libedataserver}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{libedataserverui}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes:	%{_lib}edataserverui4 < 3.6.4-2

%description -n %{libedataserverui}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{devcamel}
Summary:	Libraries and include files for using Evolution Data Server - camel
Group:		Development/GNOME and GTK+
Requires:	%{libcamel} = %{version}-%{release}

%description -n %{devcamel}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{devebackend}
Summary:	Libraries and include files for using Evolution Data Server - ebackend
Group:		Development/GNOME and GTK+
Requires:	%{libebackend} = %{version}-%{release}

%description -n %{devebackend}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{devebook}
Summary:	Libraries and include files for using Evolution Data Server - ebook
Group:		Development/GNOME and GTK+
Requires:	%{libebook} = %{version}-%{release}
Requires:	%{girebook} = %{version}-%{release}

%description -n %{devebook}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{devecal}
Summary:	Libraries and include files for using Evolution Data Server - ecal
Group:		Development/GNOME and GTK+
Requires:	%{libecal} = %{version}-%{release}

%description -n %{devecal}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{devedatabook}
Summary:	Libraries and include files for using Evolution Data Server - edatabook
Group:		Development/GNOME and GTK+
Requires:	%{libedatabook} = %{version}-%{release}

%description -n %{devedatabook}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{devedatacal}
Summary:	Libraries and include files for using Evolution Data Server - edatacal
Group:		Development/GNOME and GTK+
Requires:	%{libedatacal} = %{version}-%{release}
Requires:	%{girecalendar} = %{version}-%{release}

%description -n %{devedatacal}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{devedataserver}
Summary:	Libraries and include files for using Evolution Data Server
Group:		Development/GNOME and GTK+
Requires:	%{libedataserver} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devedataserver}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{devedataserverui}
Summary:	Libraries and include files for using Evolution Data Server - edatserverui
Group:		Development/GNOME and GTK+
Requires:	%{libedataserverui} = %{version}-%{release}

%description -n %{devedataserverui}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Obsoletes:	%{_lib}evolution-data-server-gir1.2 < 3.6.4-2

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{girecalendar}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Conflicts:	%{_lib}evolution-data-server-gir1.2 < 3.6.4-2

%description -n %{girecalendar}
GObject Introspection interface description for %{name}.

%package -n %{girebook}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Conflicts:	%{_lib}evolution-data-server-gir1.2 < 3.6.4-2

%description -n %{girebook}
GObject Introspection interface description for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--with-krb5=%{_prefix} \
	--with-krb5-libs=%{_libdir} \
	--with-libdb=%{_prefix}	\
	--disable-static \
	--with-openldap=yes \
	--with-static-ldap=no \
	--enable-gtk-doc=yes 

%make

%install
%makeinstall_std

# remove libtool archives for importers and the like
find %{buildroot}/%{_libdir} -name '*.la' -exec rm {} \;

# give the libraries some executable bits 
find %{buildroot} -name '*.so.*' -exec chmod +x {} \;

%find_lang %{name}-%{url_ver}

%files -f %{name}-%{url_ver}.lang
%doc COPYING NEWS
%{_libexecdir}/%{name}
%{_libexecdir}/camel-index-control-%{api}
%{_libexecdir}/evolution-addressbook-factory
%{_libexecdir}/evolution-calendar-factory

%{_libdir}/evolution-source-registry

%attr(2755,root,mail) %{_libexecdir}/camel-lock-helper-%{api}
%{_datadir}/%{name}-%{url_ver}
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.AddressBook.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.Calendar.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.Sources.service
%{_datadir}/pixmaps/%{name}
%{_datadir}/GConf/gsettings/evolution-data-server.convert

#GSettings
%{_datadir}/GConf/gsettings/libedataserver.convert
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.eds-shell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.shell.network-config.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Evolution.DefaultSources.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution-data-server.addressbook.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution-data-server.calendar.gschema.xml

%files -n %{libcamel}
%{_libdir}/libcamel-%{api}.so.%{camelmajor}*

%files -n %{libebackend}
%{_libdir}/libebackend-%{api}.so.%{ebackendmajor}*

%files -n %{libebook}
%{_libdir}/libebook-%{api}.so.%{ebookmajor}*

%files -n %{libecal}
%{_libdir}/libecal-%{api}.so.%{ecalmajor}*

%files -n %{libedatabook}
%{_libdir}/libedata-book-%{api}.so.%{edatabookmajor}*

%files -n %{libedatacal}
%{_libdir}/libedata-cal-%{api}.so.%{edatacalmajor}*

%files -n %{libedataserver}
%{_libdir}/libedataserver-%{api}.so.%{edataservermajor}*

%files -n %{libedataserverui}
%{_libdir}/libedataserverui-%{uiapi}.so.%{edataserveruimajor}*

%files -n %{girname}
%{_libdir}/girepository-1.0/EDataServer-%{api}.typelib

%files -n %{girecalendar}
%{_libdir}/girepository-1.0/ECalendar-%{api}.typelib

%files -n %{girebook}
%{_libdir}/girepository-1.0/EBook-%{api}.typelib

%files -n %{devcamel}
%doc %{_datadir}/gtk-doc/html/camel/*
%{_includedir}/%{name}-%{url_ver}/camel
%{_libdir}/pkgconfig/camel-%{api}.pc
%{_libdir}/libcamel-%{api}.so

%files -n %{devebackend}
%doc %{_datadir}/gtk-doc/html/libebackend/*
%{_includedir}/%{name}-%{url_ver}/libebackend
%{_libdir}/pkgconfig/libebackend-%{api}.pc
%{_libdir}/libebackend-%{api}.so

%files -n %{devebook}
%doc %{_datadir}/gtk-doc/html/libebook/*
%{_includedir}/%{name}-%{url_ver}/libebook/
%{_libdir}/pkgconfig/libebook-%{api}.pc
%{_libdir}/libebook-%{api}.so

%files -n %{devecal}
%doc %{_datadir}/gtk-doc/html/libecal/*
%{_includedir}/%{name}-%{url_ver}/libecal/
%{_libdir}/pkgconfig/libecal-%{api}.pc
%{_libdir}/libecal-%{api}.so
%{_datadir}/gir-1.0/ECalendar-%{api}.gir

%files -n %{devedatabook}
%doc %{_datadir}/gtk-doc/html/libedata-book/*
%{_includedir}/%{name}-%{url_ver}/libedata-book/
%{_libdir}/pkgconfig/libedata-book-%{api}.pc
%{_libdir}/libedata-book-%{api}.so
%{_datadir}/gir-1.0/EBook-%{api}.gir

%files -n %{devedatacal}
%doc %{_datadir}/gtk-doc/html/libedata-cal/*
%{_includedir}/%{name}-%{url_ver}/libedata-cal/
%{_libdir}/pkgconfig/libedata-cal-%{api}.pc
%{_libdir}/libedata-cal-%{api}.so

%files -n %{devedataserver}
%doc %{_datadir}/gtk-doc/html/libedataserver/*
%{_includedir}/%{name}-%{url_ver}/libedataserver/
%{_libdir}/pkgconfig/libedataserver-%{api}.pc
%{_libdir}/pkgconfig/evolution-data-server-%{api}.pc
%{_libdir}/libedataserver-%{api}.so
%{_datadir}/gir-1.0/EDataServer-%{api}.gir

%files -n %{devedataserverui}
%doc %{_datadir}/gtk-doc/html/libedataserverui/*
%{_includedir}/%{name}-%{url_ver}/libedataserverui/
%{_libdir}/pkgconfig/libedataserverui-%{uiapi}.pc
%{_libdir}/libedataserverui-%{uiapi}.so

