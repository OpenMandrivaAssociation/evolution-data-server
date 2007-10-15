%define libsoup_version_required 2.2.3
%define api_version 1.2
%define base_version 1.12
%define lib_major 6
%define lib_name %mklibname %{name} %{lib_major}
%define firefox_version 1.0.1

%define oldmajor 6
%define oldlibname %mklibname %name %oldmajor

%define oldmajor2006 4
%define oldlibname2006 %mklibname %name %oldmajor2006

%define camelmajor 10
%define camel_libname %mklibname camel %camelmajor

%define camelprovidermajor 10
%define camelprovider_libname %mklibname camel-provider %camelprovidermajor

%define ebookmajor 9
%define ebook_libname %mklibname ebook %ebookmajor

%define ecalmajor 7
%define ecal_libname %mklibname ecal %ecalmajor

%define edatabookmajor 2
%define edatabook_libname %mklibname edata-book %edatabookmajor

%define edatacalmajor 6
%define edatacal_libname %mklibname edata-cal %edatacalmajor

%define edataservermajor 9
%define edataserver_libname %mklibname edataserver %edataservermajor
%define edataserver_libnamedev %mklibname -d edataserver

%define edataserveruimajor 8
%define edataserverui_libname %mklibname edataserverui %edataserveruimajor

%define egroupwisemajor 13
%define egroupwise_libname %mklibname egroupwise %egroupwisemajor

%define exchangemajor 3
%define exchange_libname %mklibname exchange-storage %exchangemajor

Name:		evolution-data-server
Summary:	Evolution Data Server
Version: 1.12.1
Release: %mkrel 1
License: 	GPL
Group:		System/Libraries
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (pt) 1.10.0-3mdv fix empty error dialog in non utf8 locale
Patch1:		evolution-data-server-1.11.1-gpgutf8.patch

URL: 		http://www.gnome.org/projects/evolution/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

BuildRequires: bison flex
BuildRequires: gtk-doc
BuildRequires: krb5-devel
BuildRequires: libglade2.0-devel
BuildRequires: libgnomeui2-devel
BuildRequires: libsoup-devel >= %{libsoup_version_required}
BuildRequires: nss-devel >= %{firefox_version}
BuildRequires: nspr-devel >= %{firefox_version}
BuildRequires: openldap-devel 
BuildRequires: perl-XML-Parser
BuildRequires: db4-devel

Obsoletes: %oldlibname


%description
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{camel_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
Obsoletes: %oldlibname2006

%description -n %{camel_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{camelprovider_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n %{camelprovider_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ebook_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n %{ebook_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ecal_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n %{ecal_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edatabook_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
Obsoletes: %oldlibname2006

%description -n %{edatabook_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edatacal_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
Obsoletes: %oldlibname2006

%description -n %{edatacal_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserver_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
Obsoletes: %oldlibname2006

%description -n %{edataserver_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserverui_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
Obsoletes: %{_lib}edataserverui4

%description -n %{edataserverui_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{egroupwise_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n %{egroupwise_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{exchange_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n %{exchange_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{edataserver_libnamedev}
Summary:	Libraries and include files for using Evolution Data Server
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}
Requires: %camel_libname = %version
Requires: %camelprovider_libname = %version
Requires: %ebook_libname = %version
Requires: %ecal_libname = %version
Requires: %edatabook_libname = %version
Requires: %edatacal_libname = %version
Requires: %edataserver_libname = %version
Requires: %edataserverui_libname = %version
Requires: %egroupwise_libname = %version
Requires: %exchange_libname = %version
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides: libedataserver-devel = %version-%release
Requires: nss-devel >= %{firefox_version}
Requires: nspr-devel >= %{firefox_version}
Obsoletes: %mklibname -d edataserver 9
%define _requires_exceptions nspr4\\|plc4\\|plds4\\|nss3\\|smime3\\|softokn3\\|ssl3

%description -n %{edataserver_libnamedev}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%prep
%setup -q
%patch1 -p1 -b .gpgutf8

%build

%configure2_5x --with-krb5=%{_prefix} --with-krb5-libs=%{_libdir} \
--without-krb4 --with-libdb=%{_prefix} \
--with-openldap=yes --with-static-ldap=no --enable-gtk-doc=yes 
#--enable-gnome-keyring=yes
%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall_std


%{find_lang} %{name}-%{base_version}

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post -n %camel_libname -p /sbin/ldconfig
%postun -n %camel_libname -p /sbin/ldconfig
%post -n %camelprovider_libname -p /sbin/ldconfig
%postun -n %camelprovider_libname -p /sbin/ldconfig
%post -n %ebook_libname -p /sbin/ldconfig
%postun -n %ebook_libname -p /sbin/ldconfig
%post -n %ecal_libname -p /sbin/ldconfig
%postun -n %ecal_libname -p /sbin/ldconfig
%post -n %edatabook_libname -p /sbin/ldconfig
%postun -n %edatabook_libname -p /sbin/ldconfig
%post -n %edatacal_libname -p /sbin/ldconfig
%postun -n %edatacal_libname -p /sbin/ldconfig
%post -n %edataserver_libname -p /sbin/ldconfig
%postun -n %edataserver_libname -p /sbin/ldconfig
%post -n %edataserverui_libname -p /sbin/ldconfig
%postun -n %edataserverui_libname -p /sbin/ldconfig
%post -n %egroupwise_libname -p /sbin/ldconfig
%postun -n %egroupwise_libname -p /sbin/ldconfig
%post -n %exchange_libname -p /sbin/ldconfig
%postun -n %exchange_libname -p /sbin/ldconfig

%files -f %{name}-%{base_version}.lang
%defattr(-, root, root)
%doc COPYING ChangeLog 
%{_libexecdir}/%{name}-%{base_version}
%{_libexecdir}/%{name}-%{api_version}
%{_libexecdir}/camel-index-control-%{api_version}
%attr(2755,root,mail) %{_libexecdir}/camel-lock-helper-%{api_version}
%{_libdir}/bonobo/servers/*
%{_datadir}/idl/%{name}-%{api_version}
%{_datadir}/%{name}-%{base_version}
%{_datadir}/pixmaps/%{name}

%files -n %{camel_libname}
%defattr(-, root, root)
%{_libdir}/libcamel-%{api_version}.so.%{camelmajor}*

%files -n %{camelprovider_libname}
%defattr(-, root, root)
%{_libdir}/libcamel-provider*.so.%{camelprovidermajor}*

%files -n %{ebook_libname}
%defattr(-, root, root)
%{_libdir}/libebook*.so.%{ebookmajor}*

%files -n %{ecal_libname}
%defattr(-, root, root)
%{_libdir}/libecal*.so.%{ecalmajor}*

%files -n %{edatabook_libname}
%defattr(-, root, root)
%{_libdir}/libedata-book*.so.%{edatabookmajor}*

%files -n %{edatacal_libname}
%defattr(-, root, root)
%{_libdir}/libedata-cal*.so.%{edatacalmajor}*

%files -n %{edataserver_libname}
%defattr(-, root, root)
%{_libdir}/libedataserver-*.so.%{edataservermajor}*

%files -n %{edataserverui_libname}
%defattr(-, root, root)
%{_libdir}/libedataserverui-*.so.%{edataserveruimajor}*

%files -n %{egroupwise_libname}
%defattr(-, root, root)
%{_libdir}/libegroupwise-*.so.%{egroupwisemajor}*

%files -n %{exchange_libname}
%defattr(-, root, root)
%{_libdir}/libexchange-storage-*.so.%{exchangemajor}*

%files -n %{edataserver_libnamedev}
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/%{name}-%{base_version}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
