Summary:	A program to transcode DVDs and other sources to MPEG-4 and MKV
Name:		handbrake
Version:	1.2.2
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
URL:		http://handbrake.fr/
Source0:	https://download2.handbrake.fr/%{version}/HandBrake-%{version}-source.tar.bz2
# Source0-md5:	282924665fa45b3b08fef66b51beaac5
# Source1 is a tarball of the downloads/ folder that contains third party
# libraries required and automatically downloaded by HandBrake the first
# time 'make' is run. If you update Source0 to a newer release you must
# recreate an updated Source1 tarball for it too!
Source1:	HandBrake-%{version}-contrib-tarballs.tar
# Source1-md5:	226891f181995e2ea7c8ab018def2b46
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
BuildRequires:	gtk-webkit3-devel
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
BuildRequires:	subversion
BuildRequires:	udev-glib-devel
BuildRequires:	yasm
BuildRequires:	zlib-devel
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HandBrake is an open-source, GPL-licensed, multi-platform,
multi-threaded transcoder, available for MacOS X, Linux and Windows.

%package gui
Summary:	A program to transcode DVDs and other sources to MPEG-4 and MKV
Group:		Applications/Multimedia
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-ugly
Requires:	gtk+3
Requires:	libdvdcss
Obsoletes:	HandBrake
Obsoletes:	handbrake

%package cli
Summary:	A program to transcode DVDs and other sources to MPEG-4 and MKV
Group:		Applications/Multimedia
Requires:	gtk-update-icon-cache
Requires:	libdvdcss
Obsoletes:	HandBrake
Obsoletes:	handbrake

%description gui
HandBrake is an open-source, GPL-licensed, multi-platform,
multi-threaded transcoder, available for MacOS X, Linux and Windows.

This is the GTK GUI version of HandBrake.

%description cli
HandBrake is an open-source, GPL-licensed, multi-platform,
multi-threaded transcoder, available for MacOS X, Linux and Windows.

This is the CLI tool version of HandBrake.

%prep
%setup -q -n HandBrake-%{version} -a1

%build
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"
./configure \
	--prefix=%{_prefix} \
	--disable-df-fetch
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
cat > build/GNUmakefile.custom.defs <<EOF
CONF.args = --prefix=$RPM_BUILD_ROOT%{_prefix}
PREFIX    = $RPM_BUILD_ROOT%{_prefix}
PREFIX/   = $RPM_BUILD_ROOT%{_prefix}/
EOF
%{__make} -C build install

%{__rm} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache

%{__mv} $RPM_BUILD_ROOT%{_localedir}/it{_IT,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/ja{_JP,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{no,nb}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/ro{_RO,}

%find_lang ghb

%clean
rm -rf $RPM_BUILD_ROOT

%post gui
%update_icon_cache hicolor

%postun gui
%update_icon_cache hicolor

%files gui -f ghb.lang
%defattr(644,root,root,755)
%doc COPYING AUTHORS.markdown NEWS.markdown README.markdown THANKS.markdown
%attr(755,root,root) %{_bindir}/ghb
%{_desktopdir}/fr.handbrake.ghb.desktop
%{_iconsdir}/hicolor/scalable/apps/hb-icon.svg
%{_iconsdir}/hicolor/scalable/apps/fr.handbrake.ghb.svg
%{_datadir}/metainfo/fr.handbrake.ghb.appdata.xml

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/HandBrakeCLI
