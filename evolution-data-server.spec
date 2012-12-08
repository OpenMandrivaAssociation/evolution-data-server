%define api		1.2
%define base_version	3.0
%define dir_version	3.6

%define oldmajor	6
%define oldlibname %mklibname %{name} %{oldmajor}

%define oldmajor2006 4
%define oldlibname2006 %mklibname %{name} %{oldmajor2006}

%define camelmajor 40
%define camel_libname %mklibname camel %{camelmajor}
%define camel_devel %mklibname camel -d

%define ebackendmajor 5
%define ebackend_libname %mklibname ebackend %{ebackendmajor}
%define ebackend_devel %mklibname ebackend -d

%define ebookmajor 14
%define ebook_libname %mklibname ebook %{ebookmajor}
%define ebook_devel %mklibname ebook -d

%define ecalmajor 15
%define ecal_libname %mklibname ecal %{ecalmajor}
%define ecal_devel %mklibname ecal -d

%define edatabookmajor 15
%define edatabook_libname %mklibname edata-book %{edatabookmajor}
%define edatabook_devel %mklibname edata-book -d

%define edatacalmajor 18
%define edatacal_libname %mklibname edata-cal %{edatacalmajor}
%define edatacal_devel %mklibname edata-cal -d

%define edataservermajor 17
%define edataserver_libname %mklibname edataserver %{edataservermajor}
%define edataserver_devel %mklibname -d edataserver

%define edataserveruimajor 4
%define edataserverui_libname %mklibname edataserverui %{edataserveruimajor}
%define edataserverui_devel %mklibname edataserverui -d

%define girmajor 1.2
%define girname %mklibname %{name}-gir %{girmajor}

Name:		evolution-data-server
Summary:	Evolution Data Server
Version:	3.6.2
Release:	1
License: 	LGPLv2+
Group:		System/Libraries
URL: 		http://www.gnome.org/projects/evolution/
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz

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
BuildRequires:  pkgconfig(gcr-base-3) >= 3.4

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
%configure2_5x \
	--with-krb5=%{_prefix} \
	--with-krb5-libs=%{_libdir} \
	--with-libdb=%{_prefix}	\
	--disable-static \
	--with-openldap=yes \
	--with-static-ldap=no \
	--enable-gtk-doc=yes 
#	--enable-gnome-keyring=yes

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

%{_libdir}/evolution-source-registry

%attr(2755,root,mail) %{_libexecdir}/camel-lock-helper-%{api}
%{_datadir}/%{name}-%{dir_version}
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

%changelog
* Tue Nov 13 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.2-1
- update to 3.6.2

* Fri Sep 28 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Mon Aug 13 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.4-1
+ Revision: 814436
- update to new version 3.4.4

* Tue Jun 19 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.3-1
+ Revision: 806153
- update to new version 3.4.3

* Wed May 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.2-1
+ Revision: 799174
- new version 3.4.2
- cleaned up spec

* Thu Apr 26 2012 Guilherme Moro <guilherme@mandriva.com> 3.4.1-0
+ Revision: 793645
- Updated to version 3.4.1

* Sun Nov 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 3.2.2-1
+ Revision: 733688
- fixed BR
- fixed files lists
- added missing BR
- new version 3.2.2
- syncd spec to mga (but greatly extended)
- each devel pkg split out
- gir pkg split out
- egroupwise pkg removed
- dep loop removed
- defattr removed
- clean section removed
- BRs converted to pkgconfig provides
- mkrel & BuildRoot removed

* Mon Oct 24 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.3-3
+ Revision: 705835
- rebuild for new libpng

* Mon Jun 20 2011 Oden Eriksson <oeriksson@mandriva.com> 2.32.3-2
+ Revision: 686310
- avoid pulling 32 bit libraries on 64 bit arch

* Fri Apr 22 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.3-1
+ Revision: 656660
- new version
- drop patch

* Sun Apr 10 2011 Funda Wang <fwang@mandriva.org> 2.32.2-3
+ Revision: 652410
- clean up BRs
- build with db 5.1

* Thu Apr 07 2011 Funda Wang <fwang@mandriva.org> 2.32.2-2
+ Revision: 651368
- fix build with gtk 2.24
- rebuild for update libsoup libtool archive

