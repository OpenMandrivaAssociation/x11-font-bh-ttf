Name: x11-font-bh-ttf
Version: 1.0.3
Release: %mkrel 1
Summary: Xorg X11 font bh-ttf
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-bh-ttf-%{version}.tar.bz2
# We may not modify the software!
License: Bigelow & Holmes Font License
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11 <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font bh-ttf

%prep
%setup -q -n font-bh-ttf-%{version}

%build
./configure --prefix=/usr --x-includes=%{_includedir}\
	    --x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/TTF

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/TTF/fonts.dir
rm -f %{buildroot}%_datadir/fonts/TTF/fonts.scale

%post
mkfontscale %_datadir/fonts/TTF
mkfontdir %_datadir/fonts/TTF

%postun
mkfontscale %_datadir/fonts/TTF
mkfontdir %_datadir/fonts/TTF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%_datadir/fonts/TTF/luxi*.ttf
/usr/etc/fonts/conf/conf.avail/42-luxi-mono.conf
/usr/etc/fonts/conf/conf.d/42-luxi-mono.conf
