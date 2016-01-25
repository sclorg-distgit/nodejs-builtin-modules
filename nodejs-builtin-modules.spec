%{?scl:%scl_package nodejs-builtin-modules}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-builtin-modules

%global npm_name builtin-modules
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-builtin-modules
Version:	1.1.0
Release:	1%{?dist}
Summary:	List of the Node.js builtin modules
Url:		https://github.com/sindresorhus/builtin-modules#readme
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(ava)
BuildRequires:	%{?scl_prefix}npm(xo)
%endif

%description
List of the Node.js builtin modules

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/builtin-modules

%doc readme.md license

%changelog
* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 1.1.0-1
- Initial build
