%define api_version 1.2
%define ui_api_version 3.0
%define ecal_api 2.0
%define edata_api 2.0
%define dir_version %(echo %{version} | awk -F. '{print $1"."$2 + $2 % 2}')

%define camelmajor 62
%define camel_libname %mklibname camel %{api_version} %{camelmajor}

%define ebookmajor 20
%define ebook_libname %mklibname ebook %{api_version} %{ebookmajor}

%define ecalmajor 1
%define ecal_libname %mklibname ecal %{ecal_api} %{ecalmajor}

%define edatabookmajor 26
%define edatabook_libname %mklibname edata-book %{api_version} %{edatabookmajor}

%define ebook_contactsmajor 3
%define ebook_contacts_libname %mklibname ebook-contacts %{api_version} %{ebook_contactsmajor}

%define edatacalmajor 1
%define edatacal_libname %mklibname edata-cal %{api_version} %{edatacalmajor}

%define edataservermajor 26
%define edataserver_libname %mklibname edataserver %{api_version} %{edataservermajor}
%define edataserver_libnamedev %mklibname -d edataserver %{api_version}

%define edataserveruimajor 3
%define edataserverui_libname %mklibname edataserverui %{api_version} %{edataserveruimajor}

%define ebackendmajor 10
%define ebackend_libname %mklibname ebackend %{api_version} %{ebackendmajor}

%define gi_major 1.2
%define girname %mklibname %{name}-gir %{gi_major}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define _disable_rebuild_configure 1
%define __noautoreq '^devel\\(libedbus-private'
# allow private lib path to remain
%define _cmake_skip_rpath %nil

Name:		evolution-data-server
Summary:	Evolution Data Server
Version:	3.42.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
URL:		http://www.gnome.org/projects/evolution/
BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	db-devel
BuildRequires:	gettext
BuildRequires:	gnome-common
BuildRequires:	gperf
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig(krb5)
BuildRequires:	pkgconfig(gio-2.0) >= 2.30
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.2
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.30
BuildRequires:	pkgconfig(libical-glib)
BuildRequires:	pkgconfig(libxml-2.0) >= 2.0.0
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.31.2
BuildRequires:	pkgconfig(libgdata) >= 0.10.0
BuildRequires:	pkgconfig(goa-1.0) >= 3.1.1
BuildRequires:	pkgconfig(nspr)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(gweather-3.0) >= 2.90.0
BuildRequires:	pkgconfig(sqlite3) >= 3.5
BuildRequires:	pkgconfig(libical) >= 2.0
BuildRequires:	pkgconfig(oauth) >= 0.9.4
BuildRequires:	pkgconfig(gcr-base-3)
BuildRequires:	pkgconfig(libsecret-unstable)
BuildRequires:	pkgconfig(libaccounts-glib)
BuildRequires:	pkgconfig(libsignon-glib)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:	vala-tools
BuildRequires:  gobject-introspection-devel
BuildRequires:	pkgconfig(webkit2gtk-4.0)
BuildRequires:	pkgconfig(ss)

