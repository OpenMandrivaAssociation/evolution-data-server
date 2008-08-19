%define nspr_major 4
%define nss_major 3

%define _requires_exceptions nspr%{nspr_major}\\|plc%{nspr_major}\\|plds%{nspr_major}\\|nss%{nss_major}\\|smime%{nss_major}\\|softokn%{nss_major}\\|ssl%{nss_major}\\|nssutil%{nss_major}

%define version 2.23.90.1
%define libsoup_version_required 2.3.0
%define api_version 1.2
%define base_version 2.24
%define lib_major 6
%define lib_name %mklibname %{name} %{lib_major}
%define firefox_version 1.0.1

%define oldmajor 6
%define oldlibname %mklibname %name %oldmajor

%define oldmajor2006 4
%define oldlibname2006 %mklibname %name %oldmajor2006

%define camelmajor 13
%define camel_libname %mklibname camel %camelmajor

%define ebookmajor 9
%define ebook_libname %mklibname ebook %ebookmajor

%define ecalmajor 7
%define ecal_libname %mklibname ecal %ecalmajor

%define edatabookmajor 2
%define edatabook_libname %mklibname edata-book %edatabookmajor

%define edatacalmajor 6
%define edatacal_libname %mklibname edata-cal %edatacalmajor

%define edataservermajor 11
%define edataserver_libname %mklibname edataserver %edataservermajor
%define edataserver_libnamedev %mklibname -d edataserver

%define edataserveruimajor 8
%define edataserverui_libname %mklibname edataserverui %edataserveruimajor

%define egroupwisemajor 13
%define egroupwise_libname %mklibname egroupwise %egroupwisemajor

%define exchangemajor 3
%define exchange_libname %mklibname exchange-storage %exchangemajor

%define gdatamajor 1
%define gdata_libname %mklibname gdata %gdatamajor

%define ebackendmajor 0
%define ebackend_libname %mklibname ebackend %ebackendmajor

# disable under and over linking check, Makefile.am patch isn't enough

%define _disable_ld_as_needed 1
%define _disable_ld_no_undefined 1

Name:		evolution-data-server
Summary:	Evolution Data Server
Version: %version
Release: %mkrel 1
License: 	LGPLv2
Group:		System/Libraries
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# fix underlinking (not working for now)
Patch0: evolution-data-server-2.22.2-fix-linking.patch
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
BuildRequires: sqlite3-devel >= 3.5
BuildRequires: intltool
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

%package -n %{gdata_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n %{gdata_libname}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%package -n %{ebackend_libname}
Summary:	Shared libraries for using Evolution Data Server
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

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
Requires: %egroupwise_libname = %version
Requires: %exchange_libname = %version
Requires: %gdata_libname = %version
Requires: %ebackend_libname = %version
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides: libedataserver-devel = %version-%release
Requires: nss-devel >= %{firefox_version}
Requires: nspr-devel >= %{firefox_version}
Obsoletes: %mklibname -d edataserver 9

%description -n %{edataserver_libnamedev}
Evolution Data Server provides a central location for your addressbook
and calendar in the gnome desktop.

%prep
%setup -q
#%patch0 -p1 -b .fixlinking

#needed by patch0
#automake

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

%if %mdkversion < 200900
%post -n %camel_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %camel_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %ebook_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %ebook_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %ecal_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %ecal_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %edatabook_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %edatabook_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %edatacal_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %edatacal_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %edataserver_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %edataserver_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %edataserverui_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %edataserverui_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %egroupwise_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %egroupwise_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %exchange_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %exchange_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %gdata_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %gdata_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %ebackend_libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %ebackend_libname -p /sbin/ldconfig
%endif


%files -f %{name}-%{base_version}.lang
%defattr(-, root, root)
%doc COPYING NEWS
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
%{_libdir}/libcamel-provider-%{api_version}.so.%{camelmajor}*

%files -n %{ebook_libname}
%defattr(-, root, root)
%{_libdir}/libebook-%{api_version}.so.%{ebookmajor}*

%files -n %{ecal_libname}
%defattr(-, root, root)
%{_libdir}/libecal-%{api_version}.so.%{ecalmajor}*

%files -n %{edatabook_libname}
%defattr(-, root, root)
%{_libdir}/libedata-book-%{api_version}.so.%{edatabookmajor}*

%files -n %{edatacal_libname}
%defattr(-, root, root)
%{_libdir}/libedata-cal-%{api_version}.so.%{edatacalmajor}*

%files -n %{edataserver_libname}
%defattr(-, root, root)
%{_libdir}/libedataserver-%{api_version}.so.%{edataservermajor}*

%files -n %{edataserverui_libname}
%defattr(-, root, root)
%{_libdir}/libedataserverui-%{api_version}.so.%{edataserveruimajor}*

%files -n %{egroupwise_libname}
%defattr(-, root, root)
%{_libdir}/libegroupwise-%{api_version}.so.%{egroupwisemajor}*

%files -n %{exchange_libname}
%defattr(-, root, root)
%{_libdir}/libexchange-storage-%{api_version}.so.%{exchangemajor}*

%files -n %{gdata_libname}
%defattr(-, root, root)
%{_libdir}/libgdata-%{api_version}.so.%{gdatamajor}*
%{_libdir}/libgdata-google-%{api_version}.so.%{gdatamajor}*

%files -n %{ebackend_libname}
%defattr(-, root, root)
%{_libdir}/libebackend-%{api_version}.so.%{ebackendmajor}*

%files -n %{edataserver_libnamedev}
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/%{name}-%{base_version}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
