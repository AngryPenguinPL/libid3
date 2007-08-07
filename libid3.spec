%define	major 0
%define libname	%mklibname id 3 %{major}
%define develname %mklibname -d id3

Summary:	ID3 Parsing Library
Name:		libid3
Version:	1.2
Release:	%mkrel 1
Group:		System/Libraries
License:	BSD-like
URL:		http://www.tangent.org/
Source0:	http://download.tangent.org/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Library for parsing ID3 tags from files or sections of memory.

%package -n	%{libname}
Summary:	ID3 Parsing Library
Group:          System/Libraries

%description -n	%{libname}
Library for parsing ID3 tags from files or sections of memory.

%package -n	%{develname}
Summary:	Static library and header files for the ID3 Parsing Library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Conflicts:	libid3_3.8-devel
Requires:	%{libname} = %{version}
Obsoletes:	%{libname}-devel

%description -n	%{develname}
Library for parsing ID3 tags from files or sections of memory.

This package contains the static libid3 library and its header
files.

%package	tools
Summary:	Tools using the ID3 Parsing Library
Group:		Sound

%description	tools
This package contains various files using the ID3 Parsing Library.

%prep

%setup -q -n %{name}-%{version}

%build

%configure2_5x  --disable-static

%make

# make the man pages
pod2man Docs/libID3.pod > libID3.3
pod2man Docs/tagpuller.pod > tagpuller.1

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_mandir}/man{1,3}

%makeinstall_std

install -m0755 tests/id3test %{buildroot}%{_bindir}/

install -m0644 libID3.3 %{buildroot}%{_mandir}/man3/
install -m0644 tagpuller.1 %{buildroot}%{_mandir}/man1/

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING ChangeLog README TODO
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_mandir}/man3/*

%files tools
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
