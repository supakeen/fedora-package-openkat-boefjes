Name:           openkat-boefjes
Version:        main
Release:        1%{?dist}
Summary:        The OpenKAT system 'boefjes'.

License:        EUPL 1.2
URL:            https://openkat.nl
Source0:        https://github.com/minvws/nl-kat-boefjes/archive/refs/heads/main.zip
Patch0:         pyproject.patch

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:       rabbitmq

%global _description %{expand:
openkat-boefjes contains the 'boefjes' (test scripts) for the openkat project
}

%description %_description

%prep
%autosetup -p1 -n nl-kat-mula-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files scheduler

%check
%pyproject_check_import
# no pytest yet, it fails

%files -n kat-mula -f %{pyproject_files}
/usr/bin/kat-mula

%doc README.md
%license LICENSE

%changelog
* Wed Jul 6 2022 supakeen <cmdr@supakeen.com>
- Initial version of the package.
