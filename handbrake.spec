Summary:	A program to transcode DVDs and other sources to MPEG-4 and MKV
Summary(pl.UTF-8):	Program do przekodowywania DVD i innych źródeł do formatów MPEG-4 i MKV
Name:		handbrake
Version:	1.9.0
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	https://github.com/HandBrake/HandBrake/releases/download/%{version}/HandBrake-%{version}-source.tar.bz2
# Source0-md5:	ebe3a23bcb66194b144240009cd8b7dc
# Source1 is a tarball of the downloads/ folder that contains third party
# libraries required and automatically downloaded by HandBrake the first
# time 'make' is run. If you update Source0 to a newer release you must
# recreate an updated Source1 tarball for it too!
Source1:	HandBrake-%{version}-contrib-tarballs.tar
# Source1-md5:	de3c724885c4fd10ee4bc7161747e17b
URL:		https://handbrake.fr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	glib2-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+3-devel
BuildRequires:	harfbuzz-devel
BuildRequires:	intltool
BuildRequires:	jansson-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libass-devel
BuildRequires:	libnotify-devel
BuildRequires:	libogg-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libx264-devel
BuildRequires:	libxml2-devel
BuildRequires:	m4
BuildRequires:	opus-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 2.005
BuildRequires:	subversion
BuildRequires:	udev-glib-devel
BuildRequires:	yasm
BuildRequires:	zlib-devel
BuildConflicts:	libudfread-devel
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
HandBrake is an open-source, GPL-licensed, multi-platform,
multi-threaded transcoder, available for MacOS X, Linux and Windows.

%description -l pl.UTF-8
HandBrake to mający otwarte źródła, wydany na licencji GPL,
wieloplatformowy, wielowątkowy program do przekodowywania filmów,
dostępny dla systemów MacOS X, Linux i Windows.

%package cli
Summary:	A program to transcode DVDs and other sources to MPEG-4 and MKV
Summary(pl.UTF-8):	Program do przekodowywania DVD i innych źródeł do formatów MPEG-4 i MKV
Group:		Applications/Multimedia
Requires:	libdvdcss
Obsoletes:	HandBrake < 1
Obsoletes:	handbrake < 1

%description cli
HandBrake is an open-source, GPL-licensed, multi-platform,
multi-threaded transcoder, available for MacOS X, Linux and Windows.

This is the CLI tool version of HandBrake.

%description cli -l pl.UTF-8
HandBrake to mający otwarte źródła, wydany na licencji GPL,
wieloplatformowy, wielowątkowy program do przekodowywania filmów,
dostępny dla systemów MacOS X, Linux i Windows.

Ten pakiet zawiera HandBrake w postaci narzędzia linii poleceń.

%package gui
Summary:	A program to transcode DVDs and other sources to MPEG-4 and MKV
Summary(pl.UTF-8):	Program do przekodowywania DVD i innych źródeł do formatów MPEG-4 i MKV
Group:		Applications/Multimedia
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-ugly
Requires:	gtk+3
Requires:	libdvdcss
Obsoletes:	HandBrake < 1
Obsoletes:	handbrake < 1

%description gui
HandBrake is an open-source, GPL-licensed, multi-platform,
multi-threaded transcoder, available for MacOS X, Linux and Windows.

This is the GTK GUI version of HandBrake.

%description gui -l pl.UTF-8
HandBrake to mający otwarte źródła, wydany na licencji GPL,
wieloplatformowy, wielowątkowy program do przekodowywania filmów,
dostępny dla systemów MacOS X, Linux i Windows.

Ten pakiet zawiera HandBrake z graficznym interfejsem GTK.

%prep
%setup -q -n HandBrake-%{version} -a1

%build
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"
./configure \
	--force \
	--prefix=%{_prefix} \
	--disable-libdovi \
	--disable-df-fetch

cat > build/GNUmakefile.custom.defs <<EOF
STRIP.exe = /bin/true
BUILD.jobs = %{__jobs}
GCC.args.g.none = %{rpmcflags}
GCC.args.O.speed = %{rpmcflags}
EOF

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_localedir}/sl{_SI,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/uk{_UA,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{no,nb}

%find_lang ghb

%clean
rm -rf $RPM_BUILD_ROOT

%post gui
%update_icon_cache hicolor
%update_desktop_database_post

%postun gui
%update_icon_cache hicolor
%update_desktop_database_postun

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/HandBrakeCLI

%files gui -f ghb.lang
%defattr(644,root,root,755)
%doc COPYING AUTHORS.markdown NEWS.markdown README.markdown THANKS.markdown
%attr(755,root,root) %{_bindir}/ghb
%{_desktopdir}/fr.handbrake.ghb.desktop
%{_iconsdir}/hicolor/scalable/apps/fr.handbrake.ghb.svg
%{_datadir}/metainfo/fr.handbrake.ghb.metainfo.xml
