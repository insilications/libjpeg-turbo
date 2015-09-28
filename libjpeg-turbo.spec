#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libjpeg-turbo
Version  : 1.4.2
Release  : 12
URL      : http://downloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-1.4.2.tar.gz
Source0  : http://downloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-1.4.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause IJG
Requires: libjpeg-turbo-bin
Requires: libjpeg-turbo-lib
Requires: libjpeg-turbo-doc
BuildRequires : cmake
BuildRequires : nasm-bin

%description
libjpeg-turbo note:  This file has been modified by The libjpeg-turbo Project
to include only information relevant to libjpeg-turbo, to wordsmith certain
sections, and to remove impolitic language that existed in the libjpeg v8
information specific to libjpeg-turbo.

%package bin
Summary: bin components for the libjpeg-turbo package.
Group: Binaries

%description bin
bin components for the libjpeg-turbo package.


%package dev
Summary: dev components for the libjpeg-turbo package.
Group: Development
Requires: libjpeg-turbo-lib
Requires: libjpeg-turbo-bin
Provides: libjpeg-turbo-devel

%description dev
dev components for the libjpeg-turbo package.


%package doc
Summary: doc components for the libjpeg-turbo package.
Group: Documentation

%description doc
doc components for the libjpeg-turbo package.


%package lib
Summary: lib components for the libjpeg-turbo package.
Group: Libraries

%description lib
lib components for the libjpeg-turbo package.


%prep
%setup -q -n libjpeg-turbo-1.4.2

%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export CFLAGS="$CFLAGS -O3 -fno-semantic-interposition -ffunction-sections -flto "
export CXXFLAGS="$CXXFLAGS -O3 -fno-semantic-interposition -ffunction-sections -flto "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cjpeg
/usr/bin/djpeg
/usr/bin/jpegtran
/usr/bin/rdjpgcom
/usr/bin/tjbench
/usr/bin/wrjpgcom

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libjpeg-turbo/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
