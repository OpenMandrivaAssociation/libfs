%define major 6
%define libname %mklibname fs %{major}
%define develname %mklibname fs -d

Summary:	Library Interface to the X Font Server
Name:		libfs
Version:	1.0.4
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libFS-%{version}.tar.bz2
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	x11-xtrans-devel >= 1.0.0

%description
Libfs is a library interface to the X Font Server.

%package -n %{libname}
Summary:	Library Interface to the X Font Server
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
Libfs is a library interface to the X Font Server.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	libxorg-x11-devel < 7.0
Obsoletes:	%{_lib}fs-static-devel < 1.0.4

%description -n %{develname}
Development files for %{name}.

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%prep
%setup -qn libFS-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std
rm -f %{buildroot}%{_datadir}/doc/libFS/FSlib.txt

%files -n %{libname}
%doc doc/FSlib.txt
%{_libdir}/libFS.so.%{major}*

%files -n %{develname}
%{_libdir}/libFS.so
%{_libdir}/pkgconfig/libfs.pc
%{_includedir}/X11/fonts/FSlib.h


%changelog
* Thu Aug 16 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.4-1
+ Revision: 814980
- spec file clean
- update to new version 1.0.4

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.3-3
+ Revision: 745620
- fixed typo
- rebuild
- disabled static build
- removed .la files
- cleaned up spec
- employed major macro

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2
+ Revision: 660251
- mass rebuild

* Thu Oct 28 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 589776
- adjust file list
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2010.1
+ Revision: 520777
- rebuilt for 2010.1

* Wed Jul 08 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.0.2-1mdv2010.0
+ Revision: 393478
- update to new version 1.0.2

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2009.0
+ Revision: 264798
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jun 02 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-2mdv2009.0
+ Revision: 214368
- Rebuild to match changes in xtrans.

  + Thierry Vignaud <tv@mandriva.org>
    - improved description

* Tue May 27 2008 Colin Guthrie <cguthrie@mandriva.org> 1.0.1-1mdv2009.0
+ Revision: 211827
- New version
- Minor spec cleanup

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.0-5mdv2008.1
+ Revision: 153338
- Update BuildRequires and rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-4mdv2008.1
+ Revision: 150561
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Jul 21 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-3mdv2008.0
+ Revision: 54150
- rebuild for 2008
- new devel policy


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

