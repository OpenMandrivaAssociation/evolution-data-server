%define api		1.2
%define base_version	3.0
%define dir_version	3.4

%define oldmajor	6
%define oldlibname %mklibname %{name} %{oldmajor}

%define oldmajor2006 4
%define oldlibname2006 %mklibname %{name} %{oldmajor2006}

%define camelmajor 33
%define camel_libname %mklibname camel %{camelmajor}
%define camel_devel %mklibname camel -d

%define ebackendmajor 2
%define ebackend_libname %mklibname ebackend %{ebackendmajor}
%define ebackend_devel %mklibname ebackend -d

%define ebookmajor 13
%define ebook_libname %mklibname ebook %{ebookmajor}
%define ebook_devel %mklibname ebook -d

%define ecalmajor 11
%define ecal_libname %mklibname ecal %{ecalmajor}
%define ecal_devel %mklibname ecal -d

%define edatabookmajor 13
%define edatabook_libname %mklibname edata-book %{edatabookmajor}
%define edatabook_devel %mklibname edata-book -d

%define edatacalmajor 15
%define edatacal_libname %mklibname edata-cal %{edatacalmajor}
%define edatacal_devel %mklibname edata-cal -d

%define edataservermajor 16
%define edataserver_libname %mklibname edataserver %{edataservermajor}
%define edataserver_devel %mklibname -d edataserver

%define edataserveruimajor 1
%define edataserverui_libname %mklibname edataserverui %{edataserveruimajor}
%define edataserverui_devel %mklibname edataserverui -d

%define girmajor 1.2
%define girname %mklibname %{name}-gir %{girmajor}

Name:		evolution-data-server
Summary:	Evolution Data Server
Version:	3.4.2
Release:	1
License: 	LGPLv2+
Group:		System/Libraries
URL: 		http://www.gnome.org/projects/evolution/
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

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
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(gconf-2.0) >= 2.0.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.0.0
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.31.2
BuildRequires:	pkgconfig(libgdata) >= 0.7.0
BuildRequires:	pkgconfig(goa-1.0) >= 3.1.1
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gnome-keyring-1) >= 2.20.1
BuildRequires:	pkgconfig(nspr)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(gweather-3.0) >= 2.90.0
BuildRequires:	pkgconfig(sqlite3) >= 3.5
BuildRequires:	pkgconfig(libical) >= 0.43
BuildRequires:	pkgconfig(oauth) >= 0.9.4

Obsoletes: %oldlibname

