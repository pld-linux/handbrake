Summary:	A program to transcode DVDs and other sources to MPEG-4 and MKV
Name:		handbrake
Version:	0.9.5
Release:	0.1
License:	GPL v2+
Group:		Applications/Multimedia
URL:		http://handbrake.fr/
# in order to get HandBrake to identify itself as version 0.9.5 rather
# than svn rev3735 the source code tarball has been generated as follows:
# svn co -r 3735 svn://svn.handbrake.fr/HandBrake/tags/0.9.5 HandBrake-0.9.5
# tar cvfj HandBrake-0.9.5.tar.bz2 HandBrake-0.9.5/
Source0:	HandBrake-%{version}.tar.bz2
# Source0-md5:	31e75e6d26ed02a2355e1b898d4587a4
# Source1 is a tarball of the downloads/ folder that contains third party
# libraries required and automatically downloaded by HandBrake the first
# time 'make' is run. If you update Source0 to a newer release you must
# recreate an updated Source1 tarball for it too!
Source1:	HandBrake-%{version}-contrib-tarballs.tar.bz2
# Source1-md5:	4a5c76949ebe23210d5e21c2a316b308
Patch0:		disable-download.patch
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-webkit-devel
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	m4
BuildRequires:	python
BuildRequires:	subversion
BuildRequires:	udev-glib-devel
BuildRequires:	yasm
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HandBrake is an open-source, GPL-licensed, multi-platform,
multi-threaded transcoder, available for MacOS X, Linux and Windows.

%package gui
Summary:	A program to transcode DVDs and other sources to MPEG-4 and MKV
Group:		Applications/Multimedia
Requires:	gstreamer-ffmpeg
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-ugly
Requires:	gtk+2
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
%patch0 -p1

install -d _docs
iconv -f ISO-8859-1 -t UTF-8 CREDITS > _docs/CREDITS
iconv -f ISO-8859-1 -t UTF-8 THANKS > _docs/THANKS

%build
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"
./configure \
	--prefix=%{_prefix}
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
install -Dp gtk/src/hb-icon.64.png \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/hb-icon.png

%clean
rm -rf $RPM_BUILD_ROOT

%post gui
%update_icon_cache_post hicolor

%postun gui
%update_icon_cache_post hicolor

%files gui
%defattr(644,root,root,755)
%doc AUTHORS COPYING _docs/CREDITS NEWS _docs/THANKS TRANSLATIONS
%attr(755,root,root) %{_bindir}/ghb
%{_desktopdir}/ghb.desktop
%{_iconsdir}/hicolor/64x64/apps/hb-icon.png
%{_iconsdir}/hicolor/128x128/apps/hb-icon.png

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/HandBrakeCLI
