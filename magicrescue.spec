Summary:	Recovery tool using "magic bytes"
Name:		magicrescue
Version:	1.1.9
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://www.itu.dk/people/jobr/magicrescue/release/%{name}-%{version}.tar.gz
# Source0-md5:	093ac491bc5f70c4b050e57e3437ab07
URL:		http://www.itu.dk/people/jobr/magicrescue/
BuildRequires:	db-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Magic Rescue scans a block device for file types it knows how to
recover and calls an external program to extract them. It looks at
"magic bytes" in file contents, so it can be used both as an undelete
utility and for recovering a corrupted drive or partition.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%{__mv} $RPM_BUILD_ROOT{%{_prefix}/man,%{_mandir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/dupemap
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/magicsort
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/recipes
%dir %{_datadir}/%{name}/tools
%attr(755,root,root) %{_datadir}/%{name}/tools/*
%{_mandir}/man1/*.1*
