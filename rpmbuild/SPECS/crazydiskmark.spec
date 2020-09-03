# Created by pyp2rpm-3.3.4
%global pypi_name crazydiskmark

Name:           python-%{pypi_name}
Version:        0.4.8
Release:        1%{?dist}
Summary:        Linux disk benchmark tool like CrystalDiskMark

License:        None
URL:            https://github.com/fredcox/crazydiskmark
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Crazy DiskMark![Crazy DiskMark - Logo]( [About](about) *
[Dependencies](dependencies) * [Install](install) * [Buy me a Coffee](buy-me-a-
coffee) * [License](license) Please, this program is made to run in SSD´s only.
Don´t try to run this app in mechanical disks. Thank you. About***Crazy
DiskMark*** is a utility to benchmark ***SSD*** disks on linux and produce
results like...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(coloredlogs)
Requires:       python3dist(humanfriendly)
Requires:       python3dist(pyqt5)
%description -n python3-%{pypi_name}
 Crazy DiskMark![Crazy DiskMark - Logo]( [About](about) *
[Dependencies](dependencies) * [Install](install) * [Buy me a Coffee](buy-me-a-
coffee) * [License](license) Please, this program is made to run in SSD´s only.
Don´t try to run this app in mechanical disks. Thank you. About***Crazy
DiskMark*** is a utility to benchmark ***SSD*** disks on linux and produce
results like...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{_bindir}/crazydiskmark
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Sep 03 2020 Fred Lins - 0.4.8-1
- Initial package.
