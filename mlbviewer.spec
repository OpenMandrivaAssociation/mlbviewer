Name:		mlbviewer
Summary:	mlb.tv viewing tools
Version:	0.1alpha8
Release:	%{mkrel 1}
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.eds.org/~straycat/mlblinux.php
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
Requires:	python-simplejson
Requires:	mplayer
Requires:	ffmpeg
Requires:	xterm

%description
A collection of tools to view and listen to streaming baseball games
from mlb.tv. Please note that mlbviewer is for paying subscribers to
mlb.tv: you will require a login and password from mlb.com.

%prep
%setup -q

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --compile --optimize=2
mv %{buildroot}%{_bindir}/%{name}.py %{buildroot}%{_bindir}/%{name}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
%{py_puresitedir}/MLBviewer
%{py_puresitedir}/%{name}-0.1alpha6svn-py%{pyver}.egg-info
