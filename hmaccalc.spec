#
# TODO: disable non-FIPS (md*), currently fails with "Error ensuring FIPS mode."
#
Summary:	Tools for computing and checking HMAC values for files
Name:		hmaccalc
Version:	0.9.12
Release:	2
License:	MIT
Group:		Base
Source0:	https://fedorahosted.org/released/hmaccalc/%{name}-%{version}.tar.gz
# Source0-md5:	bf1e70cac02f6cfa85826b8878a27985
URL:		https://fedorahosted.org/hmaccalc/
Patch0:		no-md4.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	nss-devel
BuildRequires:	pkgconfig
Suggests:	prelink
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The hmaccalc package contains tools which can calculate HMAC
(hash-based message authentication code) values for files. The names
and interfaces are meant to mimic the sha*sum tools provided by the
coreutils package.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
PRELINK_CMD=/usr/sbin/prelink \
%configure \
	--enable-sum-directory=%{_libdir}/%{name} \
	--enable-non-fips

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/md2hmac
%attr(755,root,root) %{_bindir}/md5hmac
%attr(755,root,root) %{_bindir}/sha1hmac
%attr(755,root,root) %{_bindir}/sha256hmac
%attr(755,root,root) %{_bindir}/sha384hmac
%attr(755,root,root) %{_bindir}/sha512hmac
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/md2hmac.hmac
%{_libdir}/%{name}/md5hmac.hmac
%{_libdir}/%{name}/sha1hmac.hmac
%{_libdir}/%{name}/sha256hmac.hmac
%{_libdir}/%{name}/sha384hmac.hmac
%{_libdir}/%{name}/sha512hmac.hmac
%{_mandir}/man8/*hmac.8*
