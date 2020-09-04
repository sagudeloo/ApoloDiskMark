%global pypi_name crazydiskmark
%global debug_package %{nil}
Name:           python-%{pypi_name}
Version:        0.5.4
Release:        1%{?dist}
Summary:        Linux disk benchmark tool like CrystalDiskMark

License:        MIT
URL:            https://github.com/fredcox/crazydiskmark
Source0:        %{pypi_source}
BuildArch:      noarch

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
# install desktop file
desktop-file-install                                    \
  --dir=%{buildroot}%{_datadir}/applications              \
  $RPM_BUILD_DIR/%{pypi_name}-%{version}/%{pypi_name}/%{pypi_name}.desktop
# install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install $RPM_BUILD_DIR/%{pypi_name}-%{version}/%{pypi_name}/images/%{pypi_name}_icon.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{pypi_name}_icon.png
# install manual
mkdir -p %{buildroot}%{_datadir}/man/man1/
install $RPM_BUILD_DIR/%{pypi_name}-%{version}/%{pypi_name}.1.gz \
  %{buildroot}%{_datadir}/man/man1/%{pypi_name}.1.gz





%files -n python3-%{pypi_name}
%doc README.me
%{_bindir}/crazydiskmark
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{_datadir}/applications/%{pypi_name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{pypi_name}_icon.png
%{_mandir}/man1/crazydiskmark.1.gz

%changelog
* Fri Sep 4 2020 Fred Lins <fredcox@gmail.com>
- 0.5.4-1
- First release for Fedora
