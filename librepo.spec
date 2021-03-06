#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : librepo
Version  : 1.7.20
Release  : 41
URL      : file:///aot/build/clearlinux/packages/librepo/librepo-1.7.20.tar.gz
Source0  : file:///aot/build/clearlinux/packages/librepo/librepo-1.7.20.tar.gz
Summary  : Repodata downloading library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 LGPL-2.1+
Requires: librepo-lib = %{version}-%{release}
Requires: librepo-python = %{version}-%{release}
Requires: librepo-python3 = %{version}-%{release}
BuildRequires : Flask
BuildRequires : Sphinx
BuildRequires : acl-staticdev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : check-dev
BuildRequires : compat-lua-53
BuildRequires : compat-lua-53-abi
BuildRequires : compat-lua-53-bin
BuildRequires : compat-lua-53-dev
BuildRequires : compat-lua-53-lib
BuildRequires : compat-lua-53-man
BuildRequires : compat-lua-53-staticdev
BuildRequires : curl-dev
BuildRequires : db-dev
BuildRequires : dbus-dev
BuildRequires : dbus-glib
BuildRequires : dbus-glib-dev
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : expat-dev
BuildRequires : expat-staticdev
BuildRequires : expect
BuildRequires : fakechroot
BuildRequires : fakechroot-dev
BuildRequires : fakechroot-staticdev
BuildRequires : file
BuildRequires : file-abi
BuildRequires : file-bin
BuildRequires : file-data
BuildRequires : file-dev
BuildRequires : file-lib
BuildRequires : file-license
BuildRequires : file-man
BuildRequires : flex
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
BuildRequires : gdb
BuildRequires : gdb-dev
BuildRequires : gettext-bin
BuildRequires : git
BuildRequires : glib
BuildRequires : glib-dev
BuildRequires : glibc-abi
BuildRequires : glibc-bench
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-doc
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : gmp-dev
BuildRequires : gmp-staticdev
BuildRequires : gnupg
BuildRequires : gpgme
BuildRequires : gpgme-dev
BuildRequires : graphviz
BuildRequires : guile
BuildRequires : json-c
BuildRequires : json-c-dev
BuildRequires : json-c-staticdev
BuildRequires : libarchive
BuildRequires : libarchive-dev
BuildRequires : libarchive-staticdev
BuildRequires : libassuan-dev
BuildRequires : libcap
BuildRequires : libcap-dev
BuildRequires : libcomps-dev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libgcrypt
BuildRequires : libgcrypt-dev
BuildRequires : libmodulemd
BuildRequires : libmodulemd-dev
BuildRequires : libmodulemd-staticdev
BuildRequires : librepo-dev
BuildRequires : librepo-staticdev
BuildRequires : libsolv-dev
BuildRequires : libstdc++
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libunwind
BuildRequires : libunwind-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : lz4-dev
BuildRequires : lz4-staticdev
BuildRequires : lzo-dev
BuildRequires : lzo-staticdev
BuildRequires : m4
BuildRequires : nettle-dev
BuildRequires : nettle-staticdev
BuildRequires : nose
BuildRequires : nspr-dev
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : popt
BuildRequires : popt-dev
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : rpm
BuildRequires : rpm-dev
BuildRequires : smartcols
BuildRequires : sqlite-autoconf
BuildRequires : sqlite-autoconf-dev
BuildRequires : sqlite-autoconf-staticdev
BuildRequires : swig
BuildRequires : unzip
BuildRequires : xattr
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zip
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
A library providing C and Python (libcURL like) API to downloading repository
metadata.

%package dev
Summary: dev components for the librepo package.
Group: Development
Requires: librepo-lib = %{version}-%{release}
Provides: librepo-devel = %{version}-%{release}
Requires: librepo = %{version}-%{release}

%description dev
dev components for the librepo package.


%package lib
Summary: lib components for the librepo package.
Group: Libraries

%description lib
lib components for the librepo package.


%package python
Summary: python components for the librepo package.
Group: Default
Requires: librepo-python3 = %{version}-%{release}

%description python
python components for the librepo package.


%package python3
Summary: python3 components for the librepo package.
Group: Default
Requires: python3-core

%description python3
python3 components for the librepo package.


%package staticdev
Summary: staticdev components for the librepo package.
Group: Default
Requires: librepo-dev = %{version}-%{release}

%description staticdev
staticdev components for the librepo package.


%prep
%setup -q -n librepo
cd %{_builddir}/librepo

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618980871
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_GEN"
export FCFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_GEN"
export FFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_GEN"
export LDFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
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
%cmake .. -DPYTHON_DESIRED=3 \
-DENABLE_TESTS=ON \
-DENABLE_DOCS=OFF \
-DWITH_ZCHUNK=OFF \
-DENABLE_PYTHON=ON \
-DCMAKE_BUILD_TYPE="Release"
make  %{?_smp_mflags}

ctest --parallel 16 -V --progress || :
#make -j1 check || :
#make -j1 test  || :
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
%cmake .. -DPYTHON_DESIRED=3 \
-DENABLE_TESTS=OFF \
-DENABLE_DOCS=OFF \
-DWITH_ZCHUNK=OFF \
-DENABLE_PYTHON=ON \
-DCMAKE_BUILD_TYPE="Release"
make  %{?_smp_mflags}
fi
popd

%install
export SOURCE_DATE_EPOCH=1618980871
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/librepo/checksum.h
/usr/include/librepo/downloader.h
/usr/include/librepo/downloader_internal.h
/usr/include/librepo/downloadtarget.h
/usr/include/librepo/fastestmirror.h
/usr/include/librepo/gpg.h
/usr/include/librepo/handle.h
/usr/include/librepo/librepo.h
/usr/include/librepo/metadata_downloader.h
/usr/include/librepo/metalink.h
/usr/include/librepo/mirrorlist.h
/usr/include/librepo/package_downloader.h
/usr/include/librepo/rcodes.h
/usr/include/librepo/repoconf.h
/usr/include/librepo/repomd.h
/usr/include/librepo/repoutil_yum.h
/usr/include/librepo/result.h
/usr/include/librepo/types.h
/usr/include/librepo/url_substitution.h
/usr/include/librepo/util.h
/usr/include/librepo/version.h
/usr/include/librepo/xmlparser.h
/usr/include/librepo/yum.h
/usr/lib64/librepo.so
/usr/lib64/pkgconfig/librepo.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/librepo.so.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/librepo.a