%description
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{camel_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes: %oldlibname2006

%description -n %{camel_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ebackend_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries

%description -n %{ebackend_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ebook_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries

%description -n %{ebook_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ecal_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries

%description -n %{ecal_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edatabook_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes: %oldlibname2006

%description -n %{edatabook_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edatacal_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes: %oldlibname2006

%description -n %{edatacal_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserver_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes: %oldlibname2006

%description -n %{edataserver_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserverui_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Obsoletes: %{_lib}edataserverui4

%description -n %{edataserverui_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{camel_devel}
Summary:	Libraries and include files for using Evolution Data Server - camel
Group:		Development/GNOME and GTK+
Requires:	%{camel_libname} = %{version}-%{release}

%description -n %{camel_devel}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ebackend_devel}
Summary:	Libraries and include files for using Evolution Data Server - ebackend
Group:		Development/GNOME and GTK+
Requires:	%{ebackend_libname} = %{version}-%{release}

%description -n %{ebackend_devel}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ebook_devel}
Summary:	Libraries and include files for using Evolution Data Server - ebook
Group:		Development/GNOME and GTK+
Requires:	%{ebook_libname} = %{version}-%{release}

%description -n %{ebook_devel}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ecal_devel}
Summary:	Libraries and include files for using Evolution Data Server - ecal
Group:		Development/GNOME and GTK+
Requires:	%{ecal_libname} = %{version}-%{release}

%description -n %{ecal_devel}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edatabook_devel}
Summary:	Libraries and include files for using Evolution Data Server - edatabook
Group:		Development/GNOME and GTK+
Requires:	%{edatabook_libname} = %{version}-%{release}

%description -n %{edatabook_devel}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edatacal_devel}
Summary:	Libraries and include files for using Evolution Data Server - edatacal
Group:		Development/GNOME and GTK+
Requires:	%{edatacal_libname} = %{version}-%{release}

%description -n %{edatacal_devel}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserver_devel}
Summary:	Libraries and include files for using Evolution Data Server
Group:		Development/GNOME and GTK+
Requires:	%{edataserver_libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d edataserver 9

%description -n %{edataserver_devel}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserverui_devel}
Summary:	Libraries and include files for using Evolution Data Server - edatserverui
Group:		Development/GNOME and GTK+
Requires:	%{edataserverui_libname} = %{version}-%{release}

%description -n %{edataserverui_devel}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%setup -q

%build

%configure2_5x --with-krb5=%{_prefix} --with-krb5-libs=%{_libdir} \
--with-libdb=%{_prefix} --disable-static \
--with-openldap=yes --with-static-ldap=no --enable-gtk-doc=yes 
#--enable-gnome-keyring=yes
%make

%install
%makeinstall_std

# remove libtool archives for importers and the like
find %{buildroot}/%{_libdir} -name '*.la' -exec rm {} \;

# give the libraries some executable bits 
find %{buildroot} -name '*.so.*' -exec chmod +x {} \;

%find_lang %{name}-%{dir_version}

%files -f %{name}-%{dir_version}.lang
%doc COPYING NEWS
%{_libexecdir}/%{name}
%{_libexecdir}/camel-index-control-%{api}
%{_libexecdir}/evolution-addressbook-factory
%{_libexecdir}/evolution-calendar-factory
%attr(2755,root,mail) %{_libexecdir}/camel-lock-helper-%{api}
%{_datadir}/%{name}-%{dir_version}
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.AddressBook.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.Calendar.service
%{_datadir}/pixmaps/%{name}

#GSettings
%{_datadir}/GConf/gsettings/libedataserver.convert
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.eds-shell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.shell.network-config.gschema.xml

%files -n %{camel_libname}
%{_libdir}/libcamel-%{api}.so.%{camelmajor}*

%files -n %{ebackend_libname}
%{_libdir}/libebackend-%{api}.so.%{ebackendmajor}*

%files -n %{ebook_libname}
%{_libdir}/libebook-%{api}.so.%{ebookmajor}*

%files -n %{ecal_libname}
%{_libdir}/libecal-%{api}.so.%{ecalmajor}*

%files -n %{edatabook_libname}
%{_libdir}/libedata-book-%{api}.so.%{edatabookmajor}*

%files -n %{edatacal_libname}
%{_libdir}/libedata-cal-%{api}.so.%{edatacalmajor}*

%files -n %{edataserver_libname}
%{_libdir}/libedataserver-%{api}.so.%{edataservermajor}*

%files -n %{edataserverui_libname}
%{_libdir}/libedataserverui-%{base_version}.so.%{edataserveruimajor}*

%files -n %{girname}
%{_libdir}/girepository-1.0/EDataServer-%{girmajor}.typelib
%{_libdir}/girepository-1.0/ECalendar-%{girmajor}.typelib
%{_libdir}/girepository-1.0/EBook-%{girmajor}.typelib

%files -n %{camel_devel}
%doc %{_datadir}/gtk-doc/html/camel/*
%{_includedir}/%{name}-%{dir_version}/camel
%{_libdir}/pkgconfig/camel-%{api}.pc
##{_libdir}/pkgconfig/camel-provider-%{api}.pc
%{_libdir}/libcamel-%{api}.so
##{_libdir}/libcamel-provider-%{api}.so

%files -n %{ebackend_devel}
%doc %{_datadir}/gtk-doc/html/libebackend/*
%{_includedir}/%{name}-%{dir_version}/libebackend
%{_libdir}/pkgconfig/libebackend-%{api}.pc
%{_libdir}/libebackend-%{api}.so

%files -n %{ebook_devel}
%doc %{_datadir}/gtk-doc/html/libebook/*
%{_includedir}/%{name}-%{dir_version}/libebook/
%{_libdir}/pkgconfig/libebook-%{api}.pc
%{_libdir}/libebook-%{api}.so

%files -n %{ecal_devel}
%doc %{_datadir}/gtk-doc/html/libecal/*
%{_includedir}/%{name}-%{dir_version}/libecal/
%{_libdir}/pkgconfig/libecal-%{api}.pc
%{_libdir}/libecal-%{api}.so
%{_datadir}/gir-1.0/ECalendar-%{girmajor}.gir

%files -n %{edatabook_devel}
%doc %{_datadir}/gtk-doc/html/libedata-book/*
%{_includedir}/%{name}-%{dir_version}/libedata-book/
%{_libdir}/pkgconfig/libedata-book-%{api}.pc
%{_libdir}/libedata-book-%{api}.so
%{_datadir}/gir-1.0/EBook-%{girmajor}.gir

%files -n %{edatacal_devel}
%doc %{_datadir}/gtk-doc/html/libedata-cal/*
%{_includedir}/%{name}-%{dir_version}/libedata-cal/
%{_libdir}/pkgconfig/libedata-cal-%{api}.pc
%{_libdir}/libedata-cal-%{api}.so

%files -n %{edataserver_devel}
%doc %{_datadir}/gtk-doc/html/libedataserver/*
%{_includedir}/%{name}-%{dir_version}/libedataserver/
%{_libdir}/pkgconfig/libedataserver-%{api}.pc
%{_libdir}/pkgconfig/evolution-data-server-%{api}.pc
%{_libdir}/libedataserver-%{api}.so
%{_datadir}/gir-1.0/EDataServer-%{girmajor}.gir

%files -n %{edataserverui_devel}
%doc %{_datadir}/gtk-doc/html/libedataserverui/*
%{_includedir}/%{name}-%{dir_version}/libedataserverui/
#{_libdir}/pkgconfig/libedataserverui-%{api}.pc
%{_libdir}/pkgconfig/libedataserverui-*.pc
#{_libdir}/libedataserverui-%{api}.so
%{_libdir}/libedataserverui-*.so

