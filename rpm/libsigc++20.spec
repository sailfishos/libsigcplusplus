Name:           libsigc++20
Version:        2.10.4
Release:        1
Summary:        Typesafe signal framework for C++

License:        LGPLv2+
URL:            https://github.com/libsigcplusplus/libsigcplusplus
Source0:        %{name}-%{version}.tar.bz2
Patch0:         0001-Disable-mm-common-checking-as-we-do-not-use-it.patch

BuildRequires:  gcc-c++
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl

%description
libsigc++ implements a typesafe callback system for standard C++. It
allows you to define signals and to connect those signals to any
callback function, either global or a member function, regardless of
whether it is static or virtual.

libsigc++ is used by gtkmm to wrap the GTK+ signal system. It does not
depend on GTK+ or gtkmm.


%package devel
Summary:        Development tools for the typesafe signal framework for C++
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the static libraries and header files
needed for development with %{name}.


%package        doc
Summary:        Documentation for %{name}, includes full API docs
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains documentation for %{name}.


%prep
%autosetup -p1 -n libsigc++20-%{version}/upstream


%build
%meson -Dbuild-documentation=false -Dmaintainer-mode=true
%meson_build


%install
%meson_install

%post -n libsigc++20 -p /sbin/ldconfig

%postun -n libsigc++20 -p /sbin/ldconfig


%files
%license COPYING
%{_libdir}/libsigc-2.0.so.0*

%files devel
%{_includedir}/*
%{_libdir}/sigc++-2.0/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libsigc-2.0.so

%files doc
%doc AUTHORS README NEWS
