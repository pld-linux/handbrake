#
# TODO: build with system dav1d, libbluray, libdvdnav, libdvdread
#
Summary:	A program to transcode DVDs and other sources to MPEG-4 and MKV
Summary(pl.UTF-8):	Program do przekodowywania DVD i innych źródeł do formatów MPEG-4 i MKV
Name:		handbrake
Version:	1.10.2
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	https://github.com/HandBrake/HandBrake/releases/download/%{version}/HandBrake-%{version}-source.tar.bz2
# Source0-md5:	031ea98553b4653fe75211dfec1485c2
Source10:	https://gitlab.com/AOMediaCodec/SVT-AV1/-/archive/v3.1.2/SVT-AV1-v3.1.2.tar.gz
# Source10-md5:	77b9d52e8c26bacf8bca742f8448dbc1
Source11:	https://download.videolan.org/videolan/dav1d/1.5.1/dav1d-1.5.1.tar.xz
# Source11-md5:	0ab0617fd17f0aa380a71bdc4a485315
Source12:	https://ffmpeg.org/releases/ffmpeg-7.1.1.tar.bz2
# Source12-md5:	af1873e543460808f90c02e1a4e60d27
Source13:	https://download.videolan.org/pub/videolan/libbluray/1.3.4/libbluray-1.3.4.tar.bz2
# Source13-md5:	c744e610f539ba4b31280185ad48f1e1
Source14:	https://download.videolan.org/pub/videolan/libdvdnav/6.1.1/libdvdnav-6.1.1.tar.bz2
# Source14-md5:	46c46cb0294fbd1fcb8a0181818dad15
Source15:	https://download.videolan.org/pub/videolan/libdvdread/6.1.3/libdvdread-6.1.3.tar.bz2
# Source15-md5:	3c58d1624a71a16ff40f55dbaca82523
Source16:	https://github.com/FFmpeg/nv-codec-headers/releases/download/n13.0.19.0/nv-codec-headers-13.0.19.0.tar.gz
# Source16-md5:	be320d5c194da4878ded13f82fb635d7
Source17:	https://github.com/HandBrake/HandBrake-contribs/releases/download/contribs2/x265-snapshot-20250729-13276.tar.gz
# Source17-md5:	7907fd71ff37449fe3613ce3343072b6
Source18:	https://github.com/HandBrake/HandBrake-contribs/releases/download/contribs2/zimg-snapshot-20250624.tar.gz
# Source18-md5:	e97b457a54a83f72aedf413439728d0b
Patch0:		dav1d-url.patch
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
%setup -q -n HandBrake-%{version}
%patch -P0 -p1

mkdir $RPM_BUILD_DIR/HandBrake-%{version}/download
cp %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} \
	$RPM_BUILD_DIR/HandBrake-%{version}/download/

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

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/co

%{__mv} $RPM_BUILD_ROOT%{_localedir}/sl{_SI,}

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
