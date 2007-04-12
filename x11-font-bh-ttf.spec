Name: x11-font-bh-ttf
Version: 1.0.0
Release: %mkrel 4
Summary: Xorg X11 font bh-ttf
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-bh-ttf-%{version}.tar.bz2
License: CHECK
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch

BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11 <= 6.9.0
PreReq: mkfontdir
PreReq: mkfontscale

%description
Xorg X11 font bh-ttf

%prep
%setup -q -n font-bh-ttf-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
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
%_datadir/fonts/TTF/luxi*.ttf


