Name:           golang-github-calmh-xdr
Summary:        XDR enc/decoder for Go
Epoch:          1
Version:        1.1.0
Release:        2%{?dist}
License:        MIT

# https://github.com/calmh/xdr
%global repo    xdr
%global goipath github.com/calmh/%{repo}
%global tag     v1.1.0

%gometa

URL:            %{gourl}
Source0:        %{gourl}/archive/%{tag}/%{repo}-%{version}.tar.gz

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%build
%gobuildroot

%gobuild -o _bin/cmd/genxdr %{goipath}/cmd/genxdr


%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 _bin/cmd/genxdr %{buildroot}%{_bindir}

%goinstall


%check
%gochecks


%files
%license LICENSE
%doc README.md

%{_bindir}/genxdr


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1:1.1.0-2
- Use standard GitHub SourceURL again for consistency between releases.
- Use forgeautosetup instead of gosetup.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 1:1.1.0-1
- Update to 'new' version 1.1.0.
- Update to spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.0-0.1.git08e072f
- First package for Fedora

