Summary:	A cool game for GNOME
Name: 		gnome-breakout
Version:        0.5.3
Epoch:	        1
Release:	%mkrel 3
License:	GPLv2+
Group:		Games/Arcade
Source:		http://www.users.on.net/mipearson/%name-%version.tar.bz2
Patch1: 01_makefile_fixes.dpatch
Patch3: 03_configure_fixes.dpatch
Patch4: 04_po_config.dpatch
Patch5: gnome-breakout-0.5.3-fix-desktop.patch
URL:		http://www.users.on.net/mipearson/
Buildroot:	%_tmppath/%name-%version-%release-root
BuildRequires:  gnomeui2-devel
BuildRequires:  imagemagick desktop-file-utils


%description
A breakout clone for GNOME. It supports mouse and keyboard control,
multiple difficulty levels, various nifty powerups, exploding blocks,
and customizable levels.

%prep
%setup -q
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0

%build
autoreconf -f -i
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std
desktop-file-install --vendor='' --delete-original \
	--dir %buildroot%_datadir/applications \
	--add-category='GTK;GNOME;ArcadeGame;Game' \
	%buildroot%_datadir/gnome/apps/Games/*.desktop

#icons
mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
ln -s %_datadir/pixmaps/%name.png %buildroot%_liconsdir
convert -scale 32x32 %name.png %buildroot%_iconsdir/%name.png
convert -scale 16x16 %name.png %buildroot%_miconsdir/%name.png

%find_lang %name

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -fr %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%_bindir/gnome-breakout
%_datadir/pixmaps/*
%_datadir/applications/*.desktop
%_datadir/%name
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png
%attr(664, games, games) %{_localstatedir}/lib/games/*
