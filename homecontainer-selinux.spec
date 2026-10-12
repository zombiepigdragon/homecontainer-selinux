%global selinuxtype targeted
%global modulename  homecontainer

Name:           homecontainer-selinux
Version:        1.0
Release:        2
Summary:        SELinux domain for containers that need access to user home files
License:        MIT
URL:            https://github.com/zombiepigdragon/homecontainer-selinux
Source0:        %{modulename}.cil
BuildArch:      noarch

BuildRequires:  selinux-policy-devel
Requires:       udica
Requires(post): udica
%{?selinux_requires}

%description
Custom SELinux container domain (homecontainer.process) with read/write
access to user_home_t, for use with SecurityLabelType= in quadlets.

%prep

%build

%install
install -D -m 0644 %{SOURCE0} \
    %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.cil

%post
%selinux_modules_install -s %{selinuxtype} %{_datadir}/udica/templates/base_container.cil %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.cil

%postun
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

# Reload udica's base template whenever udica itself is updated
%triggerin -- udica
%selinux_modules_install -s %{selinuxtype} %{_datadir}/udica/templates/base_container.cil

%files
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.cil

%changelog
* Mon Oct 12 2026 Alex Rawson <ajzecrom@gmail.com> - 1.0-2
- Fix scriptlet argument handling
* Mon Oct 12 2026 Alex Rawson <ajzecrom@gmail.com> - 1.0-1
- Initial package
