Name:           m2vrequantiser
Version:        20030929
Release:        3%{?dist}
Summary:        MPEG-2 stream requantizer

Group:          Applications/Multimedia
License:        GPL+
URL:            http://www.metakine.com/
Source0:        http://www.xeatre.tv/community/burn/contrib/M2VRequantizer.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
M2VRequantiser is a tool to requantize MPEG-2 streams without
recompressing.


%prep
%setup -q -n M2VRequantizer
rm -f requant


%build
%{__cc} $RPM_OPT_FLAGS -lm -o requant main.c


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 requant $RPM_BUILD_ROOT%{_bindir}/requant
ln -s requant $RPM_BUILD_ROOT%{_bindir}/M2VRequantiser


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/M2VRequantiser
%{_bindir}/requant



%changelog
* Sat Sep 20 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 20030929-3
- rebuild for rpmfusion

* Wed Aug 22 2007 Ville Skyttä <ville.skytta at iki.fi> - 20030929-2
- License: GPL+

* Mon Dec 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 20030929-1
- First RLO build.

* Thu Aug 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 20030929-0.1
- First build.
