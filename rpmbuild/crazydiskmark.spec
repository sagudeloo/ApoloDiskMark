%global pypi_name crazydiskmark
%global debug_package %{nil}
Name:           python-%{pypi_name}
Version:        0.4.9
Release:        1%{?dist}
Summary:        Linux disk benchmark tool like CrystalDiskMark

License:        MIT
URL:            https://github.com/fredcox/crazydiskmark
Source0:        %{pypi_source}
BuildArch:      x86_64

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  python3dist(setuptools)

%description
  Crazy DiskMark is a utility to benchmark SSD disks on linux and produce
results like CrystalDiskMark.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(coloredlogs)
Requires:       python3dist(humanfriendly)
Requires:       python3dist(pyqt5)
Requires:       fio
%description -n python3-%{pypi_name}
  Crazy DiskMark is a utility to benchmark SSD disks on linux and produce
results like CrystalDiskMark.


%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
# Prepare to download and install desktop file
mkdir -p %{buildroot}/%{_datadir}/applications
curl https://raw.githubusercontent.com/fredcox/crazydiskmark/master/crazydiskmark/crazydiskmark.desktop \
  --output %{buildroot}/%{_datadir}/applications/crazydiskmark.desktop
# Prepare to download and install icon file
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps
curl https://raw.githubusercontent.com/fredcox/crazydiskmark/master/crazydiskmark/images/crazydiskmark_icon.png \
  --output %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/crazydiskmark_icon.png


%files -n python3-%{pypi_name}
%doc README.md
%{_bindir}/crazydiskmark
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{_datadir}/icons/hicolor/48x48/apps/crazydiskmark_icon.png
%{_datadir}/applications/crazydiskmark.desktop


%changelog
* Thu Sep 03 2020 Fred Lins - 0.4.9-1
- Release 0.4.9.
