Name:           oonl
Version:        0.1.0
Release:        1%{?dist}
Summary:        Configurable line numbering utility with page header, body, and footer separation.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oonl
Source0:        oonl-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oonl is a sovereign, capability-bounded LINE NUMBERER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oonl
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oonl-uninstall

%files
/usr/bin/oonl
/usr/bin/oonl-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
