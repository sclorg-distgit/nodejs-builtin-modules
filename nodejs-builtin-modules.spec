%{?scl:%scl_package nodejs-delegates}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename builtin-modules
%global enable_tests 0

Name:		%{?scl_prefix}nodejs-builtin-modules
Version:	1.1.1
Release:	4%{?dist}
Summary:	List of the Node.js builtin modules

License:	MIT
URL:		https://github.com/sindresorhus/builtin-modules.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/sindresorhus/builtin-modules/d317be16fab701f2ac73bc9aa771f60ec052ed66/test.js

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif


BuildRequires:	%{?scl_prefix}nodejs-devel
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(ava)
%endif

#Requires:	nodejs

%description
List of the Node.js builtin modules


%prep
%setup -q -n package
# setup the tests
cp -p %{SOURCE1} .



%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr *.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{_bindir}/xo && %{_bindir}/ava
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}



%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.1-4
- rebuilt

* Thu Feb 11 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.1-3
- Initial packaging for RHEL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Jared Smith <jsmith@fedoraproject.org> - 1.1.1-1
- Update to upstream 1.1.1 release

* Mon Oct 26 2015 Jared Smith <jsmith@fedoraproject.org> - 1.1.0-1
- Initial packaging
