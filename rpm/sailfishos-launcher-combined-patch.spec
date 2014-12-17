# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sailfishos-launcher-combined-patch

# >> macros
BuildArch: noarch
# << macros

Summary:    Launcher combined patches
Version:    0.0.1
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   lipstick-jolla-home-qt5 >= 0.22.44.7

%description
A homescreen patches for changing launcher grid size and adding new icon style showing folder icons


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-launcher-combined-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-launcher-combined-patch
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-launcher-combined-patch
# >> files
# << files