#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libjpeg-turbo
Version  : 2.1.0
Release  : 301
URL      : file:///aot/build/clearlinux/packages/libjpeg-turbo/libjpeg-turbo-v2.1.0.tar.gz
Source0  : file:///aot/build/clearlinux/packages/libjpeg-turbo/libjpeg-turbo-v2.1.0.tar.gz
Summary  : A SIMD-accelerated JPEG codec that provides the TurboJPEG API
Group    : Development/Tools
License  : IJG
Requires: libjpeg-turbo-bin = %{version}-%{release}
Requires: libjpeg-turbo-lib = %{version}-%{release}
Requires: libjpeg-turbo-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : findutils
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : nasm
BuildRequires : openjdk13
BuildRequires : openjdk13-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : yasm
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
BuildRequires : zlib-staticdev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
TurboJPEG Java Wrapper
======================
The TurboJPEG shared library can optionally be built with a Java Native
Interface wrapper, which allows the library to be loaded and used directly from
Java applications.  The Java front end for this is defined in several classes
located under org/libjpegturbo/turbojpeg.  The source code for these Java
classes is licensed under a BSD-style license, so the files can be incorporated
directly into both open source and proprietary projects without restriction.  A
Java archive (JAR) file containing these classes is also shipped with the
"official" distribution packages of libjpeg-turbo.

%package bin
Summary: bin components for the libjpeg-turbo package.
Group: Binaries

%description bin
bin components for the libjpeg-turbo package.


%package dev
Summary: dev components for the libjpeg-turbo package.
Group: Development
Requires: libjpeg-turbo-lib = %{version}-%{release}
Requires: libjpeg-turbo-bin = %{version}-%{release}
Provides: libjpeg-turbo-devel = %{version}-%{release}
Requires: libjpeg-turbo = %{version}-%{release}

%description dev
dev components for the libjpeg-turbo package.


%package dev32
Summary: dev32 components for the libjpeg-turbo package.
Group: Default
Requires: libjpeg-turbo-lib32 = %{version}-%{release}
Requires: libjpeg-turbo-bin = %{version}-%{release}
Requires: libjpeg-turbo-dev = %{version}-%{release}

%description dev32
dev32 components for the libjpeg-turbo package.


%package doc
Summary: doc components for the libjpeg-turbo package.
Group: Documentation
Requires: libjpeg-turbo-man = %{version}-%{release}

%description doc
doc components for the libjpeg-turbo package.


%package lib
Summary: lib components for the libjpeg-turbo package.
Group: Libraries

%description lib
lib components for the libjpeg-turbo package.


%package lib32
Summary: lib32 components for the libjpeg-turbo package.
Group: Default

%description lib32
lib32 components for the libjpeg-turbo package.


%package man
Summary: man components for the libjpeg-turbo package.
Group: Default

%description man
man components for the libjpeg-turbo package.


%package staticdev
Summary: staticdev components for the libjpeg-turbo package.
Group: Default
Requires: libjpeg-turbo-dev = %{version}-%{release}

%description staticdev
staticdev components for the libjpeg-turbo package.


%package staticdev32
Summary: staticdev32 components for the libjpeg-turbo package.
Group: Default
Requires: libjpeg-turbo-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the libjpeg-turbo package.


%prep
%setup -q -n libjpeg-turbo
cd %{_builddir}/libjpeg-turbo

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622249496
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FCFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export CXXFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export LDFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common -funroll-loops
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags_pgo end
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%cmake .. -DENABLE_SHARED=1 -DENABLE_STATIC=1 -DREQUIRE_SIMD=1 -DWITH_SIMD=1 -DWITH_TURBOJPEG=1
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1

VERBOSE=1 V=1 make %{?_smp_mflags} test || :
./tjbench ../testimages/testimgint.jpg
find . -type f,l -not -name '*.gcno' -not -name 'statuspgo*' -delete -print
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%cmake .. -DENABLE_SHARED=1 -DENABLE_STATIC=1 -DREQUIRE_SIMD=1 -DWITH_SIMD=1 -DWITH_TURBOJPEG=1
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1
fi
popd
mkdir -p clr-build32
pushd clr-build32
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_INSTALL_LIBDIR=/usr/lib32 -DLIB_SUFFIX=32 .. -DENABLE_SHARED=1 -DENABLE_STATIC=1 -DREQUIRE_SIMD=1 -DWITH_SIMD=1 -DWITH_TURBOJPEG=1
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1
unset PKG_CONFIG_PATH
popd

%install
export SOURCE_DATE_EPOCH=1622249496
rm -rf %{buildroot}
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
    pushd %{buildroot}/usr/lib32/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
popd
pushd clr-build
%make_install
popd
## install_append content
[ -d %{buildroot}/usr/lib/ ] && mv %{buildroot}/usr/lib/*so* %{buildroot}/usr/lib32
install -dm 0755 %{buildroot}/usr/lib64/haswell/ || :
cp --archive %{buildroot}/usr/lib64/lib*.so* %{buildroot}/usr/lib64/haswell/ || :
## install_append end

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
/usr/include/jconfig.h
/usr/include/jerror.h
/usr/include/jmorecfg.h
/usr/include/jpeglib.h
/usr/include/turbojpeg.h
/usr/lib64/cmake/libjpeg-turbo/libjpeg-turboConfig.cmake
/usr/lib64/cmake/libjpeg-turbo/libjpeg-turboConfigVersion.cmake
/usr/lib64/cmake/libjpeg-turbo/libjpeg-turboTargets-relwithdebinfo.cmake
/usr/lib64/cmake/libjpeg-turbo/libjpeg-turboTargets.cmake
/usr/lib64/haswell/libjpeg.so
/usr/lib64/haswell/libturbojpeg.so
/usr/lib64/libjpeg.so
/usr/lib64/libturbojpeg.so
/usr/lib64/pkgconfig/libjpeg.pc
/usr/lib64/pkgconfig/libturbojpeg.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/libjpeg-turbo/libjpeg-turboConfig.cmake
/usr/lib32/cmake/libjpeg-turbo/libjpeg-turboConfigVersion.cmake
/usr/lib32/cmake/libjpeg-turbo/libjpeg-turboTargets-relwithdebinfo.cmake
/usr/lib32/cmake/libjpeg-turbo/libjpeg-turboTargets.cmake
/usr/lib32/libjpeg.so
/usr/lib32/libturbojpeg.so
/usr/lib32/pkgconfig/32libjpeg.pc
/usr/lib32/pkgconfig/32libturbojpeg.pc
/usr/lib32/pkgconfig/libjpeg.pc
/usr/lib32/pkgconfig/libturbojpeg.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libjpeg\-turbo/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libjpeg.so.62
/usr/lib64/haswell/libjpeg.so.62.3.0
/usr/lib64/haswell/libturbojpeg.so.0
/usr/lib64/haswell/libturbojpeg.so.0.2.0
/usr/lib64/libjpeg.so.62
/usr/lib64/libjpeg.so.62.3.0
/usr/lib64/libturbojpeg.so.0
/usr/lib64/libturbojpeg.so.0.2.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libjpeg.so.62
/usr/lib32/libjpeg.so.62.3.0
/usr/lib32/libturbojpeg.so.0
/usr/lib32/libturbojpeg.so.0.2.0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cjpeg.1
/usr/share/man/man1/djpeg.1
/usr/share/man/man1/jpegtran.1
/usr/share/man/man1/rdjpgcom.1
/usr/share/man/man1/wrjpgcom.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libjpeg.a
/usr/lib64/libturbojpeg.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libjpeg.a
/usr/lib32/libturbojpeg.a
