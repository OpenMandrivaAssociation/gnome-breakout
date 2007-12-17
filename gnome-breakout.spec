Summary:	A cool game for GNOME
Name: 		gnome-breakout
Version:        0.5.3
Epoch:	        1
Release:	%mkrel 1
License:	GPL
Group:		Games/Arcade
Source:		http://www.users.on.net/mipearson/%name-%version.tar.bz2
Patch: gnome-breakout-0.5.2-5.patch
Patch1: gnome-breakout-0.5.2-xdg.patch
URL:		http://www.users.on.net/mipearson/
BuildRequires:  gnome-libs-devel
BuildRequires:  ImageMagick


%description
A breakout clone for GNOME. It supports mouse and keyboard control,
multiple difficulty levels, various nifty powerups, exploding blocks,
and customizable levels.

%prep

%setup -q
%patch -p1
%patch1 -p1 -b .xdg

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std GETTEXT_PACKAGE=%name
mv %buildroot%_datadir/gnome/apps/Games/ %buildroot%_datadir/applications

install -d -m 0755 %buildroot/%_menudir
cat > %buildroot/%_menudir/%name <<EOF
?package(%{name}): \
command="gnome-breakout" \
title="Gnome-Breakout" \
longtitle="Gnome breakout" \
icon="%name.png" \
needs="x11" \
section="More Applications/Games/Arcade" xdg="true"
EOF

#icons
mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
ln -s %_datadir/pixmaps/%name.png %buildroot%_liconsdir
convert -scale 32x32 %name.png %buildroot%_iconsdir/%name.png
convert -scale 16x16 %name.png %buildroot%_miconsdir/%name.png

%find_lang %name

%post
%update_menus

%postun
%clean_menus

%clean
rm -fr %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%_bindir/gnome-breakout
%_datadir/pixmaps/*
%_datadir/applications
%_datadir/%name/
%_menudir/*
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png
%attr(664, games, games) %{_localstatedir}/games/*