* Sun Feb 06 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.2-1
+ Revision: 636463
- update to new version 2.32.2

* Mon Nov 15 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.1-1mdv2011.0
+ Revision: 597725
- update to new version 2.32.1

* Tue Sep 28 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.0-3mdv2011.0
+ Revision: 581642
- update devel deps

* Tue Sep 28 2010 Funda Wang <fwang@mandriva.org> 2.32.0-2mdv2011.0
+ Revision: 581568
- now build correctly with our default link flags

* Mon Sep 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581343
- update to new version 2.32.0

* Mon Sep 13 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.92.1-1mdv2011.0
+ Revision: 578004
- update to new version 2.31.92.1

* Mon Sep 13 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 577917
- new version

* Mon Aug 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 574290
- new version
- new edataserverui major

* Mon Aug 16 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.90-1mdv2011.0
+ Revision: 570438
- update to new version 2.31.90

* Mon Aug 09 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.6-2mdv2011.0
+ Revision: 568202
- rebuild for new libproxy

* Tue Aug 03 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 565435
- new version
- new major
- new base version

* Fri Jul 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.5-1mdv2011.0
+ Revision: 563362
- new version
- new major
- depend on external libgdata

* Mon Jun 21 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.2.1-1mdv2010.1
+ Revision: 548431
- Release 2.30.2.1
- Remove patch1 (merged upstream)