%description
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{camel_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
# (cg) Obsolete old non-conformant libname
Obsoletes:	%{mklibname camel 38}

%description -n %{camel_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ebook_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
# (cg) Obsolete old non-conformant libname
Obsoletes:	%{mklibname ebook 14}

%description -n %{ebook_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ecal_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
# (cg) Obsolete old non-conformant libname
Obsoletes:	%{mklibname ecal 15}

%description -n %{ecal_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ebook_contacts_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n %{ebook_contacts_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edatabook_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
# (cg) Obsolete old non-conformant libname
Obsoletes:	%{mklibname edata-book 15}

%description -n %{edatabook_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edatacal_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
# (cg) Obsolete old non-conformant libname
Obsoletes:	%{mklibname edata-cal 18}

%description -n %{edatacal_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserver_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
# (cg) Obsolete old non-conformant libname
Obsoletes:	%{mklibname edataserver 17}
Requires:	gsettings-desktop-schemas

%description -n %{edataserver_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserverui_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n %{edataserverui_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ebackend_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
# (cg) Obsolete old non-conformant libname
Obsoletes:	%{mklibname ebackend 4}

%description -n %{ebackend_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserver_libnamedev}
Summary:	Libraries and include files for using Evolution Data Server
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}
Requires: %camel_libname = %version
Requires: %ebook_libname = %version
Requires: %ecal_libname = %version
Requires: %edatabook_libname = %version
Requires: %edatacal_libname = %version
Requires: %edataserver_libname = %version
Requires: %edataserverui_libname = %version
Requires: %ebackend_libname = %version
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libedataserver-devel = %version-%release
# (cg) Obsolete old non-conformant devel name
Obsoletes:	%{mklibname -d edataserver}

%description -n %{edataserver_libnamedev}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{girname}
Summary:        GObject Introspection interface description for %name
Group:          System/Libraries

%description -n %{girname}
GObject Introspection interface description for %name.

%prep
%setup -q

%build
%cmake -DENABLE_VALA_BINDINGS=1 -DENABLE_INTROSPECTION=ON -DENABLE_UOA=OFF -DWITH_LIBDB=%{_prefix} \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
	-DLIB_INSTALL_DIR:PATH=%{_libdir} 
%make_build

%install
%make_install -C build

# remove libtool archives for importers and the like
find $RPM_BUILD_ROOT/%{_libdir} -name '*.la' -delete

# give the libraries some executable bits
find $RPM_BUILD_ROOT -name '*.so.*' -exec chmod +x {} \;

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING NEWS
%{_libdir}/%{name}/
%{_libexecdir}/camel-gpg-photo-saver
%{_libexecdir}/camel-index-control-%{api_version}
%{_libexecdir}/evolution-addressbook-factory
%{_libexecdir}/evolution-calendar-factory
%{_libexecdir}/evolution-addressbook-factory-subprocess
%{_libexecdir}/evolution-calendar-factory-subprocess
%{_libexecdir}/evolution-source-registry
%{_libexecdir}/evolution-user-prompter
%{_libexecdir}/evolution-scan-gconf-tree-xml
%{_libexecdir}/evolution-data-server
%{_prefix}/lib/systemd/user
%{_sysconfdir}/xdg/autostart/org.gnome.Evolution-alarm-notify.desktop
%{_datadir}/applications/org.gnome.Evolution-alarm-notify.desktop

%attr(2755,root,mail) %{_libexecdir}/camel-lock-helper-%{api_version}
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.AddressBook*.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.Calendar*.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.Sources*.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.UserPrompter*.service
%{_datadir}/GConf/gsettings/*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/pixmaps/%{name}

%files -n %{camel_libname}
%{_libdir}/libcamel-%{api_version}.so.%{camelmajor}*

%files -n %{ebook_libname}
%{_libdir}/libebook-%{api_version}.so.%{ebookmajor}*

%files -n %{ecal_libname}
%{_libdir}/libecal-%{ecal_api}.so.%{ecalmajor}*

%files -n %{ebook_contacts_libname}
%{_libdir}/libebook-contacts-%{api_version}.so.%{ebook_contactsmajor}*

%files -n %{edatabook_libname}
%{_libdir}/libedata-book-%{api_version}.so.%{edatabookmajor}*

%files -n %{edatacal_libname}
%{_libdir}/libedata-cal-%{edata_api}.so.%{edatacalmajor}*

%files -n %{edataserver_libname}
%{_libdir}/libedataserver-%{api_version}.so.%{edataservermajor}*

%files -n %{edataserverui_libname}
%{_libdir}/libedataserverui-%{api_version}.so.%{edataserveruimajor}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Camel-%{gi_major}.typelib
%{_libdir}/girepository-1.0/EDataServer-%{gi_major}.typelib
%{_libdir}/girepository-1.0/EDataServerUI-%{gi_major}.typelib
%{_libdir}/girepository-1.0/EBook-%{gi_major}.typelib
%{_libdir}/girepository-1.0/EBookContacts-%{gi_major}.typelib
%{_libdir}/girepository-1.0/EBackend-1.2.typelib
%{_libdir}/girepository-1.0/ECal-2.0.typelib
%{_libdir}/girepository-1.0/EDataBook-1.2.typelib
%{_libdir}/girepository-1.0/EDataCal-2.0.typelib

%files -n %{ebackend_libname}
%{_libdir}/libebackend-%{api_version}.so.%{ebackendmajor}*

%files -n %{edataserver_libnamedev}
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/Camel-%{gi_major}.gir
%{_datadir}/gir-1.0/EBackend-1.2.gir
%{_datadir}/gir-1.0/EDataServer-%{gi_major}.gir
%{_datadir}/gir-1.0/EDataServerUI-%{gi_major}.gir
%{_datadir}/gir-1.0/EBook-%{gi_major}.gir
%{_datadir}/gir-1.0/EBookContacts-%{gi_major}.gir
%{_datadir}/gir-1.0/ECal-2.0.gir
%{_datadir}/gir-1.0/EDataBook-1.2.gir
%{_datadir}/gir-1.0/EDataCal-2.0.gir
%{_datadir}/vala/vapi/camel-1.2.deps
%{_datadir}/vala/vapi/camel-1.2.vapi
%{_datadir}/vala/vapi/libebackend-%{gi_major}.deps
%{_datadir}/vala/vapi/libebackend-%{gi_major}.vapi
%{_datadir}/vala/vapi/libebook-1.2.deps
%{_datadir}/vala/vapi/libebook-1.2.vapi
%{_datadir}/vala/vapi/libebook-contacts-1.2.deps
%{_datadir}/vala/vapi/libebook-contacts-1.2.vapi
%{_datadir}/vala/vapi/libecal-2.0.deps
%{_datadir}/vala/vapi/libecal-2.0.vapi
%{_datadir}/vala/vapi/libedata-book-%{gi_major}.deps
%{_datadir}/vala/vapi/libedata-book-%{gi_major}.vapi
%{_datadir}/vala/vapi/libedata-cal-2.0.deps
%{_datadir}/vala/vapi/libedata-cal-2.0.vapi
%{_datadir}/vala/vapi/libedataserver-1.2.deps
%{_datadir}/vala/vapi/libedataserver-1.2.vapi
%{_datadir}/vala/vapi/libedataserverui-1.2.deps
%{_datadir}/vala/vapi/libedataserverui-1.2.vapi