* Mon Jun 21 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.2-2mdv2010.1
+ Revision: 548418
- Patch0 (GIT): revert invalid fix (GNOME bug #619347)

* Mon Jun 21 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.2-1mdv2010.1
+ Revision: 548396
- Release 2.30.2
- Remove patch1 (merged upstream)

* Tue May 25 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.1-5mdv2010.1
+ Revision: 545937
- Update patch1 with many fixes from upstream GIT

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 2.30.1-4mdv2010.1
+ Revision: 540334
- rebuild so that shared libraries are properly stripped again

* Tue Apr 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.1-3mdv2010.1
+ Revision: 539829
- rebuild for lost package

  + Frederic Crozat <fcrozat@mandriva.com>
    - Patch1 (GIT): various GIT fixes

* Mon Apr 26 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 538842
- update to new version 2.30.1

* Fri Apr 09 2010 Funda Wang <fwang@mandriva.org> 2.30.0-2mdv2010.1
+ Revision: 533333
- rebuild

* Mon Mar 29 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528931
- update to new version 2.30.0
- remove old configure option

* Mon Mar 08 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 515652
- update build deps
- update to new version 2.29.92

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 2.29.91-2mdv2010.1
+ Revision: 511563
- rebuilt against openssl-0.9.8m

* Mon Feb 22 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 509586
- update to new version 2.29.91

* Mon Feb 08 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.90-1mdv2010.1
+ Revision: 502043
- update to new version 2.29.90

* Mon Jan 25 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.6-1mdv2010.1
+ Revision: 495908
- update to new version 2.29.6

* Mon Jan 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.5-1mdv2010.1
+ Revision: 489894
- new version
- new edata-cal major

* Mon Dec 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.4-1mdv2010.1
+ Revision: 480884
- update to new version 2.29.4

* Wed Dec 09 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.3-1mdv2010.1
+ Revision: 475367
- new version
- update build deps
- drop exchange-storage lib
- update file list

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458689
- Fix BR
- Release 2.28.1

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446483
- update to new version 2.28.0

* Mon Sep 07 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 432722
- update to new version 2.27.92

* Mon Aug 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 420259
- update to new version 2.27.91

* Mon Aug 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 414277
- update to new version 2.27.90

* Mon Jul 27 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 400551
- update to new version 2.27.5

* Mon Jul 13 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 395457
- update to new version 2.27.4

* Mon Jun 15 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 386062
- update to new version 2.27.3

* Mon May 25 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 379628
- update to new version 2.27.2

* Mon May 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 374163
- new version
- new dir version

* Wed Apr 15 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1.1-1mdv2009.1
+ Revision: 367533
- update to new version 2.26.1.1

* Tue Apr 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366930
- update to new version 2.26.1

* Mon Mar 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355701
- update to new version 2.26.0

* Mon Mar 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 347255
- new version
- drop patch 1

* Mon Feb 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 340938
- update to new version 2.25.91

* Mon Feb 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 336517
- new version
- update patch 1
- depend on libical
- new camel major

* Mon Jan 19 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.5-1mdv2009.1
+ Revision: 331259
- update to new version 2.25.5

* Tue Jan 06 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.4-1mdv2009.1
+ Revision: 325396
- new version
- bump libgweather dep

* Fri Dec 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 316162
- update build deps
- new version
- fix build

* Tue Dec 02 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.2-2mdv2009.1
+ Revision: 309160
- fix build deps
- rebuild to get rid of libtasn1 dep

* Tue Dec 02 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 309038
- fix build deps
- update to new version 2.25.2

* Sun Nov 09 2008 Adam Williamson <awilliamson@mandriva.org> 2.25.1-2mdv2009.1
+ Revision: 301222
- rebuild for xcb changes

* Mon Nov 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 299480
- new version
- new base ver
- new camel major

* Mon Oct 20 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295642
- new version
- new camel major
- drop patch 1

* Wed Oct 01 2008 Frederic Crozat <fcrozat@mandriva.com> 2.24.0-2mdv2009.0
+ Revision: 290466
- Patch1 (SVN): various bug fixes from SVN

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286537
- new version

* Mon Sep 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282522
- new version
- update license

* Mon Sep 01 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 278208
- new version

* Tue Aug 19 2008 Frederic Crozat <fcrozat@mandriva.com> 2.23.90.1-1mdv2009.0
+ Revision: 273963
- Release 2.23.90.1

* Tue Aug 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.90-3mdv2009.0
+ Revision: 273603
- fix previous fix

* Mon Aug 18 2008 Oden Eriksson <oeriksson@mandriva.com> 2.23.90-2mdv2009.0
+ Revision: 273355
- rebuild
- try to unbork stuff with the mozilla lib deps

* Mon Aug 18 2008 Frederic Crozat <fcrozat@mandriva.com> 2.23.90-1mdv2009.0
+ Revision: 273214
- Release 2.23.90

* Mon Aug 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 263157
- new version
- drop patches 1 and 2

* Mon Jul 28 2008 Pascal Terjan <pterjan@mandriva.org> 2.23.5-2mdv2009.0
+ Revision: 251045
- Upstream patch for a crash on startup (Upstream #544049)

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - patch to fix gtk-doc build

* Tue Jul 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.5-1mdv2009.0
+ Revision: 240182
- fix buildrequires
- new version
- new camel major
- drop camel-provider package
- disable gtk-doc build

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.4-1mdv2009.0
+ Revision: 230971
- new version
- bump major numbers
- add ebackend package

* Mon Jun 30 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.3-1mdv2009.0
+ Revision: 230220
- new version
- drop patch 1
- update license

  + Frederic Crozat <fcrozat@mandriva.com>
    - Don't package changelog, package NEWS, more informative

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Jun 05 2008 Frederic Crozat <fcrozat@mandriva.com> 2.22.2-2mdv2009.0
+ Revision: 215236
- disable over/under linking checks for now, Makefile.am patch prevent build
- Patch1 : various IMAP bug fixes from SVN

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - fix buildrequires
    - new version
    - patch to fix linking

* Sun May 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.1.1-2mdv2009.0
+ Revision: 201161
- new version

* Tue Apr 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.1-2mdv2009.0
+ Revision: 193612
- rebuild for missing package on x86_64

* Wed Apr 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 192466
- new version
- drop patch

* Tue Apr 01 2008 Frederic Crozat <fcrozat@mandriva.com> 2.22.0-2mdv2008.1
+ Revision: 191377
- Patch0: various fixes from SVN

* Mon Mar 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183289
- new version

* Mon Feb 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 174989
- new version

* Tue Feb 12 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.91-2mdv2008.1
+ Revision: 166144
- libsoup rebuild

* Mon Feb 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 165221
- new version

* Mon Jan 28 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 159518
- new version
- new camel major
- bump deps

* Thu Jan 17 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.5.1-1mdv2008.1
+ Revision: 153973
- new version

* Mon Jan 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 151525
- new version
- drop patch

* Mon Dec 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-3mdv2008.1
+ Revision: 137399
- patch to fix bug #36319

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 21 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-2mdv2008.1
+ Revision: 136243
- rebuild for db 4.6

* Mon Dec 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-1mdv2008.1
+ Revision: 130001
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.3-1mdv2008.1
+ Revision: 115202
- new version

* Fri Nov 16 2007 Frederic Crozat <fcrozat@mandriva.com> 2.21.2-2mdv2008.1
+ Revision: 109121
- Remove patch1, it was merged upstream

* Tue Nov 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.2-1mdv2008.1
+ Revision: 108388
- new version

* Mon Oct 29 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.1-1mdv2008.1
+ Revision: 102947
- new version
- new base version
- add package for libgdata

* Mon Oct 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.12.1-1mdv2008.1
+ Revision: 98551
- new version
- drop patch 2

* Wed Oct 10 2007 Frederic Crozat <fcrozat@mandriva.com> 1.12.0-2mdv2008.1
+ Revision: 96894
- Patch2: fix e-d-s leak (GNOME bug #420167)

* Mon Sep 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.12.0-1mdv2008.0
+ Revision: 89317
- new version

* Mon Sep 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.11.92-1mdv2008.0
+ Revision: 78770
- new version

* Mon Aug 27 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.11.91-1mdv2008.0
+ Revision: 72045
- new version

* Tue Aug 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.11.90-1mdv2008.0
+ Revision: 63034
- new version

* Wed Aug 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.11.6.1-1mdv2008.0
+ Revision: 57378
- new version
- new devel name

* Tue Jul 31 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.11.6-1mdv2008.0
+ Revision: 56937
- new version

* Mon Jul 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.11.5-1mdv2008.0
+ Revision: 50651
- new version

* Mon Jun 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.11.4-1mdv2008.0
+ Revision: 41016
- new version
- new version
- new base version
- update patch 1
- drop patch 3

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags

* Mon May 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.10.2-1mdv2008.0
+ Revision: 32137
- new version
- drop merged patches

* Wed May 23 2007 Pascal Terjan <pterjan@mandriva.org> 1.10.1-3mdv2008.0
+ Revision: 30111
- Fix a crash when using timezones which do not include a TZNAME (GNOME bug #425129)

* Mon May 21 2007 Frederic Crozat <fcrozat@mandriva.com> 1.10.1-2mdv2008.0
+ Revision: 29366
- Patch4 (SVN): fix APOP vulnerability (CVE 2007-1558)

* Tue Apr 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.10.1-1mdv2008.0
+ Revision: 14041
- new version
- drop patch 0


* Tue Apr 03 2007 Frederic Crozat <fcrozat@mandriva.com> 1.10.0-4mdv2007.1
+ Revision: 150347
- Patch2: fix bug report when e-d-s crashes
- Patch3 (Fedora): support for Exchange 2003 behind ISA Server 2004 (GNOME bug #415922)
- build with db4 dynamically now, reduce memory usage

* Wed Mar 28 2007 Pascal Terjan <pterjan@mandriva.org> 1.10.0-3mdv2007.1
+ Revision: 149236
- fix empty dialog when gnupg returns errors in non utf8 locale

* Thu Mar 15 2007 Frederic Crozat <fcrozat@mandriva.com> 1.10.0-2mdv2007.1
+ Revision: 144442
- Patch0 (SVN): disable forgotten debug output

* Mon Mar 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.10.0-1mdv2007.1
+ Revision: 142117
- new version

* Mon Feb 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.92-1mdv2007.1
+ Revision: 125992
- new version

* Mon Feb 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.91-1mdv2007.1
+ Revision: 120042
- new version
- drop patch

* Fri Jan 26 2007 Pascal Terjan <pterjan@mandriva.org> 1.9.6.1-3mdv2007.1
+ Revision: 113727
- Fix GNOME bug #400841 (new mails not appearing when using IMAP)

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - disable Gnome Keyring for now

* Tue Jan 23 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.6.1-1mdv2007.1
+ Revision: 112597
- new version

* Mon Jan 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.6-1mdv2007.1
+ Revision: 112087
- new version
- enable gnome-keyring, it doesn't build otherwise
- reenable gtk-doc

* Tue Jan 16 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.4-3mdv2007.1
+ Revision: 109629
- readd gtk-doc files to the file list
- emergency rebuild without gtk-doc
- rebuild

* Tue Dec 19 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.4-2mdv2007.1
+ Revision: 99758
- fix libcamel package

* Tue Dec 19 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.4-1mdv2007.1
+ Revision: 99078
- new version
- new major

* Fri Dec 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.3-2mdv2007.1
+ Revision: 92164
- rebuild for new firefox

* Tue Dec 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.3-1mdv2007.1
+ Revision: 90709
- new version

* Wed Nov 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.2-2mdv2007.1
+ Revision: 88438
- rebuild

* Mon Nov 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.2-1mdv2007.1
+ Revision: 87536
- new version
- update some majors

* Thu Nov 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.8.2-4mdv2007.1
+ Revision: 86614
- bot rebuild
- bot rebuild
- bot rebuild
- new version

* Fri Oct 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.8.1-3mdv2007.1
+ Revision: 63824
- rebuild
- rebuild
- Import evolution-data-server

* Fri Oct 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.8.1-1mdv2007.0
- New version 1.8.1

* Tue Sep 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.8.0-1mdv2007.0
- New release 1.8.0

* Tue Aug 22 2006 Frederic Crozat <fcrozat@mandriva.com> 1.7.92-1mdv2007.0
- Release 1.7.92

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 1.7.91-1mdv2007.0
- fix majors
- New release 1.7.91

* Wed Aug 02 2006 Frederic Crozat <fcrozat@mandriva.com> 1.7.90.1-2mdv2007.0
- Rebuild with latest dbus

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 1.7.90.1-1mdv2007.0
- drop patch
- New release 1.7.90.1

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 1.7.90-2mdv2007.0
- fix edatacal major

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 1.7.90-1mdv2007.0
- new majors
- patch to fix build, the release tarball is missing some files
- New release 1.7.90

* Tue Jul 18 2006 Frederic Crozat <fcrozat@mandriva.com> 1.7.4-2mdv2007.0
- Rebuild to drop obsolete libhowl dependency

* Tue Jul 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.7.4-1mdv2007.0
- New release 1.7.4

* Wed Jun 14 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.7.3-1
- New release 1.7.3

* Fri Jun 02 2006 Frederic Crozat <fcrozat@mandriva.com> 1.7.2-1mdv2007.0
- Release 1.7.2
- Remove patch1 (merged upstream)

* Wed May 31 2006 Götz Waschk <waschk@mandriva.org> 1.6.2-2mdv2007.0
- fix edata-cal major

* Wed May 31 2006 Götz Waschk <waschk@mandriva.org> 1.6.2-1mdv2007.0
- new majors
- drop patch 0
- New release 1.6.2

* Fri May 05 2006 Frederic Crozat <fcrozat@mandriva.com> 1.6.1-3mdk
- Patch1 (CVS): fix crash with invalid UTF-8 (GNOME bug #335961)

* Fri Apr 14 2006 Stew Benedict <sbenedict@mandriva.com> 1.6.1-2mdk
- rebuild - x86_64 got built against unowned libsoup-2.2.so.7

* Thu Apr 13 2006 Frederic Crozat <fcrozat@mandriva.com> 1.6.1-1mdk
- Release 1.6.1

* Thu Jan 12 2006 Frederic Crozat <fcrozat@mandriva.com> 1.4.2.1-5mdk
- Fix error in libedataserverui major name
- fix dependencies to allow upgrade from 2006 with auto-select

* Mon Jan 09 2006 Frederic Crozat <fcrozat@mandriva.com> 1.4.2.1-4mdk
- Replace some conflicts with obsoletes, allow smooth cooker upgrade

* Mon Jan 09 2006 Götz Waschk <waschk@mandriva.org> 1.4.2.1-3mdk
- split lib package
- mkrel

* Mon Dec 05 2005 Frederic Crozat <fcrozat@mandriva.com> 1.4.2.1-2mdk
- Patch0 (CVS): various crash fixes

* Wed Nov 30 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.4.2.1-1mdk
- New release 1.4.2.1

* Tue Nov 29 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.4.2-1mdk
- New release 1.4.2

* Mon Oct 10 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.4.1.1-1mdk
- New release 1.4.1.1

* Thu Oct 06 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.4.1-2mdk
- rebuild for new libsoup

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 1.4.1-1mdk
- Release 1.4.1
- Remove patches 2, 3, 4 (merged upstream)

* Fri Sep 16 2005 Frederic Crozat <fcrozat@mandriva.com> 1.2.3-7mdk 
- Patch4 (CVS): various fixes (mainly crashers)

* Wed Aug 31 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.2.3-6mdk
- Rebuild for new libldap-2.2

* Mon Aug 08 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.2.3-5mdk
- add BuildRequires: intltool gnome-common

* Tue Jul 05 2005 Frederic Crozat <fcrozat@mandriva.com> 1.2.3-4mdk 
- Patch3: fix i18n not initialised correctly in camel

* Sat Jun 18 2005 Andreas Hasenack <andreas@mandriva.com> 1.2.3-3mdk
- built without krb4

* Fri Jun 10 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.2.3-2mdk
- Rebuild for libkrb53-devel 1.4.1

* Mon Jun 06 2005 Götz Waschk <waschk@mandriva.org> 1.2.3-1mdk
- small build patch
- New release 1.2.3

* Wed May 04 2005 Frederic Crozat <fcrozat@mandriva.com> 1.2.2-7mdk 
- Enable kerberos support (Mdk bug #15781)

* Tue Apr 26 2005 Frederic Crozat <fcrozat@mandriva.com> 1.2.2-6mdk 
- Patch1: fix location of eds daemon (GNOME bug #15593)

* Fri Apr 22 2005 Götz Waschk <waschk@mandriva.org> 1.2.2-5mdk
- fix buildrequires

* Fri Apr 22 2005 Götz Waschk <waschk@mandriva.org> 1.2.2-4mdk
- fix buildrequires

* Fri Apr 22 2005 Götz Waschk <waschk@mandriva.org> 1.2.2-3mdk
- fix buildrequires

* Fri Apr 22 2005 Götz Waschk <waschk@mandriva.org> 1.2.2-2mdk
- fix devel deps

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 1.2.2-1mdk 
- Release 1.2.2 (based on Götz Waschk package)

* Wed Mar 16 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.4-2mdk 
- Patch0 (CVS): fix webcal timezone handling
- Patch1 (CVS): fix eds not exiting (Mdk bug #13920)

* Fri Feb 18 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.4-1mdk 
- Release 1.0.4

* Fri Feb 04 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.0.3-3mdk
- rebuild for ldap2.2_7

* Tue Jan 04 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.3-2mdk 
- Rebuild with latest howl

* Tue Dec 07 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.3-1mdk
- New release 1.0.3

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.2-1mdk
- drop merged patches 0,1
- New release 1.0.2

* Sat Oct 02 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.1-2mdk
- Patch0 (CVS): fix file_as attribute for vcard
- Patch1 (CVS): fix duplication with remote calendars

* Thu Sep 30 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.1-1mdk
- Release 1.0.1
- Remove patch0 (merged upstream)

* Wed Sep 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.0-2mdk
- Patch0: Fix addressbook loading on AMD CPUs

* Wed Sep 15 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.0-1mdk
- Release 1.0.0

* Tue Aug 31 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.0.99-1mdk
- Release 0.0.99

* Sat Aug 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.0.98-2mdk
- Rebuild with latest libsoup

* Tue Aug 17 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.98-1mdk
- requires new soup
- New release 0.0.98

* Wed Aug 04 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.0.97-1mdk
- New release 0.0.97

* Wed Jul 21 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.96-1mdk
- requires new soup
- New release 0.0.96

* Tue Jul 06 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.0.95-1mdk
- New release 0.0.95

* Fri Jun 18 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.0.94.1-1mdk
- New release 0.0.94.1

* Mon Jun 07 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.94-1mdk
- requires new soup
- New release 0.0.94

* Sun May 23 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.93-1mdk
- fix URL
- reenable libtoolize
- New release 0.0.93

* Fri Apr 30 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.92-2mdk
- fix buildrequires

* Wed Apr 21 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.0.92-1mdk
- Initial Mandrakelinux package

